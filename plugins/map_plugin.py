import logging
import re
from itertools import count
from operator import itemgetter

from sqlalchemy import func, distinct
from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from dao import MapGenDao as mapgendao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🗺Map)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        await create_map_overview(1, event, True, bot, from_id)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"mapjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                if page:
                    await create_map_overview(int(page), event, False, bot, from_id)

def list_offset(lst, offset):
    if offset == 0:
        return lst[1:11]
    if offset == 10:
        return lst[11:21]
    if offset == 20:
        return lst[21:31]
    if offset == 30:
        return lst[31:41]
    if offset == 40:
        return lst[41:51]

async def create_map_overview(page, event, send_new, bot, from_id):
    page_size = 10

    offset = (int(page) - 1) * page_size
    counter = mapgendao.calculate_all_distances(from_id)
    map_count = len(counter)
    if map_count > 0:
        max_pages = (map_count // page_size)
        if (map_count // page_size) > 0:
            max_pages += 1
            if page <= max_pages:
                maps = mapgendao.calculate_all_distances(from_id)
                maps_overview_list = ['<b>On the 🗺Map:</b>\n<i>Showing villages within a 10x10 border.</i>\n']
                if maps:
                    for map in list_offset(maps, offset):
                        maps_overview_list.append('👤')
                        maps_overview_list.append(str(villagedao.get_village_owner_player_name(map.pk)))
                        maps_overview_list.append('🏯<code>')
                        maps_overview_list.append(map.village_name)
                        maps_overview_list.append('</code> /view_vil')
                        maps_overview_list.append(str(map.pk))
                        maps_overview_list.append('\n')
                        maps_overview_list.append('🗺')
                        maps_overview_list.append(villagedao.get_overview_coordinates(map.pk))
                        maps_overview_list.append(' 🏆')
                        maps_overview_list.append(str(prof.get_village_overview_points(map.pk)))
                        maps_overview_list.append(' 📍')
                        maps_overview_list.append(str(mapgendao.calculate_village_distance(from_id, map.pk)))
                        maps_overview_list.append('\n')
                        maps_overview_list.append('⚔/attack_')
                        maps_overview_list.append(str(map.pk))
                        maps_overview_list.append(' 🛡/support_')
                        maps_overview_list.append(str(map.pk))
                        maps_overview_list.append(' 🎭/trade_')
                        maps_overview_list.append(str(map.pk))
                        maps_overview_list.append('\n\n')

                else:
                    maps_overview_list.append('\n\n- no villages on map -')

                maps_overview_text = ''.join(maps_overview_list)

                maps_paging_buttons = []

                if page > 1:
                    prev_1_button = Button.inline('◀️', bytes('mapjump_' + str(int(page) - 1), encoding='utf-8'))
                    maps_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('mapjump_' + str(int(page) + 1), encoding='utf-8'))
                    maps_paging_buttons.append(next_1_button)

                if send_new == True:
                    if len(maps_paging_buttons) > 0:
                        await bot.send_message(entity=event.chat_id, message=maps_overview_text, buttons=maps_paging_buttons, parse_mode='html')
                    else:
                        await bot.send_message(entity=event.chat_id, message=maps_overview_text, parse_mode='html')
                elif send_new == False:
                    if len(maps_paging_buttons) > 0:
                        await bot.edit_message(entity=event.chat_id, message=event.message_id, text=maps_overview_text, buttons=maps_paging_buttons, parse_mode='html')
                    else:
                        await bot.edit_message(entity=event.chat_id, message=event.message_id, text=maps_overview_text, parse_mode='html')

    elif map_count is 0:
        return_message = 'You don\'t own any maps. It\'s time to make a choice. /reclaim a new land or remain waiting in the shadows.'
        return return_message
