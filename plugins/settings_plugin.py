import logging

from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as tro

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(⚙Settings)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        fetch_player_settings = prof.fetch_player_settings(from_id)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(fetch_player_settings), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/enable_name|/disable_name)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    raw_message = message.raw_text
                    if auth.is_registered(from_id) is True:
                        set_name = prof.set_player_telegram_name_by_pk(from_id, raw_message, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(set_name), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/enable_downgrade|/disable_downgrade)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    raw_message = message.raw_text
                    if auth.is_registered(from_id) is True:
                        set_name = prof.set_player_downgrade_option_by_pk(from_id, raw_message, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(set_name), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/enable_notify|/disable_notify)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    raw_message = message.raw_text
                    if auth.is_registered(from_id) is True:
                        set_name = prof.set_disable_notify_option_by_pk(from_id, raw_message, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(set_name), parse_mode='html', buttons=default_buttons)