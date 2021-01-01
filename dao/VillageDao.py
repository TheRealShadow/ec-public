import datetime

from sqlalchemy import or_, func

from dao.RecruitmentDao import get_end_time_of_query_for_unit
from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.troops import Troops
from models.recruitment import Recruitment
from models.structure_resource_production import Structure_Resource_Production
from service import ProfileService as prof, WarService as war
from dao import RecruitmentDao as recruitmentdao
from dao import WarDao as wardao

session = None


def init(global_session):
    global session
    session = global_session


def get_structure_max_level(structure):
    if structure == 'headquarters':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'barracks':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'archery':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'stable':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'siege workshop':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'castle':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'smithy':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'rally point':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'market':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'woodcutter':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'stone mine':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'iron mine':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'farm':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'storage':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level
    elif structure == 'wall':
        for structure_max_level in session.query(Structure.structure_max_level).filter_by(
                structure_name=structure).first():
            if structure_max_level:
                return structure_max_level


def get_structure_min_level(structure):
    if structure == 'headquarters':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level is None:
                structure_min_level = 0
                return structure_min_level
    elif structure == 'barracks':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level is None:
                structure_min_level = 0
                return structure_min_level
    elif structure == 'archery':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'stable':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'siege workshop':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'castle':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'smithy':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'rally point':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'market':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'woodcutter':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'stone mine':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'iron mine':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'farm':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'storage':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level
    elif structure == 'wall':
        for structure_min_level in session.query(Structure.structure_min_level).filter_by(
                structure_name=structure).first():
            if structure_min_level:
                return structure_min_level


def get_structure_name(structure):
    if structure == 'headquarters':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'barracks':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'archery':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'stable':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'siege workshop':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'castle':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'smithy':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'rally point':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'market':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'woodcutter':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'stone mine':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'iron mine':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'farm':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'storage':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name
    elif structure == 'wall':
        for structure_name in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
            if structure_name:
                return structure_name


def get_structure_level(tg_id, structure):
    if structure == 'headquarters':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for headquarter_level in session.query(Building.headquarter_level).filter_by(
                        village_pk=village_id).first():
                    if headquarter_level:
                        return headquarter_level
    elif structure == 'barracks':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for barrack_level in session.query(Building.barrack_level).filter_by(village_pk=village_id).first():
                    if barrack_level:
                        return barrack_level
    elif structure == 'archery':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for archery_level in session.query(Building.archery_level).filter_by(village_pk=village_id).first():
                    if archery_level:
                        return archery_level
    elif structure == 'stable':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for stable_level in session.query(Building.stable_level).filter_by(village_pk=village_id).first():
                    if stable_level:
                        return stable_level
    elif structure == 'siege workshop':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for siege_workshop_level in session.query(Building.siege_workshop_level).filter_by(
                        village_pk=village_id).first():
                    if siege_workshop_level:
                        return siege_workshop_level
    elif structure == 'castle':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for castle_level in session.query(Building.castle_level).filter_by(village_pk=village_id).first():
                    if castle_level:
                        return castle_level
    elif structure == 'smithy':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for smithy_level in session.query(Building.smithy_level).filter_by(village_pk=village_id).first():
                    if smithy_level:
                        return smithy_level
    elif structure == 'rally point':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for rally_point_level in session.query(Building.rally_point_level).filter_by(
                        village_pk=village_id).first():
                    if rally_point_level:
                        return rally_point_level
    elif structure == 'market':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for market_level in session.query(Building.market_level).filter_by(village_pk=village_id).first():
                    if market_level == None:
                        market_level = 0
                        return market_level
                    elif market_level >= 0:
                        return market_level
    elif structure == 'woodcutter':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for woodcutter_level in session.query(Building.woodcutter_level).filter_by(
                        village_pk=village_id).first():
                    if woodcutter_level:
                        return woodcutter_level
    elif structure == 'stone mine':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for stone_mine_level in session.query(Building.stone_mine_level).filter_by(
                        village_pk=village_id).first():
                    if stone_mine_level:
                        return stone_mine_level
    elif structure == 'iron mine':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for iron_mine_level in session.query(Building.iron_mine_level).filter_by(village_pk=village_id).first():
                    if iron_mine_level:
                        return iron_mine_level
    elif structure == 'farm':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for farm_level in session.query(Building.farm_level).filter_by(village_pk=village_id).first():
                    if farm_level:
                        return farm_level
    elif structure == 'storage':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for storage_level in session.query(Building.storage_level).filter_by(village_pk=village_id).first():
                    if storage_level:
                        return storage_level
    elif structure == 'wall':
        for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
            for village_id in session.query(Village.pk).filter_by(pk=village_pk):
                for wall_level in session.query(Building.wall_level).filter_by(village_pk=village_id).first():
                    if wall_level:
                        return wall_level

def get_structure_overview_level(village_pk, structure):
    if structure == 'headquarters':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for headquarter_level in session.query(Building.headquarter_level).filter_by(
                    village_pk=village_id).first():
                if headquarter_level:
                    return headquarter_level
    elif structure == 'barracks':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for barrack_level in session.query(Building.barrack_level).filter_by(village_pk=village_id).first():
                if barrack_level:
                    return barrack_level
    elif structure == 'archery':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for archery_level in session.query(Building.archery_level).filter_by(village_pk=village_id).first():
                if archery_level:
                    return archery_level
    elif structure == 'stable':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for stable_level in session.query(Building.stable_level).filter_by(village_pk=village_id).first():
                if stable_level:
                    return stable_level
    elif structure == 'siege workshop':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for siege_workshop_level in session.query(Building.siege_workshop_level).filter_by(
                    village_pk=village_id).first():
                if siege_workshop_level:
                    return siege_workshop_level
    elif structure == 'castle':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for castle_level in session.query(Building.castle_level).filter_by(village_pk=village_id).first():
                if castle_level:
                    return castle_level
    elif structure == 'smithy':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for smithy_level in session.query(Building.smithy_level).filter_by(village_pk=village_id).first():
                if smithy_level:
                    return smithy_level
    elif structure == 'rally point':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for rally_point_level in session.query(Building.rally_point_level).filter_by(
                    village_pk=village_id).first():
                if rally_point_level:
                    return rally_point_level
    elif structure == 'market':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for market_level in session.query(Building.market_level).filter_by(village_pk=village_id).first():
                if market_level:
                    return market_level
    elif structure == 'woodcutter':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for woodcutter_level in session.query(Building.woodcutter_level).filter_by(
                    village_pk=village_id).first():
                if woodcutter_level:
                    return woodcutter_level
    elif structure == 'stone mine':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for stone_mine_level in session.query(Building.stone_mine_level).filter_by(
                    village_pk=village_id).first():
                if stone_mine_level:
                    return stone_mine_level
    elif structure == 'iron mine':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for iron_mine_level in session.query(Building.iron_mine_level).filter_by(village_pk=village_id).first():
                if iron_mine_level:
                    return iron_mine_level
    elif structure == 'farm':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for farm_level in session.query(Building.farm_level).filter_by(village_pk=village_id).first():
                if farm_level:
                    return farm_level
    elif structure == 'storage':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for storage_level in session.query(Building.storage_level).filter_by(village_pk=village_id).first():
                if storage_level:
                    return storage_level
    elif structure == 'wall':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for wall_level in session.query(Building.wall_level).filter_by(village_pk=village_id).first():
                if wall_level:
                    return wall_level

def get_wood_storage(tg_id):
    for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for current_wood in session.query(Village.wood_stock).filter_by(pk=village_pk).first():
            if current_wood:
                return current_wood


def get_stone_storage(tg_id):
    for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for current_stone in session.query(Village.stone_stock).filter_by(pk=village_pk).first():
            if current_stone:
                return current_stone


def get_iron_storage(tg_id):
    for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for current_iron in session.query(Village.iron_stock).filter_by(pk=village_pk).first():
            if current_iron:
                return current_iron

def get_wood_storage_by_pk(village_pk):
    for current_wood in session.query(Village.wood_stock).filter_by(pk=village_pk).first():
        if current_wood:
            return current_wood


def get_stone_storage_by_pk(village_pk):
    for current_stone in session.query(Village.stone_stock).filter_by(pk=village_pk).first():
        if current_stone:
            return current_stone


def get_iron_storage_by_pk(village_pk):
    for current_iron in session.query(Village.iron_stock).filter_by(pk=village_pk).first():
        if current_iron:
            return current_iron

def get_population_base():
    structure = 'farm'
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_base in session.query(Structure_Resource_Production.base_population_production).filter_by(
                name=structure).first():
            if pop_base:
                return pop_base


def get_population_factor():
    structure = 'farm'
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_factor in session.query(Structure_Resource_Production.population_factor).filter_by(
                name=structure).first():
            if pop_factor:
                return pop_factor


def get_capacity_base():
    structure = 'storage'
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for cap_base in session.query(Structure_Resource_Production.base_capacity).filter_by(name=structure).first():
            if cap_base:
                return cap_base


def get_capacity_factor():
    structure = 'storage'
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for cap_factor in session.query(Structure_Resource_Production.capacity_factor).filter_by(
                name=structure).first():
            if cap_factor:
                return cap_factor


def get_production_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pro_base in session.query(Structure_Resource_Production.base_production_production).filter_by(
                name=structure).first():
            if pro_base:
                return pro_base


def get_production_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pro_factor in session.query(Structure_Resource_Production.production_factor).filter_by(
                name=structure).first():
            if pro_factor:
                return pro_factor


def get_loyalty(tg_id):
    for village_pk in session.query(Player.selected_village).filter_by(tg_id=tg_id):
        for current_loyalty in session.query(Village.loyalty).filter_by(pk=village_pk).first():
            if current_loyalty:
                return current_loyalty

def get_loyalty_overview(village_pk):
    for current_loyalty in session.query(Village.loyalty).filter_by(pk=village_pk).first():
        if current_loyalty:
            return current_loyalty

def get_village_loyalty(village_pk):
    for current_loyalty in session.query(Village.loyalty).filter_by(pk=village_pk).first():
        if current_loyalty:
            return current_loyalty

def count_user_villages(tg_id):
    owner_id = prof.cur_player_id(tg_id)
    villages = len(session.query(Village).filter(Village.owner_pk==owner_id).all())
    if villages:
        return villages

def user_villages_by_player_database_player_pk(owner_pk):
    for villages in session.query(Player.villages).filter_by(pk=owner_pk).first():
        if villages:
            return villages

def count_user_villages_by_pk(player_pk):
    villages = len(session.query(Village).filter(Village.owner_pk==player_pk).all())
    if villages:
        return villages

def get_resource_village_level(village_pk, structure):
    if structure == 'woodcutter':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for woodcutter_level in session.query(Building.woodcutter_level).filter_by(village_pk=village_id).first():
                if woodcutter_level:
                    return woodcutter_level
    elif structure == 'stone mine':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for stone_mine_level in session.query(Building.stone_mine_level).filter_by(village_pk=village_id).first():
                if stone_mine_level:
                    return stone_mine_level
    elif structure == 'iron mine':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for iron_mine_level in session.query(Building.iron_mine_level).filter_by(village_pk=village_id).first():
                if iron_mine_level:
                    return iron_mine_level
    elif structure == 'storage':
        for village_id in session.query(Village.pk).filter_by(pk=village_pk):
            for storage_level in session.query(Building.storage_level).filter_by(village_pk=village_id).first():
                if storage_level:
                    return storage_level

def get_all_player_pk():
    player_ids = session.query(Player.pk).all()
    if player_ids:
        return player_ids

def get_all_village_id():
    village_ids = session.query(Village.pk).all()
    if village_ids:
        return village_ids

def get_all_village_id_of_player(owner_id):
    village_ids = session.query(Village.pk).filter_by(owner_pk=owner_id).all()
    if village_ids:
        return village_ids


def get_selected_village_id(value):
    village_ids = session.query(Village.pk).filter_by(pk=value).all()
    if village_ids:
        return village_ids


def get_upgrade_requirement(tg_id, structure):
    if structure == 'headquarters':
        return_message = 1
        return return_message
    elif structure == 'rally point':
        return_message = 1
        return return_message
    elif structure == 'woodcutter':
        return_message = 1
        return return_message
    elif structure == 'stone mine':
        return_message = 1
        return return_message
    elif structure == 'iron mine':
        return_message = 1
        return return_message
    elif structure == 'farm':
        return_message = 1
        return return_message
    elif structure == 'storage':
        return_message = 1
        return return_message
    elif structure == 'barracks':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one >= 3:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'archery':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 2
            return return_message
        elif check_building_one >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'stable':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 2
            return return_message
        elif check_building_one >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'siege workshop':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = 2
            return return_message
        elif check_building_one >= 10 and check_building_two >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'castle':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'smithy'
        check_building_two = get_structure_level(tg_id, check_building_two)
        check_building_three = 'market'
        check_building_three = get_structure_level(tg_id, check_building_three)
        if check_building_one is None or check_building_two is None or check_building_three is None:
            return_message = 2
            return return_message
        elif check_building_one >= 20 and check_building_two == 20 and check_building_three >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'smithy':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = 2
            return return_message
        elif check_building_one >= 10 and check_building_two >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'market':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 2
            return return_message
        elif check_building_one >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message
    elif structure == 'wall':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 2
            return return_message
        elif check_building_one >= 3:
            return_message = 1
            return return_message
        else:
            return_message = 2
            return return_message


def get_upgrade_requirement_reply(tg_id, structure):
    if structure == 'headquarters':
        return_message = 1
        return return_message
    elif structure == 'rally point':
        return_message = 1
        return return_message
    elif structure == 'woodcutter':
        return_message = 1
        return return_message
    elif structure == 'stone mine':
        return_message = 1
        return return_message
    elif structure == 'iron mine':
        return_message = 1
        return return_message
    elif structure == 'farm':
        return_message = 1
        return return_message
    elif structure == 'storage':
        return_message = 1
        return return_message
    elif structure == 'barracks':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one >= 3:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have 🏛Headquarters at least level 3 to build this!'
            return return_message
    elif structure == 'archery':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 'You need to have ⚔barracks level 5 to build this!'
            return return_message
        elif check_building_one >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have ⚔barracks level 5 to build this!'
            return return_message
    elif structure == 'stable':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 'You need to have ⚔barracks level 5 to build this!'
            return return_message
        elif check_building_one >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have ⚔barracks level 5 to build this!'
            return return_message
    elif structure == 'siege workshop':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = 'You need to have 🏛Headquarters level 10 and ⚔barracks level 10 to build this!'
            return return_message
        elif check_building_one >= 10 and check_building_two >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have 🏛Headquarters level 10 and ⚔barracks level 10 to build this!'
            return return_message
    elif structure == 'castle':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'smithy'
        check_building_two = get_structure_level(tg_id, check_building_two)
        check_building_three = 'market'
        check_building_three = get_structure_level(tg_id, check_building_three)
        if check_building_one is None or check_building_two is None:
            return_message = 'You need to have 🏛Headquarters level 20, ⚒smithy level 20 and ⚖️market level 10 to build this!'
            return return_message
        elif check_building_one >= 20 and check_building_two == 20 and check_building_three >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have 🏛Headquarters level 20, ⚒smithy level 20 and ⚖market level 10 to build this!'
            return return_message
    elif structure == 'smithy':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = 'You need to have 🏛Headquarters level 10, ⚔barracks level 5 to build this!'
            return return_message
        elif check_building_one >= 10 and check_building_two >= 5:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have 🏛Headquarters level 10, ⚔barracks level 5 to build this!'
            return return_message
    elif structure == 'market':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 'You need to have 🏛Headquarters level 10 to build this!'
            return return_message
        elif check_building_one >= 10:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have 🏛Headquarters level 10 to build this!'
            return return_message
    elif structure == 'wall':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = 'You need to have ⚔barracks level 3 to build this!'
            return return_message
        elif check_building_one >= 3:
            return_message = 1
            return return_message
        else:
            return_message = 'You need to have ⚔barracks level 3 to build this!'
            return return_message


def get_upgrade_requirement_overview(tg_id, structure):
    if structure == 'headquarters':
        return_message = ''
        return return_message
    if structure == 'rally point':
        return_message = ''
        return return_message
    if structure == 'woodcutter':
        return_message = ''
        return return_message
    if structure == 'stone mine':
        return_message = ''
        return return_message
    if structure == 'iron mine':
        return_message = ''
        return return_message
    if structure == 'farm':
        return_message = ''
        return return_message
    if structure == 'storage':
        return_message = ''
        return return_message
    if structure == 'barracks':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one >= 3:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'archery':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = ' 🔒'
            return return_message
        elif check_building_one >= 5:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'stable':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = ' 🔒'
            return return_message
        elif check_building_one >= 5:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'siege workshop':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = ' 🔒'
            return return_message
        elif check_building_one >= 10 and check_building_two >= 10:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'castle':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'smithy'
        check_building_two = get_structure_level(tg_id, check_building_two)
        check_building_three = 'market'
        check_building_three = get_structure_level(tg_id, check_building_three)
        if check_building_one is None or check_building_two is None or check_building_three is None:
            return_message = ' 🔒'
            return return_message
        elif check_building_one >= 20 and check_building_two == 20 and check_building_three >= 10:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'smithy':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        check_building_two = 'barracks'
        check_building_two = get_structure_level(tg_id, check_building_two)
        if check_building_one is None or check_building_two is None:
            return_message = ' 🔒'
            return return_message
        elif check_building_one >= 10 and check_building_two >= 5:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'market':
        check_building_one = 'headquarters'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = ' 🔒'
            return return_message
        if check_building_one >= 10:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message
    if structure == 'wall':
        check_building_one = 'barracks'
        check_building_one = get_structure_level(tg_id, check_building_one)
        if check_building_one is None:
            return_message = ' 🔒'
            return return_message
        if check_building_one >= 3:
            return_message = ''
            return return_message
        else:
            return_message = ' 🔒'
            return return_message


def get_x_coordinates(village_id):
    for fetch_village_x in session.query(Village.x_coord).filter_by(pk=village_id).first():
        if fetch_village_x:
            return fetch_village_x


def get_y_coordinates(village_id):
    for fetch_village_y in session.query(Village.y_coord).filter_by(pk=village_id).first():
        if fetch_village_y:
            return fetch_village_y


def get_overview_coordinates(village_id):
    fetch_village_x = get_x_coordinates(village_id)
    fetch_village_y = get_y_coordinates(village_id)
    existing_coordinates = 'X:' + str(fetch_village_x) + ' Y:' + str(fetch_village_y) + ''
    if existing_coordinates:
        return existing_coordinates

def get_all_troops_population(tg_id):
    in_village = int(get_used_troops_in_village_pop(tg_id))
    in_recruitment = int(get_used_troops_in_recruitment_pop(tg_id))
    on_march = int(get_marching_troops(tg_id))
    supporting = int(get_supporting_troops(tg_id))
    result = in_village+in_recruitment+on_march+supporting
    return result

def get_used_troops_in_village_pop(tg_id):
    village_id = prof.cur_village_id(tg_id)
    unit_1 = str(session.query(Troops.spear_man).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_2 = str(session.query(Troops.sword_man).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_3 = str(session.query(Troops.brute).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_4 = str(session.query(Troops.archer).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_5 = str(session.query(Troops.scout).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_6 = str(session.query(Troops.light_cav).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_7 = str(session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_8 = str(session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_9 = str(session.query(Troops.ram).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_10 = str(session.query(Troops.catapult).filter_by(village_pk=village_id).first()).strip('(,)')
    unit_11 = str(session.query(Troops.noble).filter_by(village_pk=village_id).first()).strip('(,)')
    all_population_taken = (int(unit_1) + int(unit_2) + int(unit_3) + int(unit_4)) + (int(unit_5) * 2) + (int(unit_6) * 4) + (int(unit_7) * 6) + (int(unit_8) + int(unit_9) * 5) + (int(unit_10) * 8) + (int(unit_11) * 100)
    return all_population_taken

def get_used_troops_in_recruitment_pop(tg_id):
    village_id = prof.cur_village_id(tg_id)
    unit_1 = recruitmentdao.que_for_unit_clean(village_id,1)
    unit_2 = recruitmentdao.que_for_unit_clean(village_id,2)
    unit_3 = recruitmentdao.que_for_unit_clean(village_id,3)
    unit_4 = recruitmentdao.que_for_unit_clean(village_id,4)
    unit_5 = recruitmentdao.que_for_unit_clean(village_id,5)
    unit_6 = recruitmentdao.que_for_unit_clean(village_id,6)
    unit_7 = recruitmentdao.que_for_unit_clean(village_id,7)
    unit_8 = recruitmentdao.que_for_unit_clean(village_id,8)
    unit_9 = recruitmentdao.que_for_unit_clean(village_id,9)
    unit_10 = recruitmentdao.que_for_unit_clean(village_id,10)
    unit_11 = recruitmentdao.que_for_unit_clean(village_id,11)
    all_population_taken = (int(unit_1) + int(unit_2) + int(unit_3) + int(unit_4)) + (int(unit_5) * 2) + (int(unit_6) * 4) + (int(unit_7) * 6) + (int(unit_8) + int(unit_9) * 5) + (int(unit_10) * 8) + (int(unit_11) * 100)
    return all_population_taken

def get_marching_troops(tg_id):
    village_id = prof.cur_village_id(tg_id)
    unit_1 = wardao.get_spear_from_march_by_from_village_id(village_id)
    unit_2 = wardao.get_sword_from_march_by_from_village_id(village_id)
    unit_3 = wardao.get_brute_from_march_by_from_village_id(village_id)
    unit_4 = wardao.get_archer_from_march_by_from_village_id(village_id)
    unit_5 = wardao.get_scout_from_march_by_from_village_id(village_id)
    unit_6 = wardao.get_light_cav_from_march_by_from_village_id(village_id)
    unit_7 = wardao.get_heavy_cav_from_march_by_from_village_id(village_id)
    unit_8 = wardao.get_mounted_arch_from_march_by_from_village_id(village_id)
    unit_9 = wardao.get_ram_from_march_by_from_village_id(village_id)
    unit_10 = wardao.get_catapult_from_march_by_from_village_id(village_id)
    unit_11 = wardao.get_noble_from_march_by_from_village_id(village_id)
    all_population_taken = (int(unit_1) + int(unit_2) + int(unit_3) + int(unit_4)) + (int(unit_5) * 2) + (int(unit_6) * 4) + (int(unit_7) * 6) + (int(unit_8) + int(unit_9) * 5) + (int(unit_10) * 8) + (int(unit_11) * 100)
    return all_population_taken

def get_supporting_troops(tg_id):
    village_id = prof.cur_village_id(tg_id)
    unit_1 = wardao.get_spear_from_support_from_village_id(village_id)
    unit_2 = wardao.get_sword_from_support_from_village_id(village_id)
    unit_3 = wardao.get_brute_from_support_from_village_id(village_id)
    unit_4 = wardao.get_archer_from_support_from_village_id(village_id)
    unit_5 = wardao.get_scout_from_support_from_village_id(village_id)
    unit_6 = wardao.get_light_cav_from_support_from_village_id(village_id)
    unit_7 = wardao.get_heavy_cav_from_support_from_village_id(village_id)
    unit_8 = wardao.get_mounted_arch_from_support_from_village_id(village_id)
    unit_9 = wardao.get_ram_from_support_from_village_id(village_id)
    unit_10 = wardao.get_catapult_from_support_from_village_id(village_id)
    unit_11 = wardao.get_noble_from_support_from_village_id(village_id)
    all_population_taken = (int(unit_1) + int(unit_2) + int(unit_3) + int(unit_4)) + (int(unit_5) * 2) + (int(unit_6) * 4) + (int(unit_7) * 6) + (int(unit_8) + int(unit_9) * 5) + (int(unit_10) * 8) + (int(unit_11) * 100)
    return all_population_taken

def get_village_owner_id(village_pk):
    for owner_pk in session.query(Village.owner_pk).filter(Village.pk==village_pk).first():
        if owner_pk:
            return owner_pk

def get_village_name_by_pk(village_pk):
    for name in session.query(Village.village_name).filter(Village.pk==village_pk).first():
        if name:
            return name

def selecting_village_check(owner_pk, village_pk):
    village_owner = get_village_owner_id(village_pk)
    village_name = get_village_name_by_pk(village_pk)
    if int(village_owner) == int(owner_pk):
        set_village = session.query(Player).filter_by(pk=owner_pk).first()
        set_village.selected_village = village_pk
        session.add(set_village)
        session.commit()
        return_message = 'You\'ve selected ' + village_name
        return return_message
    if int(village_owner) != int(owner_pk):
        return_message = 'Why are you trying to see a village which doesn\'t belong to you?'
        return return_message

def selecting_marching_village_check(tg_id, village_pk):
    village = session.query(Village).filter_by(pk=village_pk).first()
    if village:
        player = session.query(Player).filter_by(tg_id=tg_id).first()
        player.selected_march_village = village_pk
        session.add(player)
        session.commit()
        return_message = war.generate_prepare_marching_overview(tg_id)
        return return_message
    else:
        return 'There\'s no village with such ID.'

def village_owner_check(owner_pk, village_pk):
    village_owner = get_village_owner_id(village_pk)
    if int(village_owner) != int(owner_pk):
        return False
    if int(village_owner) == int(owner_pk):
        return True

def set_new_village_name(village_pk, name):
    set_new_name = session.query(Village).filter_by(pk=village_pk).first()
    set_new_name.village_name = name
    session.add(set_new_name)
    session.commit()

def owner_name_of_village_no_list(village_pk):
    for owner in session.query(Village.owner_pk).filter_by(pk=village_pk).first():
        if owner:
            return owner

def get_village_owner_player_name(village_pk):
    owner = owner_name_of_village_no_list(village_pk)
    if owner is None or owner is 0:
        return '☠Barb☠'
    elif owner:
        for owner_name in session.query(Player.player_name).filter_by(pk=owner).first():
            if owner_name is None:
                return '☠Barb☠'
            elif owner_name:
                return owner_name


def get_wall_bonus(village_id):
    wall_level = get_wall_level(village_id)
    if wall_level is None:
        wall_level = 0
    wall_bonus = 1.037 ** wall_level
    return wall_bonus

def get_wall_level(village_id):
    for wall_level in session.query(Building.wall_level).filter_by(village_pk=village_id).first():
        if wall_level != None:
            return wall_level
        if wall_level == None:
            return 0