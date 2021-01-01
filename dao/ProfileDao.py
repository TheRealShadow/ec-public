import datetime

from sqlalchemy import or_

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.troops import Troops
from models.marching import Marching
from models.support import Support
from models.recruitment import Recruitment
from models.structure_resource_production import Structure_Resource_Production
from models.settings import Settings

session = None


def init(global_session):
    global session
    session = global_session

def get_player_pk(tg_id):
    for found_id in session.query(Player.pk).filter(Player.tg_id==tg_id).first():
        if found_id:
            return found_id

def get_player_tg_id_by_pk(pk):
    for found_id in session.query(Player.tg_id).filter_by(pk=pk).first():
        if found_id:
            return found_id

def get_player_points(tg_id):
    for found_points in session.query(Player.points).filter_by(tg_id=tg_id).first():
        if found_points:
            return found_points

def get_player_points_by_pk(player_pk):
    for found_points in session.query(Player.points).filter_by(pk=player_pk).first():
        if found_points:
            return found_points

def player_village_points_by_pk(player_pk):
    for found_points in session.query(Player.avg_vil_point).filter_by(pk=player_pk).first():
        if found_points:
            return found_points

def get_player_name(tg_id):
    for found_player_name in session.query(Player.player_name).filter_by(tg_id=tg_id).first():
        if found_player_name:
            return found_player_name

def get_player_name_by_pk(player_pk):
    for found_player_name in session.query(Player.player_name).filter_by(pk=player_pk).first():
        if found_player_name:
            return found_player_name

def get_username_by_pk(player_pk):
    for found_player_name in session.query(Player.username).filter_by(pk=player_pk).first():
        if found_player_name:
            return found_player_name

def get_username_setting_by_pk(player_pk):
    for found_user_settings in session.query(Settings.show_username).filter_by(player_pk=player_pk).first():
        if found_user_settings:
            return found_user_settings

def get_downgrade_setting_by_pk(player_pk):
    for found_user_settings in session.query(Settings.show_downgrade).filter_by(player_pk=player_pk).first():
        if found_user_settings:
            return found_user_settings

def get_notify_setting_by_pk(player_pk):
    for found_user_settings in session.query(Settings.troop_return_notify).filter_by(player_pk=player_pk).first():
        if found_user_settings:
            return found_user_settings

def get_cur_village_name(tg_id):
    for selected_village in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for found_cur_village_name in session.query(Village.village_name).filter_by(pk=selected_village).first():
            if found_cur_village_name:
                return found_cur_village_name

def get_cur_village_id_by_pk(pk):
    for selected_village in session.query(Player.selected_village).filter_by(pk=pk):
        for found_cur_village_id in session.query(Village.pk).filter_by(pk=selected_village).first():
            if found_cur_village_id:
                return found_cur_village_id

def get_cur_village_id(tg_id):
    for selected_village in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for found_cur_village_id in session.query(Village.pk).filter_by(pk=selected_village).first():
            if found_cur_village_id:
                return found_cur_village_id

def get_cur_march_village_id(tg_id):
    for selected_village in session.query(Player.selected_march_village).filter_by(tg_id=tg_id).first():
        if selected_village == None:
            return None
        for found_cur_village_id in session.query(Village.pk).filter_by(pk=selected_village).first():
            if found_cur_village_id:
                return found_cur_village_id

def get_village_owner(tg_id):
    for owner in session.query(Player.pk).filter_by(tg_id=tg_id):
        if owner:
            return owner

def get_structure_points_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for points_base in session.query(Structure.structure_base_points).filter_by(structure_name=structure).first():
            if points_base:
                return points_base


def get_structure_points_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for points_factor in session.query(Structure.structure_points_factor).filter_by(
                structure_name=structure).first():
            if points_factor:
                return points_factor


def get_population_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_base in session.query(Structure.structure_base_population_cost).filter_by(
                structure_name=structure).first():
            if pop_base:
                return pop_base


def get_population_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_factor in session.query(Structure.structure_population_factor).filter_by(
                structure_name=structure).first():
            if pop_factor:
                return pop_factor