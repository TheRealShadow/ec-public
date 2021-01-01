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
    aiocron.crontab('*/20 * * * *', func=set_defeated_to_players)

def set_defeated_to_players():
    player_pks = villagedao.get_all_player_pk()
    for player_pk in player_pks:
        add_opponents = session.query(Player).filter(Player.pk==player_pk).first()
        add_opponents.total_defeated_units = add_opponents.defeated_units_defense + add_opponents.defeated_units_attack
        session.add(add_opponents)
        session.commit()