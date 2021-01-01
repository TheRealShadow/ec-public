import re
import logging
import itertools

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
    @bot.on(events.NewMessage(incoming=True, pattern=r"(/reclaim)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        reclaim = vill.reclaim_a_village(from_id, session)
                        await bot.send_message(entity=event.chat_id, message=reclaim, parse_mode='html')