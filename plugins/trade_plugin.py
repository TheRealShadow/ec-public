import datetime
import logging
import re

from sqlalchemy import func, distinct
from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from dao import TraderDao as traderdao
from models.player import Player
from models.village import Village
from models.building import Building
from models.trading import Trading
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r'/pve_trade (.*) (.*) (.*)'))
    async def handler(event):
        give_resource = event.pattern_match.group(1)
        give_amount = event.pattern_match.group(2)
        receive_resource = event.pattern_match.group(3)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if give_resource and give_amount and receive_resource:
                            resource_trade = traderdao.pve_trader(from_id, give_resource, give_amount, receive_resource, session)
                            await bot.send_message(entity=event.chat_id,
                                                   message=str(resource_trade)
                                                   , parse_mode='html')


    @bot.on(events.NewMessage(incoming=True, pattern=r'/pve_trader'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        market_level = villagedao.get_structure_level(from_id, 'market')
                        if market_level >= 5:
                            await bot.send_message(entity=event.chat_id,
                                                   message='Welcome to my shop!\nHere you can trade your resources with mine!\nI\'m not the cheapest, but I\'m the fastest around here!\nMy price is that I give 1 resource back for 2 resources I receive!\n\nto trade use:\n/pve_trade <code>GivingResourceType amount ReceivingResourceType</code>'
                                                   , parse_mode='html')
                        elif market_level < 5 or market_level is None:
                            if market_level is None:
                                market_level=0
                            await bot.send_message(entity=event.chat_id,
                                                   message='Welcome to my shop!\nHere you can trade your resources with mine!\nBut hold on, your market is only level ' + str(market_level) + '?\nSeems like I\'m spilling my time here, get back once it\'s level 5!'
                                                   , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/trade_(\d+)( (.*) (.*))?'))
    async def handler(event):
        towards_village = event.pattern_match.group(1)
        give_resource = event.pattern_match.group(3)
        give_amount = event.pattern_match.group(4)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if towards_village and give_resource and give_amount:
                            trading = traderdao.set_trade_now(from_id, towards_village, give_resource, give_amount, session)
                            await bot.send_message(entity=event.chat_id,
                                                   message=str(trading)
                                                   , parse_mode='html')
                        else:
                            await bot.send_message(entity=event.chat_id,
                                                   message='<b>To send resources:</b>\n'
                                                           '/trade_id resource amount\n'
                                                           '\n'
                                                           'resource types: wood, stone, iron\n'
                                                           'example: /trade_0 wood 10000'
                                                   , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/trades'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        player_pk = prof.cur_player_id(from_id)
                        await create_trades_overview(1, event, True, session, player_pk, bot)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"tradejump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_trades_overview(int(page), event, False, session, player_pk, bot)

async def create_trades_overview(page, event, send_new, session, player_pk, bot):
    page_size = 10

    offset = ((int(page) - 1) * page_size)
    trade_count = session.query(func.count(Trading.arrival_time)).filter(Trading.owner==player_pk).order_by(Trading.arrival_time.asc()).scalar()
    if trade_count > 0:
        max_pages = (trade_count // page_size)
        if (trade_count % page_size) > 0:
            max_pages += 1
        if page <= max_pages:
            trades = session.query(Trading).filter(Trading.owner==player_pk).order_by(Trading.arrival_time.asc()).limit(page_size).offset(offset).all()
            trades_overview_list = ['<b>Your 🎭Trades:</b>\n']
            if trades:
                for trade in trades:
                    time_left = str(trade.arrival_time - datetime.datetime.utcnow()).split(".")[0]
                    if '-1 day,' in time_left:
                        time_left = 'Soon™️'
                    trades_overview_list.append(str(trade.arrival_time))
                    trades_overview_list.append(' | ')
                    trades_overview_list.append(str(time_left))
                    trades_overview_list.append('\n')
                    if trade.wood == 0:
                        trades_overview_list.append('')
                    if trade.wood >= 1:
                        trades_overview_list.append('🪓' + str(trade.wood))
                    if trade.stone == 0:
                        trades_overview_list.append('')
                    if trade.stone >= 1:
                        trades_overview_list.append('⛏' + str(trade.stone))
                    if trade.iron == 0:
                        trades_overview_list.append('')
                    if trade.iron >= 1:
                        trades_overview_list.append('📏' + str(trade.iron))
                    if trade.type_trade == 'GOING_TO':
                        trades_overview_list.append(' going to ')
                    if trade.type_trade == 'COMING_BACK':
                        trades_overview_list.append(' returning from ')
                    trades_overview_list.append(villagedao.get_village_name_by_pk(trade.to_village_id))
                    trades_overview_list.append(' /view_vil')
                    trades_overview_list.append(str(trade.to_village_id))
                    trades_overview_list.append('\n\n')

                trades_overview_list.append('Showing ')
                trades_overview_list.append(str(offset + 1))
                trades_overview_list.append(' to ')
                trades_overview_list.append(str(offset + len(trades)))
                trades_overview_list.append(' from ')
                trades_overview_list.append(str(trade_count))
                trades_overview_list.append(' trade(s).')

            else:
                trades_overview_list.append('\n\n- no trades -')



            trades_overview_text = ''.join(trades_overview_list)

            trades_paging_buttons = []

            if page > 1:
                prev_all_button = Button.inline('⏮', bytes('tradejump_1', encoding='utf-8'))
                trades_paging_buttons.append(prev_all_button)
                if page >= 6:
                    prev_5_button = Button.inline('⏪', bytes('tradejump_' + str(int(page) - 5), encoding='utf-8'))
                    trades_paging_buttons.append(prev_5_button)
                prev_1_button = Button.inline('◀️', bytes('tradejump_' + str(int(page) - 1), encoding='utf-8'))
                trades_paging_buttons.append(prev_1_button)

            if page < max_pages:
                next_1_button = Button.inline('▶️', bytes('tradejump_' + str(int(page) + 1), encoding='utf-8'))
                trades_paging_buttons.append(next_1_button)

                if (page + 5) <= max_pages:
                    next_5_button = Button.inline('⏩', bytes('tradejump_' + str(int(page) + 5), encoding='utf-8'))
                    trades_paging_buttons.append(next_5_button)
                next_all_button = Button.inline('⏭', bytes('tradejump_' + str(max_pages), encoding='utf-8'))
                trades_paging_buttons.append(next_all_button)

            if send_new:
                if len(trades_paging_buttons) > 0:
                    await bot.send_message(entity=event.chat_id, message=trades_overview_text, buttons=trades_paging_buttons, parse_mode='html')
                else:
                    await bot.send_message(entity=event.chat_id, message=trades_overview_text, parse_mode='html')
            else:
                if len(trades_paging_buttons) > 0:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=trades_overview_text, buttons=trades_paging_buttons, parse_mode='html')
                else:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=trades_overview_text, parse_mode='html')
    elif trade_count == 0:
        await bot.send_message(entity=event.chat_id, message='You don\'t have any trades at the moment.', parse_mode='html')