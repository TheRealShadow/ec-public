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
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as troo, WarService as war

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r'/withdraw_(\d+)(@.*)?'))
    async def handler(event):
        report_id = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        check_troops_owner = auth.check_support_owner(from_id, report_id, session)
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   check_troops_owner)
                                               , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/(attack|support)_(\d+)(@.*)?'))
    async def handler(event):
        selected_village = event.pattern_match.group(2)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        chosen_village = vill.selecting_another_marching_village(from_id, selected_village)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   chosen_village)
                                               , parse_mode='html')



    @bot.on(events.NewMessage(incoming=True, pattern=r'/add_(\d+)( (.*))?'))
    async def handler(event):
        unit = event.pattern_match.group(1)
        amount = event.pattern_match.group(3)
        if not amount:
            amount = 1
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        added_units = war.add_unit_to_march(from_id, int(unit), int(amount), session)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   added_units)
                                               , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/all_(\d+)?'))
    async def handler(event):
        unit = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        added_units = war.all_unit_to_march(from_id, int(unit), session)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   added_units)
                                               , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/add_all'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        added_units = war.add_all_units_to_march(from_id, session)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   added_units)
                                               , parse_mode='html')



    @bot.on(events.NewMessage(incoming=True, pattern=r'/rem_(\d+)( (.*))?'))
    async def handler(event):
        unit = event.pattern_match.group(1)
        amount = event.pattern_match.group(3)
        if not amount:
            amount = 1
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        added_units = war.rem_unit_to_march(from_id, int(unit), int(amount), session)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   added_units)
                                               , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/reset'))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        added_units = war.rem_all_unit_to_march(from_id, session)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   added_units)
                                               , parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/send_([a-zA-Z]+)'))
    async def handler(event):
        march_type = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        march_send = await war.send_units_marching(from_id, march_type, session, bot)
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   march_send)
                                               , parse_mode='html')