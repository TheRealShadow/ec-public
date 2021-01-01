import logging

from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as tro, ResearchService as res

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🔬Research)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if auth.village_owner_from_selected_village(from_id) is True:
                            default_buttons = buttons.get_recruitment_keyboard()
                            research_menu = res.generate_research_overview(from_id)
                            await bot.send_message(entity=event.chat_id,
                                             message=str(
                                             research_menu)
                                             , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏰Nobles)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if auth.village_owner_from_selected_village(from_id) is True:
                            default_buttons = buttons.get_noble_keyboard()
                            noble_menu = res.noble_unit(from_id)
                            await bot.send_message(entity=event.chat_id,
                                                   message=str(
                                                       noble_menu)
                                                   , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/research_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        fetch_response = res.research_unit(from_id, unit_pk, session)
                        default_buttons = buttons.get_recruitment_keyboard()
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   fetch_response)
                                               , parse_mode='html', buttons=default_buttons)