from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import ProfileDao as profiledao
from dao import ResearchDao as researchdao
from dao import UnitDao as unitdao
from models.village import Village
from models.building import Building
from models.research import Research
from service import VillageService as vill, ProfileService as prof

def generate_research_overview(tg_id):
    village = prof.cur_village_id(tg_id)
    village_name = profiledao.get_cur_village_name(tg_id)
    title = '<b>🔬Research overview 🏯' + village_name + '</b>\n'
    unit_pk = 1
    unit_1 = unitdao.get_unit_name(unit_pk)
    research_1 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_1 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 2
    unit_2 = unitdao.get_unit_name(unit_pk)
    research_2 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_2 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 3
    unit_3 = unitdao.get_unit_name(unit_pk)
    research_3 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_3 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 4
    unit_4 = unitdao.get_unit_name(unit_pk)
    research_4 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_4 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 8
    unit_8 = unitdao.get_unit_name(unit_pk)
    research_8 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_8 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 5
    unit_5 = unitdao.get_unit_name(unit_pk)
    research_5 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_5 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 6
    unit_6 = unitdao.get_unit_name(unit_pk)
    research_6 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_6 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 7
    unit_7 = unitdao.get_unit_name(unit_pk)
    research_7 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_7 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 9
    unit_9 = unitdao.get_unit_name(unit_pk)
    research_9 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_9 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 10
    unit_10 = unitdao.get_unit_name(unit_pk)
    research_10 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_10 = researchdao.get_unit_research(tg_id,unit_pk)
    unit_pk = 11
    unit_11 = unitdao.get_unit_name(unit_pk)
    research_11 = researchdao.research_possible(tg_id, village, unit_pk)
    researched_11 = researchdao.get_unit_research(tg_id,unit_pk)
    return_message = title + researched_1 + ' - 🔱' + unit_1 + research_1 + researched_2 + ' - 🗡' + unit_2 + research_2 \
                     + researched_3 + ' - 🔨' + unit_3 + research_3 + researched_4 + ' - 🏹' + unit_4 + research_4 \
                     + researched_8 + ' - 🏹🐎' + unit_8 + research_8 + researched_5 + ' - 🐁' + unit_5 + research_5 \
                     + researched_6 + ' - 🐎' + unit_6 + research_6 + researched_7 + ' - 🎠' + unit_7 + research_7 \
                     + researched_9 + ' - 🥊' + unit_9 + research_9 + researched_10 + ' - ☄' + unit_10 + research_10 \
                     + researched_11 + ' - 👑' + unit_11 + research_11
    return return_message

def noble_unit(tg_id):
    noble_man = researchdao.noble_pouch_and_recruit_status(tg_id)
    return_message = str(noble_man)
    return return_message

def research_unit(tg_id, unit_pk, session):
    village = prof.cur_village_id(tg_id)
    unit_pk = int(unit_pk)
    village_name = profiledao.get_cur_village_name(tg_id)
    unit = unitdao.get_unit_name(unit_pk)
    researched = researchdao.quick_research_check(tg_id, unit_pk)
    if researched == 'YES':
        return_message = 'You already researched ' + unit + ' in ' + village_name
        return return_message
    else:
        if unit_pk == 1:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 400
            stone_cost = 500
            iron_cost = 500
            research_action = session.query(Research).filter_by(village_pk=village).first()
            barracks_level = vill.get_structure_level(tg_id,'barracks')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level >= 1:
                research_action.spear_man = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level < 1:
                return_message = 'You need ⚔Barracks Level 1'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 2:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 600
            stone_cost = 300
            iron_cost = 450
            barracks_level = vill.get_structure_level(tg_id,'barracks')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level >= 5 and smithy_level >= 1:
                research_action.sword_man = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level < 5 and smithy_level < 1:
                return_message = 'You need ⚔Barracks Level 5 and ⚒Smithy Level 1'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 3:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 500
            stone_cost = 400
            iron_cost = 600
            barracks_level = vill.get_structure_level(tg_id,'barracks')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level >= 3 and smithy_level >= 1:
                research_action.brute = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and barracks_level < 3 and smithy_level < 1:
                return_message = 'You need ⚔Barracks Level 3 and ⚒Smithy Level 1'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 4:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 500
            stone_cost = 400
            iron_cost = 600
            archery_level = vill.get_structure_level(tg_id,'archery')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and archery_level >= 1 and smithy_level >= 1:
                research_action.archer = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and archery_level < 1 and smithy_level < 1:
                return_message = 'You need 🏹Archery Level 1 and ⚒Smithy Level 1'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 8:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 2000
            stone_cost = 1800
            iron_cost = 2400
            archery_level = vill.get_structure_level(tg_id,'archery')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and archery_level >= 10 and smithy_level >= 10:
                research_action.mounted_arch = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and archery_level < 10 and smithy_level < 10:
                return_message = 'You need 🏹Archery Level 10 and ⚒Smithy Level 10'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 5:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 200
            stone_cost = 200
            iron_cost = 250
            stable_level = vill.get_structure_level(tg_id,'stable')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level >= 1 and smithy_level >= 1:
                research_action.scout = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level < 1 and smithy_level < 1:
                return_message = 'You need 🐎Stable Level 1 and ⚒Smithy Level 1'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 6:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 2400
            stone_cost = 2000
            iron_cost = 3000
            stable_level = vill.get_structure_level(tg_id,'stable')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level >= 3 and smithy_level >= 5:
                research_action.light_cav = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level < 3 and smithy_level < 5:
                return_message = 'You need 🐎Stable Level 3 and ⚒Smithy Level 5'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 7:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 3800
            stone_cost = 3600
            iron_cost = 4500
            stable_level = vill.get_structure_level(tg_id,'stable')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level >= 10 and smithy_level >= 15:
                research_action.heavy_cav = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and stable_level < 10 and smithy_level < 15:
                return_message = 'You need 🐎Stable Level 10 and ⚒Smithy Level 15'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 9:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 3000
            stone_cost = 3000
            iron_cost = 3500
            siege_workshop_level = vill.get_structure_level(tg_id,'siege workshop')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and siege_workshop_level >= 3 and smithy_level >= 5:
                research_action.ram = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and siege_workshop_level < 3 and smithy_level < 5:
                return_message = 'You need 💣siege workshop Level 3 and ⚒Smithy Level 5'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 10:
            village_wood = vill.get_wood_storage(tg_id)
            village_stone = vill.get_stone_storage(tg_id)
            village_iron = vill.get_iron_storage(tg_id)
            wood_cost = 5000
            stone_cost = 7000
            iron_cost = 6000
            siege_workshop_level = vill.get_structure_level(tg_id,'siege workshop')
            smithy_level = vill.get_structure_level(tg_id,'smithy')
            paying_resources = session.query(Village).filter_by(pk=village).first()
            research_action = session.query(Research).filter_by(village_pk=village).first()
            if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and siege_workshop_level >= 10 and smithy_level >= 15:
                research_action.catapult = 'YES'
                paying_resources.wood_stock = paying_resources.wood_stock - wood_cost
                paying_resources.stone_stock = paying_resources.stone_stock - stone_cost
                paying_resources.iron_stock = paying_resources.iron_stock - iron_cost
                session.add(paying_resources)
                session.add(research_action)
                session.commit()
                return_message = 'You\'ve researched ' + unit + '!'
                return return_message
            elif village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and siege_workshop_level < 10 and smithy_level < 15:
                return_message = 'You need 💣siege workshop Level 10 and ⚒Smithy Level 15'
                return return_message
            else:
                return_message = 'You don\'t have the resources for this'
                return return_message
        if unit_pk == 11:
            castle_level = vill.get_structure_level(tg_id,'castle')
            if castle_level is None or castle_level == 0:
                return_message = 'You need 🏰castle Level 1 to get this unlock for free!'
                return return_message
            elif castle_level == 1:
                return_message = 'You already have this researched!'
                return return_message