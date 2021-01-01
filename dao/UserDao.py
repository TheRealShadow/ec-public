import datetime

from sqlalchemy import or_

from models.player import Player
from models.village import Village
from models.building import Building
from models.reports import Reports
from models.support import Support
from dao import ProfileDao as prof

session = None


def init(global_session):
    global session
    session = global_session


def get_player_by_player_id(tg_id):
    found_player = session.query(Player).filter(Player.tg_id == tg_id).first()
    if found_player:
        return found_player


def get_player_name(player_name):
    found_player_name = session.query(Player).filter(Player.player_name == player_name).first()
    if found_player_name:
        return found_player_name


def get_owner_id(village_owner):
    found_village_owner = session.query(Player).filter(Village.owner == village_owner).first()
    if found_village_owner:
        return found_village_owner


def get_building_current_row(current_village):
    found_row = session.query(Building).filter_by(village_pk=current_village).first()
    if found_row:
        return found_row


def get_village_current_row(current_village):
    found_row = session.query(Village).filter_by(pk=current_village).first()
    if found_row:
        return found_row


def owner_check(tg_id):
    village_pk = session.query(Player.selected_village).filter_by(tg_id=tg_id).first()
    owner_pk = session.query(Player.pk).filter_by(tg_id=tg_id).first()
    village_by_pk = session.query(Village.pk).filter_by(pk=village_pk).first()
    village_by_owner_pk = session.query(Village.owner_pk).filter_by(pk=village_pk).first()
    if village_pk == village_by_pk and owner_pk == village_by_owner_pk:
        return True
    else:
        return False

def report_owner_check(tg_id, report_id):
    owner_pk = session.query(Player.pk).filter_by(tg_id=tg_id).first()
    report_owner = session.query(Reports.owner).filter_by(pk=report_id).first()
    if owner_pk == report_owner:
        return True
    else:
        return False

def support_owner_check(tg_id, support_id):
    owner_pk = session.query(Player.pk).filter_by(tg_id=tg_id).first()
    report_owner = session.query(Support.owner).filter_by(pk=support_id).first()
    if owner_pk == report_owner:
        return True
    else:
        return False