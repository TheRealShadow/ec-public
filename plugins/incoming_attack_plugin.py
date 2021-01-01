import datetime
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
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as troo

logger = logging.getLogger(__name__)

async def init(bot, session):

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🔥Inc att)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_incoming_attack_overview(1, event, True, session, player_pk, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"allincattjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_incoming_attack_overview(int(page), event, False, session, player_pk, bot)

    async def create_incoming_attack_overview(page, event, send_new, session, player_pk, bot):
        page_size = 10

        offset = ((int(page) - 1) * page_size)
        order_count = session.query(func.count(Marching.pk)).filter(Marching.target_owner==player_pk).filter(Marching.type_march=='ATTACK').scalar()
        if order_count > 0:
            max_pages = (order_count // page_size)
            if (order_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                orders = session.query(Marching).filter(Marching.target_owner==player_pk).filter(Marching.type_march=='ATTACK').order_by(Marching.arrival_time.asc()).limit(page_size).offset(offset).all()
                orders_overview_list = ['<b>All incoming 🔥Attack(s):</b>\n']
                if orders:
                    for order in orders:
                        time_left = str(order.arrival_time - datetime.datetime.utcnow()).split(".")[0]
                        if '-1 day,' in time_left:
                            time_left = 'Soon™️'
                        orders_overview_list.append('🔥-')
                        orders_overview_list.append(str(villagedao.get_village_owner_player_name(order.from_village_id)))
                        orders_overview_list.append(' /pp')
                        orders_overview_list.append(str(order.owner_pk))
                        orders_overview_list.append('🏯')
                        orders_overview_list.append(str(villagedao.get_village_name_by_pk(order.from_village_id)))
                        orders_overview_list.append(' <i>/view_vil')
                        orders_overview_list.append(str(order.from_village_id))
                        orders_overview_list.append('</i>\n🎯')
                        orders_overview_list.append(str(villagedao.get_village_name_by_pk(order.to_village_id)))
                        orders_overview_list.append(' /vil')
                        orders_overview_list.append(str(order.to_village_id))
                        orders_overview_list.append('⏳')
                        orders_overview_list.append(str(order.arrival_time))
                        orders_overview_list.append(' | ')
                        orders_overview_list.append(str(time_left))
                        orders_overview_list.append('\n\n')

                    orders_overview_list.append('Showing ')
                    orders_overview_list.append(str(offset + 1))
                    orders_overview_list.append(' to ')
                    orders_overview_list.append(str(offset + len(orders)))
                    orders_overview_list.append(' from ')
                    orders_overview_list.append(str(order_count))
                    orders_overview_list.append(' incoming attack(s).')

                else:
                    orders_overview_list.append('\n\n- no orders -')


                villages_overview_text = ''.join(orders_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('allincattjump_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('allincattjump_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('allincattjump_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('allincattjump_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('allincattjump_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('allincattjump_' + str(max_pages), encoding='utf-8'))
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
        elif order_count == 0:
            await bot.send_message(entity=event.chat_id, message='You currently don\'t have incoming attacks. 🙂', parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🔥Inc vill att)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_incoming_vill_attack_overview(1, event, True, session, player_pk, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"villincattjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_incoming_vill_attack_overview(int(page), event, False, session, player_pk, bot)

    async def create_incoming_vill_attack_overview(page, event, send_new, session, player_pk, bot):
        page_size = 10

        village_id = prof.cur_village_id_by_pk(player_pk)
        offset = ((int(page) - 1) * page_size)
        vill_atk_count = session.query(func.count(Marching.pk)).filter(Marching.target_owner==player_pk).filter(Marching.to_village_id==village_id).filter(Marching.type_march=='ATTACK').scalar()
        if vill_atk_count > 0:
            max_pages = (vill_atk_count // page_size)
            if (vill_atk_count % page_size) > 0:
                max_pages += 1
            if page <= max_pages:
                orders = session.query(Marching).filter(Marching.target_owner==player_pk).filter(Marching.to_village_id==village_id).filter(Marching.type_march=='ATTACK').order_by(Marching.arrival_time.asc()).limit(page_size).offset(offset).all()
                orders_overview_list = ['<b>All incoming 🔥Attack(s):</b>\n']
                if orders:
                    for order in orders:
                        time_left = str(order.arrival_time - datetime.datetime.utcnow()).split(".")[0]
                        if '-1 day,' in time_left:
                            time_left = 'Soon™️'
                        orders_overview_list.append('🔥-')
                        orders_overview_list.append(str(villagedao.get_village_owner_player_name(order.from_village_id)))
                        orders_overview_list.append(' /pp')
                        orders_overview_list.append(str(order.owner_pk))
                        orders_overview_list.append('🏯')
                        orders_overview_list.append(str(villagedao.get_village_name_by_pk(order.from_village_id)))
                        orders_overview_list.append(' <i>/view_vil')
                        orders_overview_list.append(str(order.from_village_id))
                        orders_overview_list.append('</i>\n🎯')
                        orders_overview_list.append(str(villagedao.get_village_name_by_pk(order.to_village_id)))
                        orders_overview_list.append(' /vil')
                        orders_overview_list.append(str(order.to_village_id))
                        orders_overview_list.append('⏳')
                        orders_overview_list.append(str(order.arrival_time))
                        orders_overview_list.append(' | ')
                        orders_overview_list.append(str(time_left))
                        orders_overview_list.append('\n\n')

                    orders_overview_list.append('Showing ')
                    orders_overview_list.append(str(offset + 1))
                    orders_overview_list.append(' to ')
                    orders_overview_list.append(str(offset + len(orders)))
                    orders_overview_list.append(' from ')
                    orders_overview_list.append(str(vill_atk_count))
                    orders_overview_list.append(' incoming attack(s).')

                else:
                    orders_overview_list.append('\n\n- no orders -')


                villages_overview_text = ''.join(orders_overview_list)

                villages_paging_buttons = []

                if page > 1:
                    prev_all_button = Button.inline('⏮', bytes('villincattjump_1', encoding='utf-8'))
                    villages_paging_buttons.append(prev_all_button)
                    if page >= 6:
                        prev_5_button = Button.inline('⏪', bytes('villincattjump_' + str(int(page) - 5), encoding='utf-8'))
                        villages_paging_buttons.append(prev_5_button)
                    prev_1_button = Button.inline('◀️', bytes('villincattjump_' + str(int(page) - 1), encoding='utf-8'))
                    villages_paging_buttons.append(prev_1_button)

                if page < max_pages:
                    next_1_button = Button.inline('▶️', bytes('villincattjump_' + str(int(page) + 1), encoding='utf-8'))
                    villages_paging_buttons.append(next_1_button)

                    if (page + 5) <= max_pages:
                        next_5_button = Button.inline('⏩', bytes('villincattjump_' + str(int(page) + 5), encoding='utf-8'))
                        villages_paging_buttons.append(next_5_button)
                    next_all_button = Button.inline('⏭', bytes('villincattjump_' + str(max_pages), encoding='utf-8'))
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
        elif vill_atk_count == 0:
            await bot.send_message(entity=event.chat_id, message='You currently don\'t have incoming attacks. 🙂', parse_mode='html')