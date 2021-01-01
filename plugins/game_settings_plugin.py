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
    @bot.on(events.NewMessage(incoming=True, pattern=r"(/game_information)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        message = '<b>Empire Conquest - Version 1.2.7 Stone age.</b>\n' \
                                  '<b>Building_point_setting:</b> 1.0\n' \
                                  '<b>Building_resource_demand:</b> 1.2\n' \
                                  '<b>Building_population_demand:</b> 1.2\n' \
                                  '<b>Unit_recruitment_speed:</b> 1.0\n' \
                                  '<b>Unit_resource_demand:</b> 1.0\n' \
                                  '<b>Unit_population_demand:</b> 1.0\n' \
                                  '<b>Unit_movement_speed:</b> 1.0\n' \
                                  '<b>Starting_villages:</b> 1.0\n' \
                                  '<b>Barbarian_villages_growth:</b> Disabled\n' \
                                  '<b>Barbarian_villages_start:</b>\n<b>0:</b> ⚔🏹🐎💣 🏰⚒⚖️🧱\n<b>1:</b>🏛⛲🌾\n<b>25:</b>📦🪓⛏📏\n<b>Research:</b> Spear, Scout\n' \
                                  '<b>Resource_production_speed:</b> 1.0\n' \
                                  '<b>Noble_System:</b> Pouches\n' \
                                  '\n' \
                                  '<b>Game refresh timer settings:</b>\n' \
                                  'Toplists_refresh_timer: 1 hour\n' \
                                  'Resource_giving_refresh_timer: 15 minutes\n' \
                                  'Unit_recruit_refresh_timer: 1 minute\n' \
                                  'Trading_check_timer: 1 minute\n' \
                                  'Marching_check_timer: 1 minute\n' \
                                  'Loyalty_plus_one_timer: 30 minutes\n' \
                                  'Bot_restart: 23:59 UTC\n' \
                                  '\n' \
                                  'Feedback bot: @ECfbb_bot\n' \
                                  'Community chat: @EmpireConquestCom\n' \
                                  'News channel: @EmpireConquest'
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(message), parse_mode='html', buttons=default_buttons)