import logging
from logging.handlers import TimedRotatingFileHandler
from telethon import TelegramClient
import multiprocessing

from service import ConfigService as conf

conf.init()

from models.basemodel import Session
from dao import UserDao as userdao
from dao import ProfileDao as profiledao
from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import MapGenDao as mapgendao
from dao import RecruitmentDao as recruitmentdao
from dao import UnitDao as unitdao
from dao import ResearchDao as researchdao
from dao import  WarDao as wardao
from service import ResourceCalculationPlugin, LoyaltyPlugin, RecruitmentCronjob, PlayerPointsCronjob, TraderCronjob, VillageToplistCronjob, WarCronjob, PlayerDefeatedCronjob, VillageAvgPointCronjob

# Use your own values from my.telegram.org
api_id = conf.get_int('API', 'api_id')
api_hash = conf.get_string('API', 'api_hash')
bot_token = conf.get_string('API', 'bot_token')

# Manual call line to sign in as a bot.
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
bot.flood_sleep_threshold = 0

logger = logging.getLogger()  # Gets the root logger
logger.setLevel(logging.INFO)
logdumps = TimedRotatingFileHandler('logs/console.log', when="midnight", interval=1, backupCount=5)
formatter = logging.Formatter('%(levelname)s [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s', '%H:%M:%S')
logger.addHandler(logdumps)

dialogs = bot.get_dialogs()

session = Session()
userdao.init(session)
profiledao.init(session)
villagedao.init(session)
buildingdao.init(session)
mapgendao.init(session)
recruitmentdao.init(session)
unitdao.init(session)
researchdao.init(session)
wardao.init(session)

# ResourceCalculationPlugin.init(session)
# LoyaltyPlugin.init(session)
# RecruitmentCronjob.init(session)
# PlayerPointsCronjob.init(session)
# PlayerDefeatedCronjob.init(session)
# TraderCronjob.init(session)
# VillageToplistCronjob.init(session)
# WarCronjob.init(session)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=ResourceCalculationPlugin.init(session))
    p2 = multiprocessing.Process(target=LoyaltyPlugin.init(session))
    p3 = multiprocessing.Process(target=RecruitmentCronjob.init(session))
    p4 = multiprocessing.Process(target=PlayerPointsCronjob.init(session))
    p5 = multiprocessing.Process(target=PlayerDefeatedCronjob.init(session))
    p6 = multiprocessing.Process(target=TraderCronjob.init(session))
    p7 = multiprocessing.Process(target=VillageToplistCronjob.init(session))
    p8 = multiprocessing.Process(target=WarCronjob.init(session))

    p1.start()


try:
    # Standalone script __init__.py with folder plugins/
    import plugins

    plugins.init(bot, session)
except ImportError:
    try:
        from . import plugins

        plugins.init(bot, session)
    except ImportError:
        plugins = None
try:
    bot.run_until_disconnected()
finally:
    bot.disconnect()
