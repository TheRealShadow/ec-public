import re
import logging
import itertools

from telethon import events
from telethon.tl.custom import Button

from models.player import Player
from models.village import Village
from models.building import Building
from models.research import Research
from models.troops import Troops
from models.settings import Settings
from dao import MapGenDao as mapgendao
from service import AuthenticationService as auth, ButtonService as buttons

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🎪Alliance)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str('Not implemented yet\n'
                                                                                      'Currently working on <i>something</i>'), parse_mode='html'
                        , buttons=default_buttons)