import re
import logging
import itertools

from models.player import Player
from models.village import Village
from models.troops import Troops
from models.building import Building
from models.research import Research
from dao import VillageDao as villagedao
from dao import ProfileDao as profiledao
from dao import MapGenDao as mapgendao
from service import VillageService as vill, ProfileService as prof


def get_structure_level(tg_id, structure):
    current_structure_level = villagedao.get_structure_level(tg_id, structure)

    if current_structure_level is None:
        current_structure_level = 0
        return current_structure_level
    else:
        return current_structure_level


def get_structure_max_level(structure):
    structure_max_level = villagedao.get_structure_max_level(structure)

    if structure_max_level:
        return structure_max_level

def get_current_stock_by_village_pk(village_pk):
    wood = villagedao.get_wood_storage_by_pk(village_pk)
    if wood == None or wood == 0:
        wood = 0
    wood = int(wood)
    stone = villagedao.get_stone_storage_by_pk(village_pk)
    if stone == None or stone == 0:
        stone = 0
    stone = int(stone)
    iron = villagedao.get_iron_storage_by_pk(village_pk)
    if iron == None or iron == 0:
        iron = 0
    iron = int(iron)
    current_stock = '<code>📦 🪓' + str(wood) + ' ⛏' + str(stone) + ' 📏' + str(iron) + '</code>'
    return current_stock


def get_current_stock(tg_id):
    wood = vill.get_wood_storage(tg_id)
    wood = int(wood)
    if wood == 1 or wood == None:
        wood = 0
    stone = vill.get_stone_storage(tg_id)
    stone = int(stone)
    if stone < 1 or stone == None:
        stone = 0
    iron = vill.get_iron_storage(tg_id)
    iron = int(iron)
    if iron < 1 or iron == None:
        iron = 0
    current_stock = '<code>📦 🪓' + str(wood) + ' ⛏' + str(stone) + ' 📏' + str(iron) + '</code>'
    return current_stock

def get_current_stock_overview(village_pk):
    wood = vill.get_wood_storage_overview(village_pk)
    if wood == None:
        wood = 0
    wood = int(wood)
    stone = vill.get_stone_storage_overview(village_pk)
    if stone == None:
        stone = 0
    stone = int(stone)
    iron = vill.get_iron_storage_overview(village_pk)
    if iron == None:
        iron = 0
    iron = int(iron)
    current_stock = '<code>📦🪓' + str(wood) + ' ⛏' + str(stone) + ' 📏' + str(iron) + '</code>'
    return current_stock

def get_wood_storage(tg_id):
    current_wood_storage = villagedao.get_wood_storage(tg_id)

    if current_wood_storage == None or current_wood_storage < 0:
        current_wood_storage = 0
        return current_wood_storage
    else:
        return current_wood_storage


def get_stone_storage(tg_id):
    current_stone_storage = villagedao.get_stone_storage(tg_id)

    if current_stone_storage == None or current_stone_storage < 0:
        current_stone_storage = 0
        return current_stone_storage
    else:
        return current_stone_storage


def get_iron_storage(tg_id):
    current_iron_storage = villagedao.get_iron_storage(tg_id)

    if current_iron_storage == None or current_iron_storage < 0:
        current_iron_storage = 0
        return current_iron_storage
    else:
        return current_iron_storage

def get_wood_storage_overview(village_pk):
    current_wood_storage = villagedao.get_wood_storage_by_pk(village_pk)

    if current_wood_storage == None:
        current_wood_storage = 0
        return current_wood_storage
    if current_wood_storage != None:
        return current_wood_storage


def get_stone_storage_overview(village_pk):
    current_stone_storage = villagedao.get_stone_storage_by_pk(village_pk)

    if current_stone_storage == None:
        current_stone_storage = 0
        return current_stone_storage
    if current_stone_storage != None:
        return current_stone_storage


def get_iron_storage_overview(village_pk):
    current_iron_storage = villagedao.get_iron_storage_by_pk(village_pk)

    if current_iron_storage == None:
        current_iron_storage = 0
        return current_iron_storage
    if current_iron_storage != None:
        return current_iron_storage

def free_pop(tg_id, structure):
    population_building = prof.get_village_used_population(tg_id)
    population_units = villagedao.get_all_troops_population(tg_id)
    population_limit = prof.get_current_population_limit(tg_id, structure)

    if population_limit:
        free_population = population_limit - (population_building + population_units)
        return free_population

def get_all_population_from_village(tg_id):
    population_building = prof.get_village_used_population(tg_id)
    population_units = villagedao.get_all_troops_population(tg_id)
    quick_math = population_building + population_units
    return quick_math

def population_display(tg_id, structure):
    population_building = prof.get_village_used_population(tg_id)
    population_units = villagedao.get_all_troops_population(tg_id)
    population_limit = prof.get_current_population_limit(tg_id, structure)

    if population_limit:
        quick_math = population_building + population_units
        pop_display = '<code>(' + str(quick_math) + '/' + str(population_limit) + ')</code>'
        return pop_display

    if population_limit:
        quick_math = population_building + population_units
        pop_display = '<code>(' + str(quick_math) + '/' + str(population_limit) + ')</code>'
        return pop_display

def capacity_display(tg_id, structure):
    capacity_limit = prof.get_current_capacity_limit_overview(tg_id, structure)

    if capacity_limit:
        cap_display = '<code>' + str(capacity_limit) + '</code>'
        return cap_display


def production_display(tg_id):
    structure = 'woodcutter'
    production_wood = prof.get_current_production(tg_id, structure)
    structure = 'stone mine'
    production_stone = prof.get_current_production(tg_id, structure)
    structure = 'iron mine'
    production_iron = prof.get_current_production(tg_id, structure)

    if production_wood and production_stone and production_iron:
        pro_display = '<code>🪓' + str(production_wood) + '/h⛏' + str(production_stone) + '/h📏' + str(
            production_iron) + '/h</code>'
        return pro_display


def get_loyalty(tg_id):
    current_loyalty = villagedao.get_loyalty(tg_id)
    if current_loyalty != None:
        current_loyalty = int(current_loyalty)
        return current_loyalty
    if current_loyalty == None:
        current_loyalty = 'Error, contact @ECfbb_bot'
        return current_loyalty

def get_loyalty_overview(village_pk):
    current_loyalty = villagedao.get_loyalty_overview(village_pk)

    if current_loyalty != None:
        current_loyalty = int(current_loyalty)
        return current_loyalty
    elif current_loyalty is None:
        current_loyalty = 'Error, contact @ECfbb_bot'
        return current_loyalty

def selecting_another_village(tg_id, village_pk):
    owner_pk = prof.cur_player_id(tg_id)
    return_message = villagedao.selecting_village_check(owner_pk, village_pk)
    return return_message

def selecting_another_marching_village(tg_id, village_pk):
    return_message = villagedao.selecting_marching_village_check(tg_id, village_pk)
    return return_message

def rename_village_village(tg_id, village_pk, name):
    if '/' not in name:
        if len(name) > 30 or len(name) < 1:
            return_message ='Your village name was either too long or too short, please keep it less than 30 characters, but more than one single character.'
            return return_message
        owner_pk = prof.cur_player_id(tg_id)
        owner_check = villagedao.village_owner_check(owner_pk, village_pk)
        village_name = villagedao.get_village_name_by_pk(village_pk)
        if owner_check == True:
            villagedao.set_new_village_name(village_pk, name)
            return_message = 'You renamed ' + village_name + ' to ' + name
            return return_message
        if owner_check == False:
            return_message = 'You can\'t rename a village you don\'t own!'
            return return_message
    if '/' in name:
        return 'You used a character which is forbidden.'

def village_view(tg_id, village_pk):
    village_id = villagedao.get_village_owner_id(village_pk)
    village_owner = villagedao.get_village_owner_player_name(village_pk)
    village_name = villagedao.get_village_name_by_pk(village_pk)
    coordinates =  villagedao.get_overview_coordinates(village_pk)
    points = prof.get_village_overview_points(village_pk)
    distance = mapgendao.calculate_village_distance(tg_id, village_pk)
    if village_id is None or village_id is 0:
        return_message = 'Owner: 👤' + str(village_owner)+  '\n' \
                         'Village: 🏯' + str(village_name) + '\n' \
                         'Coordinates: 🗺' + str(coordinates) + '\n' \
                         'Points: 🏆' + str(points) + '\n' \
                         'Distance: 📍' + str(distance) + '\n\n' \
                         '⚔/attack_' + str(village_pk) + \
                         ' 🛡/support_' + str(village_pk) + \
                         ' 🎭/trade_' + str(village_pk)
        return return_message
    elif village_id > 0:
        return_message = 'Owner: 👤' + str(village_owner) + ' /pp' + str(village_id) +  '\n' \
                         'Village: 🏯' + str(village_name) + '\n' \
                         'Coordinates: 🗺' + str(coordinates) + '\n' \
                         'Points: 🏆' + str(points) + '\n' \
                         'Distance: 📍' + str(distance) + '\n\n' \
                         '⚔/attack_' + str(village_pk) + \
                         ' 🛡/support_' + str(village_pk) + \
                         ' 🎭/trade_' + str(village_pk)
        return return_message


def reclaim_a_village(tg_id, session):
    player_pk = profiledao.get_player_pk(tg_id)
    count_villages = villagedao.count_user_villages(tg_id)

    if count_villages != None:
        return 'You can\'t reclaim a village! You still have ' + count_villages + ' village(s) in your empire.'
    if count_villages == 0 or count_villages == None:
        # generating coordinates
        generated_coordinates = mapgendao.generate_coordinates()
        generated_coordinates = re.split('[(,)]', str(generated_coordinates))
        x_coord = generated_coordinates[0]
        y_coord = generated_coordinates[1]
        x_coord = str(x_coord)
        x_coord = float(x_coord)
        x_coord = round(x_coord)
        x_coord = int(x_coord)
        y_coord = str(y_coord)
        y_coord = float(y_coord)
        y_coord = round(y_coord)
        y_coord = int(y_coord)
        # Inserting the following statements to the Database:
        # Player, village and buildings creation
        new_village = Village()
        new_village.village_name = 'A new Horizon'
        new_village.owner_pk = int(player_pk)
        new_village.x_coord = x_coord
        new_village.y_coord = y_coord
        new_village.wood_stock = '2000'
        new_village.stone_stock = '2000'
        new_village.iron_stock = '2000'
        new_village.loyalty = '100'
        new_building = Building()
        new_building.village_id = new_village
        new_building.headquarter_level = '3'
        new_building.barrack_level = '1'
        new_building.archery_level = '0'
        new_building.stable_level = '0'
        new_building.siege_workshop_level = '0'
        new_building.castle_level = '0'
        new_building.smithy_level = '0'
        new_building.rally_point_level = '1'
        new_building.market_level = '0'
        new_building.woodcutter_level = '6'
        new_building.stone_mine_level = '6'
        new_building.iron_mine_level = '6'
        new_building.farm_level = '5'
        new_building.storage_level = '5'
        new_building.wall_level = '0'
        new_research = Research()
        new_research.village_id = new_village
        new_research.spear_man = 'YES'
        new_research.sword_man = 'YES'
        new_research.brute = 'NO'
        new_research.archer = 'NO'
        new_research.scout = 'YES'
        new_research.light_cav = 'NO'
        new_research.heavy_cav = 'NO'
        new_research.mounted_arch = 'NO'
        new_research.ram = 'NO'
        new_research.catapult = 'NO'
        new_troops = Troops()
        new_troops.village_id = new_village
        new_troops.spear_man = '100'
        new_troops.sword_man =  '100'
        new_troops.brute = '0'
        new_troops.archer = '0'
        new_troops.scout = '0'
        new_troops.light_cav = '0'
        new_troops.heavy_cav = '0'
        new_troops.mounted_arch = '0'
        new_troops.ram = '0'
        new_troops.catapult = '0'
        new_troops.noble = '0'
        session.add(new_village)
        session.add(new_building)
        session.add(new_research)
        session.add(new_troops)
        session.commit()
        select_village = session.query(Village.pk).filter_by(owner_pk=player_pk).first()
        set_village = session.query(Player).filter_by(pk=player_pk).first()
        set_village.selected_village = select_village
        session.add(set_village)
        session.commit()
        for _ in itertools.repeat(None, 2):
            # generating coordinates
            generated_coordinates = mapgendao.generate_coordinates()
            generated_coordinates = re.split('[(,)]', str(generated_coordinates))
            x_coord = generated_coordinates[0]
            y_coord = generated_coordinates[1]
            x_coord = str(x_coord)
            x_coord = float(x_coord)
            x_coord = round(x_coord)
            x_coord = int(x_coord)
            y_coord = str(y_coord)
            y_coord = float(y_coord)
            y_coord = round(y_coord)
            y_coord = int(y_coord)
            # Inserting the following statements to the Database:
            # Player, village and buildings creation
            new_village = Village()
            new_village.village_name = 'Barbarian'
            new_village.owner = None
            new_village.x_coord = x_coord
            new_village.y_coord = y_coord
            new_village.wood_stock = '1000'
            new_village.stone_stock = '1000'
            new_village.iron_stock = '1000'
            new_village.loyalty = '100'
            new_building = Building()
            new_building.village_id = new_village
            new_building.headquarter_level = '1'
            new_building.barrack_level = '0'
            new_building.archery_level = '0'
            new_building.stable_level = '0'
            new_building.siege_workshop_level = '0'
            new_building.castle_level = '0'
            new_building.smithy_level = '0'
            new_building.rally_point_level = '1'
            new_building.market_level = '0'
            new_building.woodcutter_level = '25'
            new_building.stone_mine_level = '25'
            new_building.iron_mine_level = '25'
            new_building.farm_level = '1'
            new_building.storage_level = '25'
            new_building.wall_level = '0'
            new_research = Research()
            new_research.village_id = new_village
            new_research.spear_man = 'YES'
            new_research.sword_man = 'NO'
            new_research.brute = 'NO'
            new_research.archer = 'NO'
            new_research.scout = 'YES'
            new_research.light_cav = 'NO'
            new_research.heavy_cav = 'NO'
            new_research.mounted_arch = 'NO'
            new_research.ram = 'NO'
            new_research.catapult = 'NO'
            new_troops = Troops()
            new_troops.village_id = new_village
            new_troops.spear_man = '0'
            new_troops.sword_man =  '0'
            new_troops.brute = '0'
            new_troops.archer = '0'
            new_troops.scout = '0'
            new_troops.light_cav = '0'
            new_troops.heavy_cav = '0'
            new_troops.mounted_arch = '0'
            new_troops.ram = '0'
            new_troops.catapult = '0'
            new_troops.noble = '0'
            session.add(new_village)
            session.add(new_building)
            session.add(new_research)
            session.add(new_troops)
            session.add(new_village)
            session.add(new_building)
            session.commit()
        return 'After wandering through the war stained lands, you\'ve found a small settlement...\nAfter talking with the villagers they got faith in your leadership and made you emperor of the village <code>A new Horizon</code>!\n\nSince this is your second village, you\'re blessed with a small advantage of the others.'