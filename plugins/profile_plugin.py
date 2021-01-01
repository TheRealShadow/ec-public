import logging
import datetime
import re

from sqlalchemy import func
from telethon import events
from telethon.tl.custom import Button

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from dao import UnitDao as unitdao
from dao import RecruitmentDao as recruitmentdao
from dao import VillageDao as villagedao
from dao import WarDao as wardao
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r'/pp(\d+)(@.*)?'))
    async def handler(event):
        pp_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        await create_pps_overview(1, event, True, session, pp_pk, bot)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/view_vil(\d+)(@.*)?'))
    async def handler(event):
        village_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        create_view = vill.village_view(from_id, village_pk)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(create_view), parse_mode='html', buttons=default_buttons)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"ppjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                pp_pk = prof.cur_player_id(from_id)
                if page:
                    await create_pps_overview(int(page), event, False, session, pp_pk, bot)

async def create_pps_overview(page, event, send_new, session, pp_pk, bot):
    page_size = 10

    offset = ((int(page) - 1) * page_size)
    pp_count = session.query(func.count(Village.village_name)).filter(Village.owner_pk==pp_pk).order_by(Village.village_name.asc()).scalar()
    if pp_count > 0:
        max_pages = (pp_count // page_size)
        if (pp_count % page_size) > 0:
            max_pages += 1
        if page <= max_pages:
            pps = session.query(Village).filter(Village.owner_pk==pp_pk).order_by(Village.village_name.asc()).limit(page_size).offset(offset).all()
            pps_overview_list = ['👤']
            pps_overview_list.append(str(prof.player_name_by_pk(pp_pk)))
            pps_overview_list.append('<i> (ID:')
            pps_overview_list.append(str(pp_pk))
            pps_overview_list.append(')</i>')
            pps_overview_list.append(' - ')
            pps_overview_list.append('🏆')
            pps_overview_list.append(str(prof.player_points_by_pk(pp_pk)))
            pps_overview_list.append('\n☠ ')
            pps_overview_list.append(str(wardao.get_all_defeated_opponents(pp_pk)))
            pps_overview_list.append(' (☠⚔ ')
            pps_overview_list.append(str(wardao.get_att_defeated_opponents(pp_pk)))
            pps_overview_list.append('| ☠🛡 ')
            pps_overview_list.append(str(wardao.get_def_defeated_opponents(pp_pk)))
            pps_overview_list.append(' )')
            pps_overview_list.append(str(prof.fetch_player_telegram_username_by_pk(pp_pk)))
            pps_overview_list.append('\nEmpire has ')
            pps_overview_list.append(str(villagedao.count_user_villages_by_pk(pp_pk)))
            pps_overview_list.append(' village(s)\n🏆')
            pps_overview_list.append(str(prof.player_village_points_by_pk(pp_pk)))
            pps_overview_list.append(' avg points per village\n')
            pps_overview_list.append('\n<b>Villages in the empire:</b>\n')
            if pps:
                for pp in pps:
                    pps_overview_list.append('🏯')
                    pps_overview_list.append(str(pp.village_name))
                    pps_overview_list.append(' 🗺')
                    pps_overview_list.append(str(villagedao.get_overview_coordinates(pp.pk)))
                    pps_overview_list.append(' 🏆')
                    pps_overview_list.append(str(prof.get_village_overview_points(pp.pk)))
                    pps_overview_list.append(' /view_vil')
                    pps_overview_list.append(str(pp.pk))
                    pps_overview_list.append('\n')

                pps_overview_list.append('Showing ')
                pps_overview_list.append(str(offset + 1))
                pps_overview_list.append(' to ')
                pps_overview_list.append(str(offset + len(pps)))
                pps_overview_list.append(' from ')
                pps_overview_list.append(str(pp_count))
                pps_overview_list.append(' village(s).')

            else:
                pps_overview_list.append('\n\n- no pp -')


            pps_overview_text = ''.join(pps_overview_list)

            pps_paging_buttons = []

            if page > 1:
                prev_all_button = Button.inline('⏮', bytes('ppjump_1', encoding='utf-8'))
                pps_paging_buttons.append(prev_all_button)
                if page >= 6:
                    prev_5_button = Button.inline('⏪', bytes('ppjump_' + str(int(page) - 5), encoding='utf-8'))
                    pps_paging_buttons.append(prev_5_button)
                prev_1_button = Button.inline('◀️', bytes('ppjump_' + str(int(page) - 1), encoding='utf-8'))
                pps_paging_buttons.append(prev_1_button)

            if page < max_pages:
                next_1_button = Button.inline('▶️', bytes('ppjump_' + str(int(page) + 1), encoding='utf-8'))
                pps_paging_buttons.append(next_1_button)

                if (page + 5) <= max_pages:
                    next_5_button = Button.inline('⏩', bytes('ppjump_' + str(int(page) + 5), encoding='utf-8'))
                    pps_paging_buttons.append(next_5_button)
                next_all_button = Button.inline('⏭', bytes('ppjump_' + str(max_pages), encoding='utf-8'))
                pps_paging_buttons.append(next_all_button)

            if send_new:
                if len(pps_paging_buttons) > 0:
                    await bot.send_message(entity=event.chat_id, message=pps_overview_text, buttons=pps_paging_buttons, parse_mode='html')
                else:
                    await bot.send_message(entity=event.chat_id, message=pps_overview_text, parse_mode='html')
            else:
                if len(pps_paging_buttons) > 0:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=pps_overview_text, buttons=pps_paging_buttons, parse_mode='html')
                else:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=pps_overview_text, parse_mode='html')
        