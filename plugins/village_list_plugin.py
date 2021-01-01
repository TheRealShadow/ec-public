import logging
import re

from sqlalchemy import func, distinct
from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from dao import WarDao as wardao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏰List)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_villages_overview(1, event, True, session, player_pk, bot)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/vil(\d+)(@.*)?'))
    async def handler(event):
        selecting_village = event.pattern_match.group(1)
        selecting_village = int(selecting_village)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        chosen_village = vill.selecting_another_village(from_id, selecting_village)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   chosen_village)
                                               , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/rename_vil(\d+) (.*)'))
    async def handler(event):
        village = event.pattern_match.group(1)
        village = int(village)
        new_name = event.pattern_match.group(2)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        new_village_name = vill.rename_village_village(from_id, village, new_name)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   new_village_name)
                                               , parse_mode='html')


    @bot.on(events.CallbackQuery(pattern=re.compile(r"villagejump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_villages_overview(int(page), event, False, session, player_pk, bot)

async def create_villages_overview(page, event, send_new, session, player_pk, bot):
    page_size = 10

    offset = ((int(page) - 1) * page_size)
    village_count = session.query(func.count(Village.village_name)).filter(Village.owner_pk==player_pk).order_by(Village.village_name.asc()).scalar()
    if village_count > 0:
        max_pages = (village_count // page_size)
        if (village_count % page_size) > 0:
            max_pages += 1
        if page <= max_pages:
            villages = session.query(Village).filter(Village.owner_pk==player_pk).order_by(Village.village_name.asc()).limit(page_size).offset(offset).all()
            villages_overview_list = ['<b>Your 🏯Empire:</b>\n']
            if villages:
                for village in villages:
                    villages_overview_list.append(str(wardao.get_village_list_status(village.pk)))
                    villages_overview_list.append('🏯')
                    villages_overview_list.append(village.village_name)
                    villages_overview_list.append(' /vil')
                    villages_overview_list.append(str(village.pk))
                    villages_overview_list.append('\n')
                    villages_overview_list.append('🗺')
                    villages_overview_list.append(villagedao.get_overview_coordinates(village.pk))
                    villages_overview_list.append(' 🏆')
                    villages_overview_list.append(str(prof.get_village_overview_points(village.pk)))
                    villages_overview_list.append(' 🕯')
                    villages_overview_list.append(str(vill.get_loyalty_overview(village.pk)))
                    villages_overview_list.append('\n')
                    villages_overview_list.append(str(vill.get_current_stock_overview(village.pk)))
                    villages_overview_list.append('\n\n')

                villages_overview_list.append('Showing ')
                villages_overview_list.append(str(offset + 1))
                villages_overview_list.append(' to ')
                villages_overview_list.append(str(offset + len(villages)))
                villages_overview_list.append(' from ')
                villages_overview_list.append(str(village_count))
                villages_overview_list.append(' village(s).')

            else:
                villages_overview_list.append('\n\n- no guilds -')


            villages_overview_text = ''.join(villages_overview_list)

            villages_paging_buttons = []

            if page > 1:
                prev_all_button = Button.inline('⏮', bytes('villagejump_1', encoding='utf-8'))
                villages_paging_buttons.append(prev_all_button)
                if page >= 6:
                    prev_5_button = Button.inline('⏪', bytes('villagejump_' + str(int(page) - 5), encoding='utf-8'))
                    villages_paging_buttons.append(prev_5_button)
                prev_1_button = Button.inline('◀️', bytes('villagejump_' + str(int(page) - 1), encoding='utf-8'))
                villages_paging_buttons.append(prev_1_button)

            if page < max_pages:
                next_1_button = Button.inline('▶️', bytes('villagejump_' + str(int(page) + 1), encoding='utf-8'))
                villages_paging_buttons.append(next_1_button)

                if (page + 5) <= max_pages:
                    next_5_button = Button.inline('⏩', bytes('villagejump_' + str(int(page) + 5), encoding='utf-8'))
                    villages_paging_buttons.append(next_5_button)
                next_all_button = Button.inline('⏭', bytes('villagejump_' + str(max_pages), encoding='utf-8'))
                villages_paging_buttons.append(next_all_button)

            if send_new:
                if len(villages_paging_buttons) > 0:
                    await bot.send_message(entity=event.chat_id, message=villages_overview_text, buttons=villages_paging_buttons, parse_mode='html')
                else:
                    await bot.send_message(entity=event.chat_id, message=villages_overview_text, parse_mode='html')
            else:
                if len(villages_paging_buttons) > 0:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=villages_overview_text, buttons=villages_paging_buttons, parse_mode='html')
                else:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=villages_overview_text, parse_mode='html')
    elif village_count == 0:
        await bot.send_message(entity=event.chat_id, message='You don\'t own any villages. It\'s time to make a choice. /reclaim a new land or remain waiting in the shadows.', parse_mode='html')
