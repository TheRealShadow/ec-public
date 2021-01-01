from datetime import datetime
import logging
import re

from sqlalchemy import func, distinct
from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from models.player import Player
from models.village import Village
from models.building import Building
from models.marching import Marching
from models.reports import Reports
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as troo

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(📯Reports)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_reports_overview(1, event, True, session, player_pk, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"reportjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_reports_overview(int(page), event, False, session, player_pk, bot)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/rep_(\d+)(@.*)?'))
    async def handler(event):
        report_id = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        check_report_owner = auth.check_report_owner(from_id, report_id, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   check_report_owner)
                                               , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/delrep_(\d+)(@.*)?'))
    async def handler(event):
        report_id = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        check_report_owner = auth.check_report_owner_to_delete(from_id, report_id, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   check_report_owner)
                                               , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/delrep_all'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        report_massacre = auth.check_reports_delete(from_id, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   report_massacre)
                                               , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/read_all'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        report_massacre = auth.check_reports_set_to_read(from_id, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   report_massacre)
                                               , parse_mode='html', buttons=default_buttons)

async def create_reports_overview(page, event, send_new, session, player_pk, bot):
    page_size = 20

    offset = ((int(page) - 1) * page_size)
    report_count = session.query(func.count(Reports.owner)).filter(Reports.owner==player_pk).scalar()
    if report_count > 0:
        max_pages = (report_count // page_size)
        if (report_count % page_size) > 0:
            max_pages += 1
        if page <= max_pages:
            reports = session.query(Reports).filter(Reports.owner==player_pk).order_by(Reports.pk.desc()).limit(page_size).offset(offset).all()
            reports_overview_list = ['<b>Your 📯Reports</b>\n<i>to delete all reports, use /delrep_all.\nIf you wish to mark them all read, use /read_all</i>\n\n']
            if reports:
                for report in reports:
                    date = report.create_date
                    date_strip = datetime.strftime(date, "%Y-%m-%d %H:%M")
                    reports_overview_list.append(str(date_strip))
                    if report.read == 0:
                        reports_overview_list.append(' |✉')
                    if report.read == 1:
                        reports_overview_list.append(' |')
                    reports_overview_list.append(str(report.title))
                    reports_overview_list.append(' | /rep_')
                    reports_overview_list.append(str(report.pk))
                    reports_overview_list.append('\n')

                reports_overview_list.append('\nShowing ')
                reports_overview_list.append(str(offset + 1))
                reports_overview_list.append(' to ')
                reports_overview_list.append(str(offset + len(reports)))
                reports_overview_list.append(' from ')
                reports_overview_list.append(str(report_count))
                reports_overview_list.append(' report(s).')

            else:
                reports_overview_list.append('\n\n- no reports -')


            villages_overview_text = ''.join(reports_overview_list)

            villages_paging_buttons = []

            if page > 1:
                prev_all_button = Button.inline('⏮', bytes('reportjump_1', encoding='utf-8'))
                villages_paging_buttons.append(prev_all_button)
                if page >= 6:
                    prev_5_button = Button.inline('⏪', bytes('reportjump_' + str(int(page) - 5), encoding='utf-8'))
                    villages_paging_buttons.append(prev_5_button)
                prev_1_button = Button.inline('◀️', bytes('reportjump_' + str(int(page) - 1), encoding='utf-8'))
                villages_paging_buttons.append(prev_1_button)

            if page < max_pages:
                next_1_button = Button.inline('▶️', bytes('reportjump_' + str(int(page) + 1), encoding='utf-8'))
                villages_paging_buttons.append(next_1_button)

                if (page + 5) <= max_pages:
                    next_5_button = Button.inline('⏩', bytes('reportjump_' + str(int(page) + 5), encoding='utf-8'))
                    villages_paging_buttons.append(next_5_button)
                next_all_button = Button.inline('⏭', bytes('reportjump_' + str(max_pages), encoding='utf-8'))
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
    elif report_count == 0:
        await bot.send_message(entity=event.chat_id, message='You don\'t have any reports to read. Try attacking someone.', parse_mode='html')