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
    @bot.on(events.NewMessage(incoming=True, pattern=r"(💀Top)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_toptotaldefeated_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"toptotaldefeated_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                village_pk = prof.cur_village_id(from_id)
                if page:
                    await create_toptotaldefeated_overview(int(page), event, False, session, bot)

    async def create_toptotaldefeated_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        village_count = session.query(func.count(Player.total_defeated_units)).filter(Player.villages > 0).order_by(Player.avg_vil_point.asc()).scalar()
        if village_count > 0:
            max_pages = (village_count // page_size)
            if (village_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                villages = session.query(Player).filter(Player.villages > 0).order_by(Player.total_defeated_units.desc()).limit(page_size).offset(offset).all()
                villages_overview_list = ['<b>Most total defeated opponents:</b>\n']
                if villages:
                    if page >= 1:
                        i = page * 10 - 10
                        for village in villages:
                            i = int(i+1)
                            if i == 1:
                                villages_overview_list.append(str('🥇'))
                            elif i == 2:
                                villages_overview_list.append(str('🥈'))
                            elif i == 3:
                                villages_overview_list.append(str('🥉'))
                            else:
                                villages_overview_list.append(str(i))
                            villages_overview_list.append('. 👤')
                            villages_overview_list.append(str(prof.player_name_by_pk(village.pk)))
                            villages_overview_list.append(' - ')
                            villages_overview_list.append('🏆')
                            villages_overview_list.append(str(prof.player_points_by_pk(village.pk)))
                            villages_overview_list.append(' /pp')
                            villages_overview_list.append(str(village.pk))
                            villages_overview_list.append('')
                            villages_overview_list.append('\n☠ ')
                            villages_overview_list.append(str(wardao.get_all_defeated_opponents(village.pk)))
                            villages_overview_list.append(' (☠⚔ ')
                            villages_overview_list.append(str(wardao.get_att_defeated_opponents(village.pk)))
                            villages_overview_list.append(' | ☠🛡 ')
                            villages_overview_list.append(str(wardao.get_def_defeated_opponents(village.pk)))
                            villages_overview_list.append(' )\n\n')

                        villages_overview_list.append('Showing ')
                        villages_overview_list.append(str(offset + 1))
                        villages_overview_list.append(' to ')
                        villages_overview_list.append(str(offset + len(villages)))
                        villages_overview_list.append(' from ')
                        villages_overview_list.append(str(village_count))
                        villages_overview_list.append(' players(s).')

                    else:
                        villages_overview_list.append('\n\n- no villages-')


                villages_overview_text = ''.join(villages_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('toptotaldefeated_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('toptotaldefeated_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('toptotaldefeated_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('toptotaldefeated_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('toptotaldefeated_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('toptotaldefeated_' + str(max_pages), encoding='utf-8'))
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

    @bot.on(events.NewMessage(incoming=True, pattern=r"(💀⚔️Top)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_topattackdefeated_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"topattackdefeated_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                village_pk = prof.cur_village_id(from_id)
                if page:
                    await create_topattackdefeated_overview(int(page), event, False, session, bot)

    async def create_topattackdefeated_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        village_count = session.query(func.count(Player.defeated_units_attack)).filter(Player.villages > 0).order_by(Player.avg_vil_point.asc()).scalar()
        if village_count > 0:
            max_pages = (village_count // page_size)
            if (village_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                villages = session.query(Player).filter(Player.villages > 0).order_by(Player.defeated_units_attack.desc()).limit(page_size).offset(offset).all()
                villages_overview_list = ['<b>Most 💀⚔defeated opponents attack:</b>\n']
                if villages:
                    if page >= 1:
                        i = page * 10 - 10
                        for village in villages:
                            i = int(i+1)
                            if i == 1:
                                villages_overview_list.append(str('🥇'))
                            elif i == 2:
                                villages_overview_list.append(str('🥈'))
                            elif i == 3:
                                villages_overview_list.append(str('🥉'))
                            else:
                                villages_overview_list.append(str(i))
                            villages_overview_list.append('. 👤')
                            villages_overview_list.append(str(prof.player_name_by_pk(village.pk)))
                            villages_overview_list.append(' - ')
                            villages_overview_list.append('🏆')
                            villages_overview_list.append(str(prof.player_points_by_pk(village.pk)))
                            villages_overview_list.append(' /pp')
                            villages_overview_list.append(str(village.pk))
                            villages_overview_list.append('')
                            villages_overview_list.append('\n☠ ')
                            villages_overview_list.append(str(wardao.get_all_defeated_opponents(village.pk)))
                            villages_overview_list.append(' (☠⚔ ')
                            villages_overview_list.append(str(wardao.get_att_defeated_opponents(village.pk)))
                            villages_overview_list.append(' | ☠🛡 ')
                            villages_overview_list.append(str(wardao.get_def_defeated_opponents(village.pk)))
                            villages_overview_list.append(' )\n\n')

                        villages_overview_list.append('Showing ')
                        villages_overview_list.append(str(offset + 1))
                        villages_overview_list.append(' to ')
                        villages_overview_list.append(str(offset + len(villages)))
                        villages_overview_list.append(' from ')
                        villages_overview_list.append(str(village_count))
                        villages_overview_list.append(' players(s).')

                    else:
                        villages_overview_list.append('\n\n- no villages-')


                villages_overview_text = ''.join(villages_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('topattackdefeated_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('topattackdefeated_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('topattackdefeated_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('topattackdefeated_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('topattackdefeated_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('topattackdefeated_' + str(max_pages), encoding='utf-8'))
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

    @bot.on(events.NewMessage(incoming=True, pattern=r"(💀🛡Top)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_topdefensedefeated_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"topdefensedefeated_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                village_pk = prof.cur_village_id(from_id)
                if page:
                    await create_topdefensedefeated_overview(int(page), event, False, session, bot)

    async def create_topdefensedefeated_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        village_count = session.query(func.count(Player.defeated_units_defense)).filter(Player.villages > 0).order_by(Player.avg_vil_point.asc()).scalar()
        if village_count > 0:
            max_pages = (village_count // page_size)
            if (village_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                villages = session.query(Player).filter(Player.villages > 0).order_by(Player.defeated_units_defense.desc()).limit(page_size).offset(offset).all()
                villages_overview_list = ['<b>Most 💀🛡defeated opponents defense:</b>\n']
                if villages:
                    if page >= 1:
                        i = page * 10 - 10
                        for village in villages:
                            i = int(i+1)
                            if i == 1:
                                villages_overview_list.append(str('🥇'))
                            elif i == 2:
                                villages_overview_list.append(str('🥈'))
                            elif i == 3:
                                villages_overview_list.append(str('🥉'))
                            else:
                                villages_overview_list.append(str(i))
                            villages_overview_list.append('. 👤')
                            villages_overview_list.append(str(prof.player_name_by_pk(village.pk)))
                            villages_overview_list.append(' - ')
                            villages_overview_list.append('🏆')
                            villages_overview_list.append(str(prof.player_points_by_pk(village.pk)))
                            villages_overview_list.append(' /pp')
                            villages_overview_list.append(str(village.pk))
                            villages_overview_list.append('')
                            villages_overview_list.append('\n☠ ')
                            villages_overview_list.append(str(wardao.get_all_defeated_opponents(village.pk)))
                            villages_overview_list.append(' (☠⚔ ')
                            villages_overview_list.append(str(wardao.get_att_defeated_opponents(village.pk)))
                            villages_overview_list.append(' | ☠🛡 ')
                            villages_overview_list.append(str(wardao.get_def_defeated_opponents(village.pk)))
                            villages_overview_list.append(' )\n\n')

                        villages_overview_list.append('Showing ')
                        villages_overview_list.append(str(offset + 1))
                        villages_overview_list.append(' to ')
                        villages_overview_list.append(str(offset + len(villages)))
                        villages_overview_list.append(' from ')
                        villages_overview_list.append(str(village_count))
                        villages_overview_list.append(' players(s).')

                    else:
                        villages_overview_list.append('\n\n- no villages-')


                villages_overview_text = ''.join(villages_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('topdefensedefeated_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('topdefensedefeated_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('topdefensedefeated_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('topdefensedefeated_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('topdefensedefeated_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('topdefensedefeated_' + str(max_pages), encoding='utf-8'))
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