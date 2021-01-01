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

bot_global = None

async def init(bot, session):
    global bot_global
    bot_global = bot

async def notify_possible_reciever(tgid, message, session):
        if tgid:
            if message:
                await bot_global.send_message(entity=int(tgid), message=message, parse_mode='html')
