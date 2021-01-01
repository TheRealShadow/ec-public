import datetime
from math import sqrt

from sqlalchemy import or_

from service import VillageService as vill
from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.research import Research
from models.unit import Unit
from models.troops import Troops
from dao import UnitDao as unitdao
from dao import ProfileDao as profiledao
from dao import RecruitmentDao as recruitmentdao
from dao import VillageDao as villagedao
from service import ProfileService as prof, RecruitmentService as rec

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
        val = '0'
        return val

def quick_research_check(tg_id, unit_pk):
    village = session.query(Player.selected_village).filter_by(tg_id=tg_id)
    if unit_pk is 1:
        for research_status in session.query(Research.spear_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 2:
        for research_status in session.query(Research.sword_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 3:
        for research_status in session.query(Research.brute).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 4:
        for research_status in session.query(Research.archer).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 5:
        for research_status in session.query(Research.scout).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 6:
        for research_status in session.query(Research.light_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 7:
        for research_status in session.query(Research.heavy_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 8:
        for research_status in session.query(Research.mounted_arch).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 9:
        for research_status in session.query(Research.ram).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 10:
        for research_status in session.query(Research.catapult).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = 'YES'
                return return_message
            else:
                return_message = 'NO'
                return return_message
    if unit_pk is 11:
        for castle in session.query(Building.castle_level).filter_by(village_pk=village).first():
            if castle is None or castle is 0:
                return_message = 'NO'
                return return_message
            elif castle == 1:
                return_message = 'YES'
                return return_message

def get_unit_research(tg_id, unit_pk):
    village = session.query(Player.selected_village).filter_by(tg_id=tg_id)
    if unit_pk is 1:
        for research_status in session.query(Research.spear_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 2:
        for research_status in session.query(Research.sword_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 3:
        for research_status in session.query(Research.brute).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 4:
        for research_status in session.query(Research.archer).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 5:
        for research_status in session.query(Research.scout).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 6:
        for research_status in session.query(Research.light_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 7:
        for research_status in session.query(Research.heavy_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 8:
        for research_status in session.query(Research.mounted_arch).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 9:
        for research_status in session.query(Research.ram).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 10:
        for research_status in session.query(Research.catapult).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '✅'
                return return_message
            else:
                return_message = '❌'
                return return_message
    if unit_pk is 11:
        for castle in session.query(Building.castle_level).filter_by(village_pk=village).first():
            if castle is None or castle is 0:
                return_message = '❌'
                return return_message
            elif castle == 1:
                return_message = '✅'
                return return_message

def get_player_pouches(tg_id):
    player_id = profiledao.get_player_pk(tg_id)
    for pouches in session.query(Player.pouches).filter_by(pk=player_id).first():
        if pouches is None:
            pouches = 0
            return pouches
        else:
            return pouches

def get_maximum_nobles(tg_id):
    count_user_villages = villagedao.count_user_villages(tg_id)
    pouches = get_player_pouches(tg_id)
    max_nobles = int(1/2*(sqrt(8*pouches+1)-1))
    return max_nobles

def get_needed_pouches(tg_id):
    numberNobles = get_maximum_nobles(tg_id)
    needed_pouches = ((numberNobles + 1) * (numberNobles + 1) + numberNobles +1) /2
    return needed_pouches

def noble_pouch_and_recruit_status(tg_id):
    count_user_villages = villagedao.count_user_villages(tg_id)
    village_id = prof.cur_village_id(tg_id)
    noble_amount = unitdao.get_noble_in_village_noble_view(village_id)
    current_pouches = get_player_pouches(tg_id)
    needed_pouches = get_needed_pouches(tg_id)
    recruitment_nobles = recruitmentdao.que_for_unit_clean(village_id,11)
    max_nobles = int(get_maximum_nobles(tg_id)-(count_user_villages-1))
    captured_villages = int(count_user_villages-1)
    all_nobles = unitdao.get_all_player_nobles(tg_id)
    other_nobles = unitdao.get_all_player_nobles(tg_id)-noble_amount
    nobles_marching = unitdao.get_marching_nobles(tg_id)
    can_be_made = int(max_nobles)-int(all_nobles)-int(recruitment_nobles)-int(nobles_marching)
    wood = int(vill.get_wood_storage(tg_id))
    stone = int(vill.get_stone_storage(tg_id))
    iron = int(vill.get_iron_storage(tg_id))
    return_message = '\n\n👑Nobles of your Empire\n' + 'You have ' + str(int(current_pouches)) + ' 👝\n' + str(int(needed_pouches)) + '👝 needed for next noble\nMax nobles: ' + str(int(max_nobles)) + '\nCaptured villages: ' + str(int(captured_villages)) + '\nCan be made: ' + str(int(can_be_made)) + '\nNobles in village: ' + str(int(noble_amount)) + '\nNobles in other villages: ' + str(int(other_nobles)) + '\n\nOne pouch costs 🪓28000 ⛏30000 📏25000\nYou have: 🪓' + str(int(wood)) + ' ⛏' + str(int(stone)) + ' 📏' + str(int(iron))
    return return_message

def research_possible(tg_id,village,unit_pk):
    if unit_pk is 1:
        for research_status in session.query(Research.spear_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 400
                stone_cost = 500
                iron_cost = 500
                if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                    return_message = '\nYou can research this unit! /research_1\n'
                    return return_message
                else:
                    return_message = '\nYou can\'t research this\n'
                    return return_message
    if unit_pk is 2:
        for research_status in session.query(Research.sword_man).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 600
                stone_cost = 300
                iron_cost = 450
                barracks_level = vill.get_structure_level(tg_id,'barracks')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if barracks_level >= 5 and smithy_level >= 1:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_2\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>⚔Barracks Level 5\n</i>            └<i>⚒Smithy Level 1\n</i>'
                    return return_message
    if unit_pk is 3:
        for research_status in session.query(Research.brute).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 500
                stone_cost = 400
                iron_cost = 600
                barracks_level = vill.get_structure_level(tg_id,'barracks')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if barracks_level >= 3 and smithy_level >= 1:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_3\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>⚔Barracks Level 3</i>\n            └<i>⚒Smithy Level 1\n</i>'
                    return return_message
    if unit_pk is 4:
        for research_status in session.query(Research.archer).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 500
                stone_cost = 400
                iron_cost = 600
                archery_level = vill.get_structure_level(tg_id,'archery')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if archery_level >= 1 and smithy_level >=1:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_4\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>🏹Archery Level 1</i>\n            └<i>⚒Smithy Level 1\n</i>'
                    return return_message
    if unit_pk is 8:
        for research_status in session.query(Research.mounted_arch).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 2000
                stone_cost = 1800
                iron_cost = 2400
                archery_level = vill.get_structure_level(tg_id,'archery')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if archery_level >= 10 and smithy_level >= 10:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_8\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>🏹Archery Level 10</i>\n            └<i>⚒Smithy Level 10</i>\n'
                    return return_message
    if unit_pk is 5:
        for research_status in session.query(Research.scout).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 200
                stone_cost = 200
                iron_cost = 250
                stable_level = vill.get_structure_level(tg_id,'stable')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if stable_level >= 1 and smithy_level >= 1:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_5\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>🐎Stable Level 1</i>\n            └<i>⚒Smithy Level 1</i>\n'
                    return return_message
    if unit_pk is 6:
        for research_status in session.query(Research.light_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 2400
                stone_cost = 2000
                iron_cost = 3000
                stable_level = vill.get_structure_level(tg_id,'stable')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if stable_level >= 3 and smithy_level >= 5:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_6\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>🐎Stable Level 3</i>\n            └<i>⚒Smithy Level 5</i>\n'
                    return return_message
    if unit_pk is 7:
        for research_status in session.query(Research.heavy_cav).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 3800
                stone_cost = 3600
                iron_cost = 4500
                stable_level = vill.get_structure_level(tg_id,'stable')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if stable_level >= 10 and smithy_level >= 15:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_7\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>🐎Stable Level 10</i>\n            └<i>⚒Smithy Level 15</i>\n'
                    return return_message
    if unit_pk is 9:
        for research_status in session.query(Research.ram).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 3000
                stone_cost = 3000
                iron_cost = 3500
                siege_workshop_level = vill.get_structure_level(tg_id,'siege workshop')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if siege_workshop_level >= 3 and smithy_level >= 5:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_9\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>💣Siege workshop Level 3</i>\n            └<i>⚒Smithy Level 5</i>\n'
                    return return_message
    if unit_pk is 10:
        for research_status in session.query(Research.catapult).filter_by(village_pk=village).first():
            if research_status == 'YES':
                return_message = '\n'
                return return_message
            elif research_status == 'NO':
                village_wood = vill.get_wood_storage(tg_id)
                village_stone = vill.get_stone_storage(tg_id)
                village_iron = vill.get_iron_storage(tg_id)
                wood_cost = 5000
                stone_cost = 7000
                iron_cost = 6000
                siege_workshop_level = vill.get_structure_level(tg_id,'siege workshop')
                smithy_level = vill.get_structure_level(tg_id,'smithy')
                if siege_workshop_level >= 10 and smithy_level >= 20:
                    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost:
                        return_message = ' - /research_10\n'
                        return return_message
                    else:
                        wood = str(get_amount(wood_cost,village_wood))
                        stone = str(get_amount(stone_cost,village_stone))
                        iron = str(get_amount(iron_cost,village_iron))
                        return_message = ' - You can\'t research this!\nMissing: 🪓' + wood + ' ⛏' + stone + ' 📏' + iron + '\n'
                        return return_message
                else:
                    return_message = ' - Req missing!\n            └<i>💣Siege workshop Level 10</i>\n            └<i>⚒Smithy Level 20</i>\n'
                    return return_message
    if unit_pk is 11:
        castle_level = vill.get_structure_level(tg_id,'castle')
        if castle_level is None or castle_level is 0:
            return_message = ' - Req missing!\n            └<i>🏰Castle level 1</i>\n'
            return return_message
        elif castle_level is 1:
            return_message = '\n'
            return return_message