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
    @bot.on(events.NewMessage)
    async def check_user_id_handler(event):
        message = event.message
        if message:
            sender = message.sender
            if sender:
                from_id = sender.id
                username = sender.username
                if auth.is_registered(from_id) is True:
                    update_username = session.query(Player).filter(Player.tg_id==from_id).first()
                    if username != update_username.username:
                        update_username.username = username
                        session.add(update_username)
                        session.commit()