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
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🥇Tops)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        default_keyboard = buttons.get_toplist_keyboard()
                        await bot.send_message(entity=int(event.chat_id), message=str('Select a 🥇Toplist you\'re interested in.'),buttons=default_keyboard , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏆Top)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_players_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"toppointsjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_players_overview(int(page), event, False, session, bot)

    async def create_players_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        player_count = session.query(func.count(Player.points)).filter(Player.villages > 0).order_by(Player.points.asc()).scalar()
        if player_count > 0:
            max_pages = (player_count // page_size)
            if (player_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                players = session.query(Player).filter(Player.villages > 0).order_by(Player.points.desc()).limit(page_size).offset(offset).all()
                players_overview_list = ['<b>Top Players In EmpireConquest:</b>\n']
                if players:
                    if page >= 1:
                        i = page * 10 - 10
                        for player in players:
                            i = int(i+1)
                            if i == 1:
                                players_overview_list.append(str('🥇'))
                            elif i == 2:
                                players_overview_list.append(str('🥈'))
                            elif i == 3:
                                players_overview_list.append(str('🥉'))
                            else:
                                players_overview_list.append(str(i))
                            players_overview_list.append('. 👤')
                            players_overview_list.append(str(prof.cur_player(player.tg_id)))
                            players_overview_list.append(' /pp')
                            players_overview_list.append(str(prof.cur_player_id(player.tg_id)))
                            players_overview_list.append('\n')
                            players_overview_list.append('      └🏆')
                            players_overview_list.append(str(prof.player_points(player.tg_id)))
                            players_overview_list.append(' 🏯')
                            players_overview_list.append(str(player.villages))
                            players_overview_list.append(' (/🏆')
                            players_overview_list.append(str(player.avg_vil_point))
                            players_overview_list.append(')')
                            players_overview_list.append('\n')

                        players_overview_list.append('Showing ')
                        players_overview_list.append(str(offset + 1))
                        players_overview_list.append(' to ')
                        players_overview_list.append(str(offset + len(players)))
                        players_overview_list.append(' from ')
                        players_overview_list.append(str(player_count))
                        players_overview_list.append(' player(s).')

                    else:
                        players_overview_list.append('\n\n- no players-')


                players_overview_text = ''.join(players_overview_list)

                players_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('toppointsjump_1', encoding='utf-8'))
                    players_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('toppointsjump_' + str(int(page) - 5), encoding='utf-8'))
                        players_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('toppointsjump_' + str(int(page) - 1), encoding='utf-8'))
                    players_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('toppointsjump_' + str(int(page) + 1), encoding='utf-8'))
                    players_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('toppointsjump_' + str(int(page) + 5), encoding='utf-8'))
                        players_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('toppointsjump_' + str(max_pages), encoding='utf-8'))
                    players_paging_buttons.append(next_all_button)

                default_buttons = buttons.get_toplist_keyboard()
                if send_new:
                    if len(players_paging_buttons) > 0:
                        await bot.send_message(entity=event.chat_id, message=players_overview_text, buttons=players_paging_buttons, parse_mode='html')
                    else:
                        await bot.send_message(entity=event.chat_id, message=players_overview_text, parse_mode='html')
                else:
                    if len(players_paging_buttons) > 0:
                        await bot.edit_message(entity=event.chat_id, message=event.message_id, text=players_overview_text, buttons=players_paging_buttons, parse_mode='html')
                    else:
                        await bot.edit_message(entity=event.chat_id, message=event.message_id, text=players_overview_text, parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏰Top)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_villages_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"topvillagesjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                village_pk = prof.cur_village_id(from_id)
                if page:
                    await create_villages_overview(int(page), event, False, session, bot)

    async def create_villages_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        village_count = session.query(func.count(Player.villages)).filter(Player.villages > 0).order_by(Player.villages.asc()).scalar()
        if village_count > 0:
            max_pages = (village_count // page_size)
            if (village_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                villages = session.query(Player).filter(Player.villages > 0).order_by(Player.villages.desc()).limit(page_size).offset(offset).all()
                villages_overview_list = ['<b>Top players by most villages:</b>\n']
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
                            villages_overview_list.append(str(prof.cur_player(village.tg_id)))
                            villages_overview_list.append(' /pp')
                            villages_overview_list.append(str(prof.cur_player_id(village.tg_id)))
                            villages_overview_list.append('\n')
                            villages_overview_list.append('      └🏆')
                            villages_overview_list.append(str(prof.player_points(village.tg_id)))
                            villages_overview_list.append(' 🏯')
                            villages_overview_list.append(str(village.villages))
                            villages_overview_list.append(' (/🏆')
                            villages_overview_list.append(str(village.avg_vil_point))
                            villages_overview_list.append(')')
                            villages_overview_list.append('\n')

                        villages_overview_list.append('Showing ')
                        villages_overview_list.append(str(offset + 1))
                        villages_overview_list.append(' to ')
                        villages_overview_list.append(str(offset + len(villages)))
                        villages_overview_list.append(' from ')
                        villages_overview_list.append(str(village_count))
                        villages_overview_list.append(' player(s).')

                    else:
                        villages_overview_list.append('\n\n- no villages-')


                villages_overview_text = ''.join(villages_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('topvillagesjump_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('topvillagesjump_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('topvillagesjump_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('topvillagesjump_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('topvillagesjump_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('topvillagesjump_' + str(max_pages), encoding='utf-8'))
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

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏰Avg)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_avgvillages_overview(1, event, True, session, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"topvillagesavgjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                village_pk = prof.cur_village_id(from_id)
                if page:
                    await create_avgvillages_overview(int(page), event, False, session, bot)

    async def create_avgvillages_overview(page, event, send_new, session, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        village_count = session.query(func.count(Player.avg_vil_point)).filter(Player.villages > 0).order_by(Player.avg_vil_point.asc()).scalar()
        if village_count > 0:
            max_pages = (village_count // page_size)
            if (village_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                villages = session.query(Player).filter(Player.villages > 0).order_by(Player.avg_vil_point.desc()).limit(page_size).offset(offset).all()
                villages_overview_list = ['<b>Highest average village points:</b>\n']
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
                            villages_overview_list.append(str(prof.cur_player(village.tg_id)))
                            villages_overview_list.append(' /pp')
                            villages_overview_list.append(str(prof.cur_player_id(village.tg_id)))
                            villages_overview_list.append('\n')
                            villages_overview_list.append('      └🏆')
                            villages_overview_list.append(str(prof.player_points(village.tg_id)))
                            villages_overview_list.append(' 🏯')
                            villages_overview_list.append(str(village.villages))
                            villages_overview_list.append(' (/🏆')
                            villages_overview_list.append(str(village.avg_vil_point))
                            villages_overview_list.append(')')
                            villages_overview_list.append('\n')

                        villages_overview_list.append('Showing ')
                        villages_overview_list.append(str(offset + 1))
                        villages_overview_list.append(' to ')
                        villages_overview_list.append(str(offset + len(villages)))
                        villages_overview_list.append(' from ')
                        villages_overview_list.append(str(village_count))
                        villages_overview_list.append(' player(s).')

                    else:
                        villages_overview_list.append('\n\n- no villages-')


                villages_overview_text = ''.join(villages_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('topvillagesavgjump_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('topvillagesavgjump_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('topvillagesavgjump_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('topvillagesavgjump_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('topvillagesavgjump_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('topvillagesavgjump_' + str(max_pages), encoding='utf-8'))
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