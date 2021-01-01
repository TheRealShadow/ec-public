from decimal import Decimal
import re

import aiocron
from dao import VillageDao as villagedao
from dao import RecruitmentDao as recruitmentdao
from models.player import Player
from models.village import Village
from models.troops import Troops
from service import ProfileService as prof

session = None

def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/15 * * * *', func=set_villages_to_players)

def set_villages_to_players():
    owner_pks = villagedao.get_all_player_pk()
    for owner_pk in owner_pks:
        count = villagedao.count_user_villages_by_pk(owner_pk)
        if count == None:
            count = 0
        set_villages = session.query(Player).filter_by(pk=owner_pk).first()
        set_villages.villages = count
        session.add(set_villages)
        session.commit()