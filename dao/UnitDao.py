import datetime

from sqlalchemy import or_, func

from sqlalchemy import or_

from service import VillageService as vill
from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.research import Research
from models.unit import Unit
from models.troops import Troops
from models.support import Support
from models.marching import Marching
from models.prepare_marching import Prepare_marching
from service import ProfileService as prof
from dao import VillageDao as villagedao
from dao import RecruitmentDao as recruitmentdao
from dao import ResearchDao as researchdao
from dao import WarDao as wardao

session = None

def init(global_session):
    global session
    session = global_session

def get_amount(value1,value2):
    value = value1 - value2
    val = int(value)
    if val >= 0:
        return val
    else:
        val = 0
        return val

def get_unit_name(unit_id):
    if unit_id:
        for unit_name in session.query(Unit.unit_name).filter_by(pk=unit_id).first():
            if unit_name:
                return unit_name

def get_unit_wood(unit_pk):
    if unit_pk:
        for unit_wood in session.query(Unit.wood_cost).filter_by(pk=unit_pk).first():
            if unit_wood:
                return unit_wood

def get_unit_stone(unit_pk):
    if unit_pk:
        for unit_stone in session.query(Unit.stone_cost).filter_by(pk=unit_pk).first():
            if unit_stone:
                return unit_stone

def get_unit_iron(unit_pk):
    if unit_pk:
        for unit_iron in session.query(Unit.iron_cost).filter_by(pk=unit_pk).first():
            if unit_iron:
                return unit_iron

def get_unit_pop(unit_pk):
    if unit_pk:
        for unit_pop in session.query(Unit.population_cost).filter_by(pk=unit_pk).first():
            if unit_pop:
                return unit_pop

def get_unit_time(unit_pk):
    if unit_pk:
        for unit_time in session.query(Unit.recruit_time).filter_by(pk=unit_pk).first():
            if unit_time:
                return unit_time

def get_unit_id(unit_pk):
    for unit_id in session.query(Unit.pk).filter_by(pk=unit_pk).first():
        if unit_id:
            return unit_id

def get_unit_atk(unit_pk):
    for unit_atk in session.query(Unit.attack).filter_by(pk=unit_pk).first():
        if unit_atk:
            return unit_atk

def get_unit_def(unit_pk):
    for unit_def in session.query(Unit.defence).filter_by(pk=unit_pk).first():
        if unit_def:
            return unit_def

def get_unit_def_cav(unit_pk):
    for unit_def in session.query(Unit.defence_cav).filter_by(pk=unit_pk).first():
        if unit_def:
            return unit_def

def get_unit_def_arc(unit_pk):
    for unit_def in session.query(Unit.defence_arc).filter_by(pk=unit_pk).first():
        if unit_def:
            return unit_def

def get_unit_loot(unit_pk):
    for unit_loot in session.query(Unit.loot_carry).filter_by(pk=unit_pk).first():
        if unit_loot:
            return unit_loot

def get_unit_speed(unit_pk):
    for unit_speed in session.query(Unit.speed).filter_by(pk=unit_pk).first():
        if unit_speed:
            return unit_speed

def get_unit_view(unit_pk):
    view = get_unit_id(unit_pk)
    if view:
        return ' /unit_' + str(view)

def get_unit_research(tg_id, unit_pk):
    village = session.query(Player.selected_village).filter_by(tg_id=tg_id)
    if unit_pk is 1:
        for research_status in session.query(Research.spear_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_1'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 2:
        for research_status in session.query(Research.sword_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_2'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 3:
        for research_status in session.query(Research.brute).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_3'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 4:
        for research_status in session.query(Research.archer).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_4'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 5:
        for research_status in session.query(Research.scout).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_5'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 6:
        for research_status in session.query(Research.light_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_6'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 7:
        for research_status in session.query(Research.heavy_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_7'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 8:
        for research_status in session.query(Research.mounted_arch).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_8'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 9:
        for research_status in session.query(Research.ram).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_9'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 10:
        for research_status in session.query(Research.catapult).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '/recruit_10'
                return return_message
            else:
                return_message = '🔒'
                return return_message
    if unit_pk is 11:
        for castle in session.query(Building.castle_level).filter_by(village_pk=village).first():
            if castle is None:
                return_message = '🔒'
                return return_message
            elif castle == 1:
                return_message = '/recruit_11'
                return return_message

def get_spear_in_village(village_id):
    for unit in session.query(Troops.spear_man).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.spear_man)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.spear_man)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🔱 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_sword_in_village(village_id):
    for unit in session.query(Troops.sword_man).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.sword_man)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.sword_man)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🗡 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_brute_in_village(village_id):
    for unit in session.query(Troops.brute).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.brute)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.brute)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🔨 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_archer_in_village(village_id):
    for unit in session.query(Troops.archer).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.archer)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.archer)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🏹 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_scout_in_village(village_id):
    for unit in session.query(Troops.scout).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.scout)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.scout)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🐁 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_light_cav_in_village(village_id):
    for unit in session.query(Troops.light_cav).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.light_cav)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.light_cav)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🐎 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_heavy_cav_in_village(village_id):
    for unit in session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.heavy_cav)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.heavy_cav)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🎠 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_mounted_arch_in_village(village_id):
    for unit in session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.mounted_arch)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.mounted_arch)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🐎🏹 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_ram_in_village(village_id):
    for unit in session.query(Troops.ram).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.ram)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.ram)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('🥊 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_catapult_in_village(village_id):
    for unit in session.query(Troops.catapult).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.catapult)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.catapult)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('☄ ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_noble_in_village(village_id):
    for unit in session.query(Troops.noble).filter_by(village_pk=village_id).first():
        support = session.query(func.sum(Support.noble)).filter_by(in_village_id=village_id).scalar()
        external_troops = session.query(func.sum(Support.noble)).filter_by(from_village_id=village_id).scalar()
        troops = 0
        if unit:
            troops += unit
        if support:
            troops += support
        unit_text_list = []
        if (troops and troops > 0) or (external_troops and external_troops > 0):
            unit_text_list.append('👑 ' + str(troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(' (')
        if support and support > 0:
            unit_text_list.append('+' + str(support))
        if external_troops and external_troops > 0:
            if support and support > 0:
                unit_text_list.append(' | ')
            unit_text_list.append('-' + str(external_troops))
        if (support and support > 0) or (external_troops and external_troops > 0):
            unit_text_list.append(')')
        return ''.join(unit_text_list)

def get_noble_in_village_noble_view(village_id):
    for unit in session.query(Troops.noble).filter_by(village_pk=village_id).first():
        if unit is None or unit is 0:
            unit = 0
            return unit
        elif unit:
            unit = unit
            return unit

def get_all_player_nobles_from_player(village_id):
    troops = session.query(Troops.noble).filter_by(village_pk=village_id).first()
    if troops is None or 0:
        nobles_amount = 0
    else:
        nobles_amount = troops.noble
    return nobles_amount

def get_all_player_nobles(tg_id):
    noble_amount = 0
    owner_id = prof.cur_player_id(tg_id)
    village_pks = villagedao.get_all_village_id_of_player(owner_id)
    for village_pk in village_pks:
        noble_amount += int(get_all_player_nobles_from_player(village_pk))
    return noble_amount

def get_marching_nobles(tg_id):
    noble_amount = 0
    owner_id = prof.cur_player_id(tg_id)
    nobles = session.query(func.sum(Marching.noble)).filter(Marching.owner_pk==owner_id).scalar()
    if nobles:
        noble_amount = nobles
    return noble_amount

def get_unit_max(tg_id, unit_pk):
    village = session.query(Player.selected_village).filter_by(tg_id=tg_id).first()
    unit_wood = get_unit_wood(unit_pk)
    unit_stone = get_unit_stone(unit_pk)
    unit_iron = get_unit_iron(unit_pk)
    vil_wood = vill.get_wood_storage(tg_id)
    vil_stone = vill.get_stone_storage(tg_id)
    vil_iron = vill.get_iron_storage(tg_id)
    population_building = prof.get_village_used_population(tg_id)
    population_units = villagedao.get_all_troops_population(tg_id)
    population_limit = prof.get_current_population_limit(tg_id, structure='farm')
    quick_math = population_building + population_units
    if unit_pk is 1:
        for research_status in session.query(Research.spear_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 2:
        for research_status in session.query(Research.sword_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 3:
        for research_status in session.query(Research.brute).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 4:
        for research_status in session.query(Research.archer).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 5:
        for research_status in session.query(Research.scout).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/2
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 6:
        for research_status in session.query(Research.light_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/4
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 7:
        for research_status in session.query(Research.heavy_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/6
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 8:
        for research_status in session.query(Research.mounted_arch).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/5
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 9:
        for research_status in session.query(Research.ram).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/5
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 10:
        for research_status in session.query(Research.catapult).filter_by(village_pk=village).first():
            if research_status == 'YES':
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/8
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            else:
                return_message = '0'
                return return_message
    if unit_pk is 11:
        for research_status in session.query(Building.castle_level).filter_by(village_pk=village).first():
            if research_status is 1:
                math = []
                wood_math = vil_wood / unit_wood
                stone_math = vil_stone / unit_stone
                iron_math = vil_iron / unit_iron
                pop_math = get_amount(population_limit,quick_math)/100
                recruitment_nobles = recruitmentdao.que_for_unit_clean(village,11)
                max_nobles = researchdao.get_maximum_nobles(tg_id)
                all_nobles = get_all_player_nobles(tg_id)
                marching_nobles = get_marching_nobles(tg_id)
                count_user_villages = villagedao.count_user_villages(tg_id)
                can_be_made = int(max_nobles)-int(all_nobles)-int(recruitment_nobles)-int(marching_nobles)-int(count_user_villages-1)
                math.append(wood_math)
                math.append(stone_math)
                math.append(iron_math)
                math.append(pop_math)
                math.append(can_be_made)
                amount_with_decimal = min(math)
                amount = str(amount_with_decimal).split(".")[0]
                return amount
            elif research_status is None or research_status is 0:
                return_message = '0'
                return return_message

def get_spear_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.spear_man)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🔱 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_sword_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.sword_man)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🗡 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_brute_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.brute)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🔨 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_archer_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.archer)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🏹 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_scout_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.scout)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🐁 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_light_cav_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.light_cav)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🐎 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_heavy_cav_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.heavy_cav)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🎠 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_mounted_arch_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.mounted_arch)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🐎🏹 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_ram_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.ram)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('🥊 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_catapult_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.catapult)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('☄ ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_noble_in_support(support_id, village_id):
    external_troops = session.query(func.sum(Support.noble)).filter_by(from_village_id=village_id).filter_by(pk=support_id).scalar()
    unit_text_list = []
    if external_troops and external_troops > 0:
        unit_text_list.append('👑 ' + str(external_troops) + ' ')
    return ''.join(unit_text_list)

def get_spear_in_village_clean(village_id):
    for unit in session.query(Troops.spear_man).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🔱 ' + str(unit) + ' /all_1 /add_1')
            return ''.join(unit_text_list)

def get_sword_in_village_clean(village_id):
    for unit in session.query(Troops.sword_man).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🗡 ' + str(unit) + ' /all_2 /add_2')
            return ''.join(unit_text_list)

def get_brute_in_village_clean(village_id):
    for unit in session.query(Troops.brute).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🔨 ' + str(unit) + ' /all_3 /add_3')
            return ''.join(unit_text_list)

def get_archer_in_village_clean(village_id):
    for unit in session.query(Troops.archer).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🏹 ' + str(unit) + ' /all_4 /add_4')
            return ''.join(unit_text_list)

def get_scout_in_village_clean(village_id):
    for unit in session.query(Troops.scout).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🐁 ' + str(unit) + ' /all_5 /add_5')
            return ''.join(unit_text_list)

def get_light_cav_in_village_clean(village_id):
    for unit in session.query(Troops.light_cav).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🐎 ' + str(unit) + ' /all_6 /add_6')
            return ''.join(unit_text_list)

def get_heavy_cav_in_village_clean(village_id):
    for unit in session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🎠 ' + str(unit) + ' /all_7 /add_7')
            return ''.join(unit_text_list)

def get_mounted_arch_in_village_clean(village_id):
    for unit in session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🏹🐎 ' + str(unit) + ' /all_8 /add_8')
            return ''.join(unit_text_list)

def get_ram_in_village_clean(village_id):
    for unit in session.query(Troops.ram).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('🥊 ' + str(unit) + ' /all_9 /add_9')
            return ''.join(unit_text_list)

def get_catapult_in_village_clean(village_id):
    for unit in session.query(Troops.catapult).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('☄ ' + str(unit) + ' /all_10 /add_10')
            return ''.join(unit_text_list)

def get_noble_in_village_clean(village_id):
    for unit in session.query(Troops.noble).filter_by(village_pk=village_id).first():
        if unit:
            unit_text_list = []
            if unit and unit > 0:
                unit_text_list.append('👑 ' + str(unit) + ' /all_11 /add_11')
            return ''.join(unit_text_list)

def get_unit_in_prepare_march(unit_id, village_id):
    unit = session.query(Prepare_marching.amount).filter_by(sending_village=village_id).filter_by(unit=unit_id).first()
    if unit:
        unit_text_list = []
        if unit_id == 1:
            unit_text_list.append('🔱 ' + str(unit[0]) + ' /rem_1')
        elif unit_id == 2:
            unit_text_list.append('🗡 ' + str(unit[0]) + ' /rem_2')
        elif unit_id == 3:
            unit_text_list.append('🔨 ' + str(unit[0]) + ' /rem_3')
        elif unit_id == 4:
            unit_text_list.append('🏹 ' + str(unit[0]) + ' /rem_4')
        elif unit_id == 5:
            unit_text_list.append('🐁 ' + str(unit[0]) + ' /rem_5')
        elif unit_id == 6:
            unit_text_list.append('🐎 ' + str(unit[0]) + ' /rem_6')
        elif unit_id == 7:
            unit_text_list.append('🎠 ' + str(unit[0]) + ' /rem_7')
        elif unit_id == 8:
            unit_text_list.append('🏹🐎 ' + str(unit[0]) + ' /rem_8')
        elif unit_id == 9:
            unit_text_list.append('🥊 ' + str(unit[0]) + ' /rem_9')
        elif unit_id == 10:
            unit_text_list.append('☄ ' + str(unit[0]) + ' /rem_10')
        elif unit_id == 11:
            unit_text_list.append('👑 ' + str(unit[0]) + ' /rem_11')
        return ''.join(unit_text_list)

def get_unit_amount_defending_village(village_id, unit_id):
    if unit_id == 1:
        for unit in session.query(Troops.spear_man).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.spear_man)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 2:
        for unit in session.query(Troops.sword_man).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.sword_man)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 3:
        for unit in session.query(Troops.brute).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.brute)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 4:
        for unit in session.query(Troops.archer).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.archer)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 5:
        for unit in session.query(Troops.scout).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.scout)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 6:
        for unit in session.query(Troops.light_cav).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.light_cav)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 7:
        for unit in session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.heavy_cav)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 8:
        for unit in session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.mounted_arch)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 9:
        for unit in session.query(Troops.ram).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.ram)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 10:
        for unit in session.query(Troops.catapult).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.catapult)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops
    if unit_id == 11:
        for unit in session.query(Troops.noble).filter_by(village_pk=village_id).first():
            support = session.query(func.sum(Support.noble)).filter_by(in_village_id=village_id).scalar()
            troops = 0
            if unit:
                troops += unit
            if support:
                troops += support
            return troops