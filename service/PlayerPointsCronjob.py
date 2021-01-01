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
    aiocron.crontab('*/19 * * * *', func=set_points_to_players)

def set_points_to_players():
    owner_pks = villagedao.get_all_player_pk()
    for owner_pk in owner_pks:
        village_ids = villagedao.get_all_village_id_of_player(owner_pk)
        points = 0
        if village_ids != None:
            for village_id in village_ids:
                village_points = prof.get_village_overview_points(village_id)
                points = points + village_points
                set_points = session.query(Player).filter_by(pk=owner_pk).first()
                set_points.points = points
                session.add(set_points)
                session.commit()