import itertools
import re

from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import ProfileDao as profiledao
from dao import ResearchDao as researchdao
from dao import UnitDao as unitdao
from dao import RecruitmentDao as recruitmentdao
from models.player import Player
from models.village import Village
from models.building import Building
from models.research import Research
from models.recruitment import Recruitment
from service import VillageService as vill, ProfileService as prof
import datetime

def set_recruitment_now(tg_id, unit_pk, session):
    village_id = profiledao.get_cur_village_id(tg_id)
    barracks = [1, 2, 3]
    archery = [4, 8]
    stable = [5, 6, 7]
    siege_workshop = [9, 10]
    unit_pk = int(unit_pk)
    unit_max = int(unitdao.get_unit_max(tg_id, unit_pk))
    if unit_pk in barracks:
        structure = 'barracks'
        building_id = buildingdao.get_structure_id(structure)
        possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
        unit_name = unitdao.get_unit_name(unit_pk)
        if possible_queue and unit_max >= 1:
            latest_build_time = possible_queue.finish_time
            unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif possible_queue is None and unit_max >= 1:
            current_time = datetime.datetime.utcnow()
            unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif  unit_max < 1:
            return_message = 'You don\'t have enough resources!'
            return return_message
    elif unit_pk in archery:
        structure = 'archery'
        building_id = buildingdao.get_structure_id(structure)
        possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
        unit_name = unitdao.get_unit_name(unit_pk)
        if possible_queue and unit_max >= 1:
            latest_build_time = possible_queue.finish_time
            unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif possible_queue is None and unit_max >= 1:
            current_time = datetime.datetime.utcnow()
            unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif  unit_max < 1:
            return_message = 'You don\'t have enough resources!'
            return return_message
    elif unit_pk in stable:
        structure = 'stable'
        building_id = buildingdao.get_structure_id(structure)
        possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
        unit_name = unitdao.get_unit_name(unit_pk)
        if possible_queue and unit_max >= 1:
            latest_build_time = possible_queue.finish_time
            unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif possible_queue is None and unit_max >= 1:
            current_time = datetime.datetime.utcnow()
            unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif  unit_max < 1:
            return_message = 'You don\'t have enough resources!'
            return return_message
    elif unit_pk in siege_workshop:
        structure = 'siege workshop'
        building_id = buildingdao.get_structure_id(structure)
        possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
        unit_name = unitdao.get_unit_name(unit_pk)
        if possible_queue and unit_max >= 1:
            latest_build_time = possible_queue.finish_time
            unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif possible_queue is None and unit_max >= 1:
            current_time = datetime.datetime.utcnow()
            unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif  unit_max < 1:
            return_message = 'You don\'t have enough resources!'
            return return_message
    elif unit_pk is 11:
        structure = 'castle'
        building_id = buildingdao.get_structure_id(structure)
        possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
        unit_name = unitdao.get_unit_name(unit_pk)
        if possible_queue and unit_max >= 1:
            latest_build_time = possible_queue.finish_time
            unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif possible_queue is None and unit_max >= 1:
            current_time = datetime.datetime.utcnow()
            unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
            new_recruitment = Recruitment()
            new_recruitment.village_id = village_id
            new_recruitment.finish_time = unit_end_time
            new_recruitment.unit_id = unit_pk
            new_recruitment.building_id = building_id
            pay_resources = session.query(Village).filter_by(pk=village_id).first()
            pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
            pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
            pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
            session.add(pay_resources)
            session.add(new_recruitment)
            session.commit()
            return_message = 'Recruitment on ' + unit_name + ' has started'
            return return_message
        elif  unit_max < 1:
            return_message = 'You don\'t have enough resources!'
            return return_message
    else:
        return_message = 'Something went wrong...'
        return return_message

def generate_a_pouch(tg_id, session):
    village_id = prof.cur_village_id(tg_id)
    castle_level = vill.get_structure_level(tg_id,'castle')
    village_wood = villagedao.get_wood_storage(tg_id)
    village_stone = villagedao.get_stone_storage(tg_id)
    village_iron = villagedao.get_iron_storage(tg_id)
    wood_cost = 28000
    stone_cost = 30000
    iron_cost = 25000
    if village_wood >= wood_cost and village_stone >= stone_cost and village_iron >= iron_cost and castle_level == 1:
        add_a_pouch = session.query(Player).filter_by(tg_id=tg_id).first()
        add_a_pouch.pouches = add_a_pouch.pouches + 1
        pay_resources = session.query(Village).filter_by(pk=village_id).first()
        pay_resources.wood_stock = pay_resources.wood_stock - wood_cost
        pay_resources.stone_stock = pay_resources.stone_stock - stone_cost
        pay_resources.iron_stock = pay_resources.iron_stock - iron_cost
        session.add(pay_resources)
        session.add(add_a_pouch)
        session.commit()
        return_message = 'You created a pouch!'
        return return_message
    elif castle_level is None or castle_level is 0:
        return_message = 'You don\'t have a castle in your current village.'
        return return_message
    else:
        return_message = 'You don\'t have enough resources\n A pouch costs: 🪓28000 ⛏30000 📏25000'
        return return_message


def set_recruitment_now_loop(tg_id, unit_pk, amount, session):
    village_id = profiledao.get_cur_village_id(tg_id)
    barracks = [1, 2, 3]
    archery = [4, 8]
    stable = [5, 6, 7]
    siege_workshop = [9, 10]
    castle = [11]
    unit_pk = int(unit_pk)
    amount = int(amount)
    unit_name = unitdao.get_unit_name(unit_pk)
    unit_max = int(unitdao.get_unit_max(tg_id, unit_pk))
    if unit_max is None or unit_max is 0:
        return_message = 'You can\'t recruit!'
        return return_message
    elif unit_max >= amount:
        count = 0
        amount = amount-1
        while (count <= amount):
            if unit_pk in barracks:
                structure = 'barracks'
                building_id = buildingdao.get_structure_id(structure)
                possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
                if possible_queue:
                    latest_build_time = possible_queue.finish_time
                    unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
                elif possible_queue is None:
                    current_time = datetime.datetime.utcnow()
                    unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
            elif unit_pk in archery:
                structure = 'archery'
                building_id = buildingdao.get_structure_id(structure)
                possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
                if possible_queue:
                    latest_build_time = possible_queue.finish_time
                    unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
                elif possible_queue is None:
                    current_time = datetime.datetime.utcnow()
                    unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
            elif unit_pk in stable:
                structure = 'stable'
                building_id = buildingdao.get_structure_id(structure)
                possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
                if possible_queue:
                    latest_build_time = possible_queue.finish_time
                    unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
                elif possible_queue is None:
                    current_time = datetime.datetime.utcnow()
                    unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
            elif unit_pk in siege_workshop:
                structure = 'siege workshop'
                building_id = buildingdao.get_structure_id(structure)
                possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
                if possible_queue:
                    latest_build_time = possible_queue.finish_time
                    unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
                elif possible_queue is None:
                    current_time = datetime.datetime.utcnow()
                    unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
            elif unit_pk in castle:
                structure = 'castle'
                building_id = buildingdao.get_structure_id(structure)
                possible_queue = session.query(Recruitment).filter(Recruitment.building_id==building_id).filter(Recruitment.village_id==village_id).order_by(Recruitment.finish_time.desc()).first()
                if possible_queue:
                    latest_build_time = possible_queue.finish_time
                    unit_end_time = latest_build_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
                elif possible_queue is None:
                    current_time = datetime.datetime.utcnow()
                    unit_end_time = current_time + datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * recruitmentdao.get_unit_production_bonus(tg_id, structure))
                    new_recruitment = Recruitment()
                    new_recruitment.village_id = village_id
                    new_recruitment.finish_time = unit_end_time
                    new_recruitment.unit_id = unit_pk
                    new_recruitment.building_id = building_id
                    pay_resources = session.query(Village).filter_by(pk=village_id).first()
                    pay_resources.wood_stock = pay_resources.wood_stock - unitdao.get_unit_wood(unit_pk)
                    pay_resources.stone_stock = pay_resources.stone_stock - unitdao.get_unit_stone(unit_pk)
                    pay_resources.iron_stock = pay_resources.iron_stock - unitdao.get_unit_iron(unit_pk)
                    session.add(pay_resources)
                    session.add(new_recruitment)
                    session.commit()
                    count = count + 1
        return_message = 'Recruitment on ' + str(amount +1) + ' ' + unit_name + ' has started'
        return return_message
    elif unit_max < amount:
        return_message = 'You don\'t have enough resources for so many ' + unit_name + '!'
        return return_message
    else:
        return_message = 'Something went wrong...'
        return return_message

def get_current_unit_queue(tg_id, session):
    village_id = prof.cur_village_id(tg_id)
    recruitlist = []
    unit1 = recruitmentdao.que_for_unit(village_id,1)
    unit2 = recruitmentdao.que_for_unit(village_id,2)
    unit3 = recruitmentdao.que_for_unit(village_id,3)
    unit4 = recruitmentdao.que_for_unit(village_id,4)
    unit5 = recruitmentdao.que_for_unit(village_id,5)
    unit6 = recruitmentdao.que_for_unit(village_id,6)
    unit7 = recruitmentdao.que_for_unit(village_id,7)
    unit8 = recruitmentdao.que_for_unit(village_id,8)
    unit9 = recruitmentdao.que_for_unit(village_id,9)
    unit10 = recruitmentdao.que_for_unit(village_id,10)
    unit11 = recruitmentdao.que_for_unit(village_id,11)
    recruitlist.append(unit1)
    recruitlist.append(unit2)
    recruitlist.append(unit3)
    recruitlist.append(unit4)
    recruitlist.append(unit5)
    recruitlist.append(unit6)
    recruitlist.append(unit7)
    recruitlist.append(unit8)
    recruitlist.append(unit9)
    recruitlist.append(unit10)
    recruitlist.append(unit11)
    filter_recruitlist = []
    for value in recruitlist:
        if value != 0:
            filter_recruitlist.append(value)
    if not filter_recruitlist:
        return_message = 'None'
        return return_message
    return_message = '\n'.join(filter_recruitlist)
    return return_message