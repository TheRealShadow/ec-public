from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import ProfileDao as profiledao
from models.village import Village
from models.building import Building
from service import VillageService as vill, ProfileService as prof


def upgrade_view(structure):
    view = buildingdao.get_structure_id(structure)
    if view:
        return ' /str' + str(view)


def get_structure_upgrade(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    from_id = tg_id
    max_level = villagedao.get_structure_max_level(structure)
    structure_name = villagedao.get_structure_name(structure)
    needed_wood = get_wood_cost(tg_id, structure)
    needed_stone = get_stone_cost(tg_id, structure)
    needed_iron = get_iron_cost(tg_id, structure)
    needed_pop = get_total_pop_cost(tg_id, structure)
    previous_pop = get_dif_total_pop_cost(tg_id, structure)
    actual_pop = needed_pop - previous_pop
    current_wood = vill.get_wood_storage(from_id)
    current_wood = int(current_wood)
    current_stone = vill.get_stone_storage(from_id)
    current_stone = int(current_stone)
    current_iron = vill.get_iron_storage(from_id)
    current_iron = int(current_iron)
    used_building_pop = prof.get_village_used_population(tg_id)
    used_units_pop = villagedao.get_all_troops_population(tg_id)
    current_pop = prof.get_current_population_limit(tg_id, structure)
    unused_pop = current_pop - used_building_pop - used_units_pop
    upgrade = upgrade_check(from_id, structure)
    if current_level is None:
        actual_pop = needed_pop
        structure_level = 0
        structure_cost = '🪓' + str(needed_wood) + ' ⛏' + str(needed_stone) + ' 📏' + str(needed_iron) + ' 👥' + str(
            actual_pop)
        current_stock = '🪓' + str(current_wood) + ' ⛏' + str(current_stone) + ' 📏' + str(current_iron) + ' 👥' + str(
            unused_pop)
        return_message = 'If you wish to upgrade your ' + str(structure_name) + ' to level ' + str(structure_level + 1) + ':\nThis will cost you: <code>' + str(structure_cost) + '</code>\nyou currently have: <code>' + str(current_stock) + '</code>\n' + upgrade
        return return_message
    elif current_level < max_level:
        structure_level = current_level
        upgrade = upgrade_check(from_id, structure)
        structure_cost = '🪓' + str(needed_wood) + ' ⛏' + str(needed_stone) + ' 📏' + str(needed_iron) + ' 👥' + str(
            actual_pop)
        current_stock = '🪓' + str(current_wood) + ' ⛏' + str(current_stone) + ' 📏' + str(current_iron) + ' 👥' + str(
            unused_pop)
        return_message = 'If you wish to upgrade your ' + structure_name + ' to level ' + str(
            structure_level + 1) + ':\nThis will cost you: <code>' + structure_cost + '</code>\nyou currently have: <code>' + current_stock + '</code>\n' + upgrade
        return return_message
    else:
        return_message = 'You\'ve reached the maximum level for this building!'
        return return_message


def upgrade_check_action(tg_id, structure, session):
    current_village = profiledao.get_cur_village_id(tg_id)
    max_level = villagedao.get_structure_max_level(structure)
    structure_name = villagedao.get_structure_name(structure)
    current_wood = vill.get_wood_storage(tg_id)
    current_stone = vill.get_stone_storage(tg_id)
    current_iron = vill.get_iron_storage(tg_id)
    needed_wood = get_wood_cost(tg_id, structure)
    needed_stone = get_stone_cost(tg_id, structure)
    needed_iron = get_iron_cost(tg_id, structure)
    possible = upgrade_check_statements(tg_id, structure)
    current_level = villagedao.get_structure_level(tg_id, structure)
    needed_pop = get_total_pop_cost(tg_id, structure)
    previous_pop = get_dif_total_pop_cost(tg_id, structure)
    actual_pop = needed_pop - previous_pop
    used_building_pop = prof.get_village_used_population(tg_id)
    used_units_pop = villagedao.get_all_troops_population(tg_id)
    current_pop = prof.get_current_population_limit(tg_id, structure)
    unused_pop = current_pop - used_building_pop - used_units_pop
    requirements_met = villagedao.get_upgrade_requirement(tg_id, structure)
    if current_level is None and int(current_wood) >= int(needed_wood) and int(current_stone) >= int(
            needed_stone) and int(current_iron) >= int(needed_iron) and requirements_met == 1 and (needed_pop is 0 or
            int(unused_pop) >= int(actual_pop)):
        building_upgrade = session.query(Building).filter_by(village_pk=current_village).first()
        building_upgrade.village_pk = current_village
        if structure_name == 'Headquarters':
            current_level = 0
            building_upgrade.headquarter_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Barracks':
            current_level = 0
            building_upgrade.barrack_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Archery':
            current_level = 0
            building_upgrade.archery_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stable':
            current_level = 0
            building_upgrade.stable_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Siege Workshop':
            current_level = 0
            building_upgrade.siege_workshop_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Castle':
            current_level = 0
            building_upgrade.castle_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Smithy':
            current_level = 0
            building_upgrade.smithy_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Rally Point':
            current_level = 0
            building_upgrade.rally_point_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Market':
            current_level = 0
            building_upgrade.market_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Woodcutter':
            current_level = 0
            building_upgrade.woodcutter_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stone Mine':
            current_level = 0
            building_upgrade.stone_mine_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Iron Mine':
            current_level = 0
            building_upgrade.iron_mine_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Farm':
            current_level = 0
            building_upgrade.farm_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Storage':
            current_level = 0
            building_upgrade.storage_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Wall':
            current_level = 0
            building_upgrade.wall_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
    elif requirements_met == 2:
        return_message = 'You didn\'t meet the building requirements.'
        return return_message
    elif current_level < max_level and int(current_wood) >= int(needed_wood) and int(current_stone) >= int(
            needed_stone) and int(current_iron) >= int(needed_iron) and requirements_met == 1 and (needed_pop == 0 or
            int(unused_pop) >= int(actual_pop)):
        building_upgrade = session.query(Building).filter_by(village_pk=current_village).first()
        building_upgrade.village_pk = current_village
        if structure_name == 'Headquarters':
            building_upgrade.headquarter_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Barracks':
            building_upgrade.barrack_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Archery':
            building_upgrade.archery_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stable':
            building_upgrade.stable_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Siege Workshop':
            building_upgrade.siege_workshop_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Castle':
            building_upgrade.castle_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Smithy':
            building_upgrade.smithy_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Rally Point':
            building_upgrade.rally_point_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Market':
            building_upgrade.market_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Woodcutter':
            building_upgrade.woodcutter_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stone Mine':
            building_upgrade.stone_mine_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Iron Mine':
            building_upgrade.iron_mine_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Farm':
            building_upgrade.farm_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Storage':
            building_upgrade.storage_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Wall':
            building_upgrade.wall_level = current_level + 1
            resources_removal = session.query(Village).filter_by(pk=current_village).first()
            resources_removal.wood_stock = int(current_wood) - int(needed_wood)
            resources_removal.stone_stock = int(current_stone) - int(needed_stone)
            resources_removal.iron_stock = int(current_iron) - int(needed_iron)
            session.add(building_upgrade)
            session.add(resources_removal)
            session.commit()
            return_message = 'Upgrade on ' + structure_name + ' was successful!'
            return return_message
    elif current_level is None and (
            int(current_wood) <= int(needed_wood) or int(current_stone) <= int(needed_stone) or int(
        current_iron) <= int(needed_iron)) or requirements_met == 2 or (int(unused_pop) < int(actual_pop)):
        return_message = 'You didn\'t meet resources needed to build this.'
        return return_message
    elif current_level == max_level:
        return_message = 'You already reached the maximum level for this building! Why do you still try to upgrade it?'
        return return_message
    elif possible is False:
        return_message = 'You either don\'t have enough resources for this upgrade or you don\'t have enough free population.'
        return return_message


def get_wood_cost(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_wood = buildingdao.get_structure_wood_base(structure)
    wood_factor = buildingdao.get_structure_wood_factor(structure)
    if current_level is None:
        wood_upgrade_cost = int(base_wood)
        return wood_upgrade_cost
    else:
        level = int(current_level + 1)
        wood_upgrade_cost = int(base_wood) * wood_factor ** level
        wood_upgrade_cost = int(wood_upgrade_cost)
        return wood_upgrade_cost


def get_stone_cost(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_stone = buildingdao.get_structure_stone_base(structure)
    stone_factor = buildingdao.get_structure_stone_factor(structure)
    if current_level is None:
        stone_upgrade_cost = int(base_stone)
        return stone_upgrade_cost
    else:
        level = int(current_level + 1)
        stone_upgrade_cost = int(base_stone) * stone_factor ** level
        stone_upgrade_cost = int(stone_upgrade_cost)
        return stone_upgrade_cost


def get_iron_cost(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_iron = buildingdao.get_structure_iron_base(structure)
    iron_factor = buildingdao.get_structure_iron_factor(structure)
    if current_level is None:
        iron_upgrade_cost = int(base_iron)
        return iron_upgrade_cost
    else:
        level = int(current_level + 1)
        iron_upgrade_cost = int(base_iron) * iron_factor ** level
        iron_upgrade_cost = int(iron_upgrade_cost)
        return iron_upgrade_cost


def get_dif_total_pop_cost(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_pop = buildingdao.get_structure_pop_base(structure)
    pop_factor = buildingdao.get_structure_pop_factor(structure)
    if base_pop is None:
        base_pop = 0
        level = int(current_level)
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost
    elif current_level is None:
        current_level = 0
        level = int(current_level)
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost
    else:
        level = int(current_level)
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost


def get_total_pop_cost(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_pop = buildingdao.get_structure_pop_base(structure)
    pop_factor = buildingdao.get_structure_pop_factor(structure)
    if current_level is None:
        pop_cost = int(base_pop)
        return pop_cost
    elif base_pop is None:
        base_pop = 0
        level = int(current_level) + 1
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost
    elif structure is 'farm' or structure is 'storage':
        pop_cost = 0
        return pop_cost
    else:
        level = int(current_level) + 1
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost


def get_used_pop(tg_id, structure):
    current_level = villagedao.get_structure_level(tg_id, structure)
    base_pop = buildingdao.get_structure_pop_base(structure)
    pop_factor = buildingdao.get_structure_pop_factor(structure)
    if current_level is None or current_level is 0:
        pop_cost = 0
        return pop_cost
    elif base_pop is None:
        base_pop = 0
        level = int(current_level)
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost
    else:
        level = int(current_level)
        pop_cost = int(base_pop) * pop_factor ** level
        pop_cost = int(pop_cost)
        return pop_cost


def upgrade_check(tg_id, structure):
    current_wood = vill.get_wood_storage(tg_id)
    current_stone = vill.get_stone_storage(tg_id)
    current_iron = vill.get_iron_storage(tg_id)
    current_free_pop = vill.free_pop(tg_id, structure)
    needed_wood = get_wood_cost(tg_id, structure)
    needed_stone = get_stone_cost(tg_id, structure)
    needed_iron = get_iron_cost(tg_id, structure)
    needed_population = get_total_pop_cost(tg_id, structure)
    needed_pop = get_total_pop_cost(tg_id, structure)
    previous_pop = get_dif_total_pop_cost(tg_id, structure)
    actual_pop = needed_pop - previous_pop
    view = buildingdao.get_structure_id(structure)
    upgrade_possible = str('You can upgrade ' + structure + '! /upg' + str(view))
    upgrade_denied = str('Upgrade of ' + structure + ' is not possible.')
    upgrade_requirements = villagedao.get_upgrade_requirement(tg_id, structure)
    requirements_not_met = villagedao.get_upgrade_requirement_reply(tg_id, structure)
    if int(current_wood) >= int(needed_wood) and int(current_stone) >= int(needed_stone) and int(current_iron) >= int(
        needed_iron) and needed_population == 0 and upgrade_requirements == 1:
        return upgrade_possible
    elif int(current_wood) >= int(needed_wood) and int(current_stone) >= int(needed_stone) and int(current_iron) >= int(
            needed_iron) and int(current_free_pop) >= int(actual_pop) and upgrade_requirements == 1:
        return upgrade_possible
    elif upgrade_requirements == 2:
        return requirements_not_met
    else:
        return upgrade_denied


def village_upgrade_check(tg_id, structure):
    current_wood = vill.get_wood_storage(tg_id)
    current_stone = vill.get_stone_storage(tg_id)
    current_iron = vill.get_iron_storage(tg_id)
    current_free_pop = vill.free_pop(tg_id, structure)
    needed_wood = get_wood_cost(tg_id, structure)
    needed_stone = get_stone_cost(tg_id, structure)
    needed_iron = get_iron_cost(tg_id, structure)
    current_used_pop = get_total_pop_cost(tg_id, structure)
    view = buildingdao.get_structure_id(structure)
    upgrade_possible = '/upg' + str(view)
    upgrade_denied = ''
    upgrade_locked = '🔒'
    if int(current_wood) >= int(needed_wood) and int(current_stone) >= int(needed_stone) and int(current_iron) >= int(
            needed_iron) and int(current_free_pop) >= int(current_used_pop):
        return upgrade_possible
    elif int(current_wood) <= int(needed_wood) or int(current_stone) <= int(needed_stone) or int(current_iron) <= int(
            needed_iron) or int(current_free_pop) <= int(current_used_pop):
        return upgrade_denied
    else:
        return upgrade_locked


def upgrade_check_statements(tg_id, structure):
    current_wood = vill.get_wood_storage(tg_id)
    current_stone = vill.get_stone_storage(tg_id)
    current_iron = vill.get_iron_storage(tg_id)
    current_free_pop = vill.free_pop(tg_id, structure)
    needed_wood = get_wood_cost(tg_id, structure)
    needed_stone = get_stone_cost(tg_id, structure)
    needed_iron = get_iron_cost(tg_id, structure)
    current_used_pop = get_total_pop_cost(tg_id, structure)
    if int(current_wood) >= int(needed_wood) and int(current_stone) >= int(needed_stone) and int(current_iron) >= int(
            needed_iron) and int(current_free_pop) >= int(current_used_pop):
        return True
    else:
        return False


def get_structure_downgrade(tg_id, structure, session):
    player_pk = prof.cur_player_id(tg_id)
    downgrade_available = profiledao.get_downgrade_setting_by_pk(player_pk)
    current_level = villagedao.get_structure_level(tg_id, structure)
    min_level = villagedao.get_structure_min_level(structure)
    downgrade = downgrade_check(tg_id, structure)
    fetch_headquarters = 'headquarters'
    headquarters_level = villagedao.get_structure_level(tg_id, fetch_headquarters)
    if downgrade_available == 1:
        if min_level is None:
            min_level = 0
            if current_level is None:
                current_level = 0
                if current_level is 0 and headquarters_level >= 10:
                    return_message = downgrade
                    return return_message
                elif current_level > min_level and headquarters_level >= 10:
                    return_message = downgrade
                    return return_message
                elif headquarters_level <= 10:
                    return_message = ''
                    return return_message
                else:
                    return 'welp'
            elif current_level is None and headquarters_level >= 10:
                return_message = downgrade
                return return_message
            elif current_level > min_level and headquarters_level >= 10:
                return_message = downgrade
                return return_message
            elif headquarters_level <= 10:
                return_message = ''
                return return_message
            else:
                return 'welp'
    if downgrade_available == 0 or downgrade_available == None:
        return ''

def downgrade_check(tg_id, structure):
    view = buildingdao.get_structure_id(structure)
    downgrade_possible = '\nYou can downgrade ' + structure + '! /dow' + str(view)
    downgrade_hq = '\nYou can\'t downgrade it lower'
    downgrade_denied = '\nDowngrades of buildings are not yet possible.'
    fetch_headquarters = 'headquarters'
    headquarters_level = villagedao.get_structure_level(tg_id, fetch_headquarters)
    if headquarters_level < 10:
        return downgrade_denied
    elif structure is 'headquarters' and headquarters_level is 10:
        return downgrade_hq
    elif structure is 'barracks' and headquarters_level is 10:
        return downgrade_possible
    elif headquarters_level >= 10:
        return downgrade_possible


def downgrade_check_action(tg_id, structure, session):
    current_village = profiledao.get_cur_village_id(tg_id)
    min_level = villagedao.get_structure_min_level(structure)
    structure_name = villagedao.get_structure_name(structure)
    current_level = villagedao.get_structure_level(tg_id, structure)
    fetch_headquarters = 'headquarters'
    headquarters_level = villagedao.get_structure_level(tg_id, fetch_headquarters)
    loyalty = villagedao.get_loyalty(tg_id)
    if headquarters_level >= 10 and loyalty == 100 and min_level is None or min_level is 0:
        min_level = 0
        building_downgrade = session.query(Building).filter_by(village_pk=current_village).first()
        building_downgrade.village_pk = current_village
        if structure_name == 'Headquarters' and 10 < current_level:
            building_downgrade.headquarter_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Headquarters' and 10 == current_level:
            return_message = 'You can\'t downgrade ' + structure_name + ' further than this'
            return return_message
        elif structure_name == 'Barracks' and min_level < current_level:
            building_downgrade.barrack_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Archery' and min_level < current_level:
            building_downgrade.archery_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stable' and min_level < current_level:
            building_downgrade.stable_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Siege Workshop' and min_level < current_level:
            building_downgrade.siege_workshop_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Castle' and min_level < current_level:
            building_downgrade.castle_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Smithy' and min_level < current_level:
            building_downgrade.smithy_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Rally Point' and min_level < current_level:
            building_downgrade.rally_point_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Market' and min_level < current_level:
            building_downgrade.market_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Woodcutter' and min_level < current_level:
            building_downgrade.woodcutter_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stone Mine' and min_level < current_level:
            building_downgrade.stone_mine_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Iron Mine' and min_level < current_level:
            building_downgrade.iron_mine_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Farm' and min_level < current_level:
            building_downgrade.farm_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Storage' and min_level < current_level:
            building_downgrade.storage_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Wall' and min_level < current_level:
            building_downgrade.wall_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
    elif headquarters_level >= 10 and loyalty == 100 and min_level > 0:
        building_downgrade = session.query(Building).filter_by(village_pk=current_village).first()
        building_downgrade.village_pk = current_village
        if structure_name == 'Headquarters' and 10 < current_level:
            building_downgrade.headquarter_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Headquarters' and 10 == current_level:
            return_message = 'You can\'t downgrade ' + structure_name + ' further than this'
            return return_message
        elif structure_name == 'Barracks' and min_level < current_level:
            building_downgrade.barrack_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Archery' and min_level < current_level:
            building_downgrade.archery_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stable' and min_level < current_level:
            building_downgrade.stable_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Siege Workshop' and min_level < current_level:
            building_downgrade.siege_workshop_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Castle' and min_level < current_level:
            building_downgrade.castle_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Smithy' and min_level < current_level:
            building_downgrade.smithy_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Rally Point' and min_level < current_level:
            building_downgrade.rally_point_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Market' and min_level < current_level:
            building_downgrade.market_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Woodcutter' and min_level < current_level:
            building_downgrade.woodcutter_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Stone Mine' and min_level < current_level:
            building_downgrade.stone_mine_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Iron Mine' and min_level < current_level:
            building_downgrade.iron_mine_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Farm' and min_level < current_level:
            building_downgrade.farm_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Storage' and min_level < current_level:
            building_downgrade.storage_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
        elif structure_name == 'Wall' and min_level < current_level:
            building_downgrade.wall_level = current_level - 1
            session.add(building_downgrade)
            session.commit()
            return_message = 'Downgrade on ' + structure_name + ' was successful!'
            return return_message
    elif loyalty < 100:
        return_message = 'You can\'t downgrade buildings if the current Loyalty is lower than 100!'
        return return_message
    elif headquarters_level < 10:
        return_message = 'If you wish to downgrade buildings, you need <b>🏛headquarters level 10</b>.'
        return return_message
