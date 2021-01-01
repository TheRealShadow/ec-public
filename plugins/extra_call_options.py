import logging

from telethon import events
from telethon.tl.custom import Button

from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(/help)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id),
                                               message=str('📣 Join @EmpireConquest for the latest news of the game.\n'
                                                           '\n'
                                                           '👥Searching for other players? Join the community chat @EmpireConquestCom\n'
                                                           '\n'
                                                           '🗣Want to report bugs, ideas or grammatical issues on the bot? Contact: @ECfbb_bot\n'
                                                           '\n'
                                                           '💰If you like our game, consider supporting us by a small donation /donate\n'
                                                           '\n'
                                                           '⚠Rules and such on /tos\n\nCurrent Game Settings: /game_information'), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/tos)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str('<b>Terms of service</b>\n'
                                                                                      '\n'
                                                                                      '<b>It\'s forbidden to:</b>\n'
                                                                                      '1. Automate your account by scripts.\n'
                                                                                      '2. Have multiple accounts.\n'
                                                                                      '3. Selling accounts or account values for real currencies.\n'
                                                                                      '4. Abuse bugs of any kind, without notifying the developers.\n'
                                                                                      '\n'
                                                                                      '<b>What userdata does this bot store?</b>\n'
                                                                                      '- Your Telegram - Username\n'
                                                                                      '- Your Telegram - ID\n'
                                                                                      '- Your Ingame Name\n'
                                                                                      '\n'
                                                                                      '<b>Note;</b> <i>This game is being developed by two hobby developers, where one is having an internship on front end development and the other is an IT support officer. If you consider updates too slow in the game, please consider playing another one.</i>'),
                                               parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/commands)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id),
                                               message=str('/rename_vil[ID] [NewVillageName] to rename your village\n'), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/donate)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str('<b>Thank you for considering a donation</b>\n'
                                                                                      '\n'
                                                                                      'Currently donations don\'t give ranks or special features, this might be added in the future.\n'
                                                                                      'if you want to donate click <a href=https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LK6PLMBFNNUMY&source=url>here</a>.\n'),
                                               parse_mode='html', link_preview=False, buttons=default_buttons)