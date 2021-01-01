import re

from dao import ProfileDao as profiledao
from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import UnitDao as unitdao
from dao import WarDao as wardao
from service import ProfileService as prof, BuildingUpgradeService as buup, VillageService as vill

def village_overview_rally_point(village_id):
    unitlist = []
    unit1 = unitdao.get_spear_in_village(village_id)
    unit2 = unitdao.get_sword_in_village(village_id)
    unit3 = unitdao.get_brute_in_village(village_id)
    unit4 = unitdao.get_archer_in_village(village_id)
    unit5 = unitdao.get_scout_in_village(village_id)
    unit6 = unitdao.get_light_cav_in_village(village_id)
    unit7 = unitdao.get_heavy_cav_in_village(village_id)
    unit8 = unitdao.get_mounted_arch_in_village(village_id)
    unit9 = unitdao.get_ram_in_village(village_id)
    unit10 = unitdao.get_catapult_in_village(village_id)
    unit11 = unitdao.get_noble_in_village(village_id)
    unitlist.append(unit1)
    unitlist.append(unit2)
    unitlist.append(unit3)
    unitlist.append(unit4)
    unitlist.append(unit5)
    unitlist.append(unit6)
    unitlist.append(unit7)
    unitlist.append(unit8)
    unitlist.append(unit9)
    unitlist.append(unit10)
    unitlist.append(unit11)
    filter_list = []
    for value in unitlist:
        if value != None:
            filter_list.append(value)
    filter_list = list(filter(None, filter_list))
    if not filter_list:
        return_message = 'No troops.'
        return return_message
    return_message = '\n'.join(filter_list)
    return return_message

def village_overview_rally_point_support(support_id, village_id):
    unitlist = []
    unit1 = unitdao.get_spear_in_support(support_id, village_id)
    unit2 = unitdao.get_sword_in_support(support_id, village_id)
    unit3 = unitdao.get_brute_in_support(support_id, village_id)
    unit4 = unitdao.get_archer_in_support(support_id, village_id)
    unit5 = unitdao.get_scout_in_support(support_id, village_id)
    unit6 = unitdao.get_light_cav_in_support(support_id, village_id)
    unit7 = unitdao.get_heavy_cav_in_support(support_id, village_id)
    unit8 = unitdao.get_mounted_arch_in_support(support_id, village_id)
    unit9 = unitdao.get_ram_in_support(support_id, village_id)
    unit10 = unitdao.get_catapult_in_support(support_id, village_id)
    unit11 = unitdao.get_noble_in_support(support_id, village_id)
    unitlist.append(unit1)
    unitlist.append(unit2)
    unitlist.append(unit3)
    unitlist.append(unit4)
    unitlist.append(unit5)
    unitlist.append(unit6)
    unitlist.append(unit7)
    unitlist.append(unit8)
    unitlist.append(unit9)
    unitlist.append(unit10)
    unitlist.append(unit11)
    filter_list = []
    for value in unitlist:
        if value != None:
            filter_list.append(value)
    filter_list = list(filter(None, filter_list))
    if not filter_list:
        return_message = 'None'
        return return_message
    return_message = ''.join(filter_list)
    return return_message

def troop_march_overview(march_id):
    unitlist = []
    unit1 = wardao.get_unit_from_march_id(march_id, 1)
    unit2 = wardao.get_unit_from_march_id(march_id, 2)
    unit3 = wardao.get_unit_from_march_id(march_id, 3)
    unit4 = wardao.get_unit_from_march_id(march_id, 4)
    unit5 = wardao.get_unit_from_march_id(march_id, 5)
    unit6 = wardao.get_unit_from_march_id(march_id, 6)
    unit7 = wardao.get_unit_from_march_id(march_id, 7)
    unit8 = wardao.get_unit_from_march_id(march_id, 8)
    unit9 = wardao.get_unit_from_march_id(march_id, 9)
    unit10 = wardao.get_unit_from_march_id(march_id, 10)
    unit11 = wardao.get_unit_from_march_id(march_id, 11)
    unitlist.append(unit1)
    unitlist.append(unit2)
    unitlist.append(unit3)
    unitlist.append(unit4)
    unitlist.append(unit5)
    unitlist.append(unit6)
    unitlist.append(unit7)
    unitlist.append(unit8)
    unitlist.append(unit9)
    unitlist.append(unit10)
    unitlist.append(unit11)
    filter_list = []
    for value in unitlist:
        if value != None and value != '0':
            filter_list.append(value)
    filter_list = list(filter(None, filter_list))
    if not filter_list:
        return_message = 'None'
        return return_message
    return_message = ''.join(filter_list)
    return return_message

def village_overview_prepare_march(village_id):
    unitlist = []
    unit1 = unitdao.get_spear_in_village_clean(village_id)
    unit2 = unitdao.get_sword_in_village_clean(village_id)
    unit3 = unitdao.get_brute_in_village_clean(village_id)
    unit4 = unitdao.get_archer_in_village_clean(village_id)
    unit5 = unitdao.get_scout_in_village_clean(village_id)
    unit6 = unitdao.get_light_cav_in_village_clean(village_id)
    unit7 = unitdao.get_heavy_cav_in_village_clean(village_id)
    unit8 = unitdao.get_mounted_arch_in_village_clean(village_id)
    unit9 = unitdao.get_ram_in_village_clean(village_id)
    unit10 = unitdao.get_catapult_in_village_clean(village_id)
    unit11 = unitdao.get_noble_in_village_clean(village_id)
    unitlist.append(unit1)
    unitlist.append(unit2)
    unitlist.append(unit3)
    unitlist.append(unit4)
    unitlist.append(unit5)
    unitlist.append(unit6)
    unitlist.append(unit7)
    unitlist.append(unit8)
    unitlist.append(unit9)
    unitlist.append(unit10)
    unitlist.append(unit11)
    filter_list = []
    for value in unitlist:
        if value != None:
            filter_list.append(value)
    filter_list = list(filter(None, filter_list))
    if not filter_list:
        return_message = 'None'
        return return_message
    return_message = '\n'.join(filter_list)
    return return_message

def village_overview_prepare_march_selected(village_id):
    unitlist = []
    unit1 = unitdao.get_unit_in_prepare_march(1, village_id)
    unit2 = unitdao.get_unit_in_prepare_march(2, village_id)
    unit3 = unitdao.get_unit_in_prepare_march(3, village_id)
    unit4 = unitdao.get_unit_in_prepare_march(4, village_id)
    unit5 = unitdao.get_unit_in_prepare_march(5, village_id)
    unit6 = unitdao.get_unit_in_prepare_march(6, village_id)
    unit7 = unitdao.get_unit_in_prepare_march(7, village_id)
    unit8 = unitdao.get_unit_in_prepare_march(8, village_id)
    unit9 = unitdao.get_unit_in_prepare_march(9, village_id)
    unit10 = unitdao.get_unit_in_prepare_march(10, village_id)
    unit11 = unitdao.get_unit_in_prepare_march(11, village_id)
    unitlist.append(unit1)
    unitlist.append(unit2)
    unitlist.append(unit3)
    unitlist.append(unit4)
    unitlist.append(unit5)
    unitlist.append(unit6)
    unitlist.append(unit7)
    unitlist.append(unit8)
    unitlist.append(unit9)
    unitlist.append(unit10)
    unitlist.append(unit11)
    filter_list = []
    for value in unitlist:
        if value != None:
            filter_list.append(value)
    filter_list = list(filter(None, filter_list))
    if not filter_list:
        return_message = 'None'
        return return_message
    return_message = '\n'.join(filter_list)
    return return_message