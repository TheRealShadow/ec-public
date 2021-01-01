import datetime

from sqlalchemy import or_, func

from dao import UnitDao as unitdao
from service import VillageService as vill
from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.recruitment import Recruitment
from models.unit import Unit
from models.structure_resource_production import Structure_Resource_Production

session = None

def init(global_session):
    global session
    session = global_session

def get_all_unit_id():
    unit_ids = session.query(Unit.pk).all()
    if unit_ids:
        return unit_ids

def get_all_due_recruitments():
    recruitment = session.query(Recruitment).filter(Recruitment.finish_time < datetime.datetime.utcnow()).all()
    if recruitment:
        return recruitment

def que_for_unit(village_pk, unit_pk):
    for amount in session.query(func.count(Recruitment.unit_id)).filter(Recruitment.village_id == village_pk).filter(Recruitment.unit_id == unit_pk).all():
        if amount is None:
            return
        elif amount:
            amount = str(amount).strip('(,)')
            amount = int(amount)
            if amount is None or amount is 0:
                amount = 0
                return amount
            elif amount > 0:
                if amount and unit_pk is 1:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🔱 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 2:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🗡 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 3:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🔨 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 4:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🏹 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 5:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🐁 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 6:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🐎 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 7:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🎠 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 8:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🐎🏹 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 9:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '🥊 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 10:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '☄ ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message
                elif amount and unit_pk is 11:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = '👑 ' + str(amount).strip('(,)') + ' | UTC - ' + str(end_time)
                    return return_message

def que_for_unit_clean(village_pk, unit_pk):
    for amount in session.query(func.count(Recruitment.unit_id)).filter(Recruitment.village_id == village_pk).filter(Recruitment.unit_id == unit_pk).all():
        if amount is None:
            return
        elif amount:
            amount = str(amount).strip('(,)')
            amount = int(amount)
            if amount is None or amount is 0:
                amount = 0
                return amount
            elif amount > 0:
                if amount and unit_pk is 1:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 2:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 3:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 4:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 5:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 6:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 7:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 8:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 9:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 10:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message
                elif amount and unit_pk is 11:
                    end_time = get_end_time_of_query_for_unit(village_pk, unit_pk)
                    return_message = str(amount).strip('(,)')
                    return return_message

def get_end_time_of_query_for_unit(village_pk, unit_pk):
    for queue_end_time in session.query(Recruitment.finish_time).filter(Recruitment.village_id == village_pk).filter(Recruitment.unit_id == unit_pk).order_by(Recruitment.finish_time.desc()).first():
        if queue_end_time:
            return queue_end_time

def get_unit_production_bonus(tg_id, structure):
    if structure == 'barracks':
        level = vill.get_structure_level(tg_id, structure)
        if level is None or level is 0:
            production_speed = '⁉-100%'
            return production_speed
        elif level is 1:
            production_speed = 60
            return production_speed
        elif level is 2:
            production_speed = 57
            return production_speed
        elif level is 3:
            production_speed = 55
            return production_speed
        elif level is 4:
            production_speed = 54
            return production_speed
        elif level is 5:
            production_speed = 53
            return production_speed
        elif level is 6:
            production_speed = 50
            return production_speed
        elif level is 7:
            production_speed = 48
            return production_speed
        elif level is 8:
            production_speed = 47
            return production_speed
        elif level is 9:
            production_speed = 45
            return production_speed
        elif level is 10:
            production_speed = 42
            return production_speed
        elif level is 11:
            production_speed = 39
            return production_speed
        elif level is 12:
            production_speed = 36
            return production_speed
        elif level is 13:
            production_speed = 33
            return production_speed
        elif level is 14:
            production_speed = 32
            return production_speed
        elif level is 15:
            production_speed = 31
            return production_speed
        elif level is 16:
            production_speed = 30
            return production_speed
        elif level is 17:
            production_speed = 28
            return production_speed
        elif level is 18:
            production_speed = 25
            return production_speed
        elif level is 19:
            production_speed = 23
            return production_speed
        elif level is 20:
            production_speed = 20
            return production_speed
        elif level is 21:
            production_speed = 20
            return production_speed
        elif level is 22:
            production_speed = 18
            return production_speed
        elif level is 23:
            production_speed = 17
            return production_speed
        elif level is 24:
            production_speed = 15
            return production_speed
        elif level is 25:
            production_speed = 14
            return production_speed
    if structure == 'archery':
        level = vill.get_structure_level(tg_id, structure)
        if level is None or level is 0:
            production_speed = '⁉-100%'
            return production_speed
        elif level is 1:
            production_speed = 60
            return production_speed
        elif level is 2:
            production_speed = 57
            return production_speed
        elif level is 3:
            production_speed = 55
            return production_speed
        elif level is 4:
            production_speed = 54
            return production_speed
        elif level is 5:
            production_speed = 53
            return production_speed
        elif level is 6:
            production_speed = 50
            return production_speed
        elif level is 7:
            production_speed = 48
            return production_speed
        elif level is 8:
            production_speed = 47
            return production_speed
        elif level is 9:
            production_speed = 45
            return production_speed
        elif level is 10:
            production_speed = 42
            return production_speed
        elif level is 11:
            production_speed = 39
            return production_speed
        elif level is 12:
            production_speed = 36
            return production_speed
        elif level is 13:
            production_speed = 33
            return production_speed
        elif level is 14:
            production_speed = 32
            return production_speed
        elif level is 15:
            production_speed = 31
            return production_speed
        elif level is 16:
            production_speed = 30
            return production_speed
        elif level is 17:
            production_speed = 28
            return production_speed
        elif level is 18:
            production_speed = 25
            return production_speed
        elif level is 19:
            production_speed = 23
            return production_speed
        elif level is 20:
            production_speed = 20
            return production_speed
    if structure == 'stable':
        level = vill.get_structure_level(tg_id, structure)
        if level is None or level is 0:
            production_speed = '⁉-100%'
            return production_speed
        elif level is 1:
            production_speed = 60
            return production_speed
        elif level is 2:
            production_speed = 57
            return production_speed
        elif level is 3:
            production_speed = 55
            return production_speed
        elif level is 4:
            production_speed = 54
            return production_speed
        elif level is 5:
            production_speed = 53
            return production_speed
        elif level is 6:
            production_speed = 50
            return production_speed
        elif level is 7:
            production_speed = 48
            return production_speed
        elif level is 8:
            production_speed = 47
            return production_speed
        elif level is 9:
            production_speed = 45
            return production_speed
        elif level is 10:
            production_speed = 42
            return production_speed
        elif level is 11:
            production_speed = 39
            return production_speed
        elif level is 12:
            production_speed = 36
            return production_speed
        elif level is 13:
            production_speed = 33
            return production_speed
        elif level is 14:
            production_speed = 32
            return production_speed
        elif level is 15:
            production_speed = 31
            return production_speed
        elif level is 16:
            production_speed = 30
            return production_speed
        elif level is 17:
            production_speed = 28
            return production_speed
        elif level is 18:
            production_speed = 25
            return production_speed
        elif level is 19:
            production_speed = 23
            return production_speed
        elif level is 20:
            production_speed = 20
            return production_speed
    if structure == 'siege workshop':
        level = vill.get_structure_level(tg_id, structure)
        if level is None or level is 0:
            production_speed = '⁉-100%'
            return production_speed
        elif level is 1:
            production_speed = 60
            return production_speed
        elif level is 2:
            production_speed = 57
            return production_speed
        elif level is 3:
            production_speed = 55
            return production_speed
        elif level is 4:
            production_speed = 54
            return production_speed
        elif level is 5:
            production_speed = 53
            return production_speed
        elif level is 6:
            production_speed = 50
            return production_speed
        elif level is 7:
            production_speed = 48
            return production_speed
        elif level is 8:
            production_speed = 47
            return production_speed
        elif level is 9:
            production_speed = 45
            return production_speed
        elif level is 10:
            production_speed = 42
            return production_speed
        elif level is 11:
            production_speed = 39
            return production_speed
        elif level is 12:
            production_speed = 36
            return production_speed
        elif level is 13:
            production_speed = 33
            return production_speed
        elif level is 14:
            production_speed = 32
            return production_speed
        elif level is 15:
            production_speed = 31
            return production_speed
    if structure == 'castle':
        level = vill.get_structure_level(tg_id, structure)
        if level is None or level is 0:
            production_speed = '⁉-100%'
            return production_speed
        elif level is 1:
            production_speed = 60
            return production_speed

def get_building_units(tg_id, structure):
    if vill.get_structure_level(tg_id, structure) >= 1 and structure == 'barracks':
        unit_pk = 1
        unit_1_name = unitdao.get_unit_name(unit_pk)
        unit_1_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_1_rec_time = '⏳' + str(str(unit_1_time).split(".")[0])
        unit_1_view = unitdao.get_unit_view(unit_pk)
        unit_1_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_1_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 2
        unit_2_name = unitdao.get_unit_name(unit_pk)
        unit_2_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_2_rec_time = '⏳' + str(str(unit_2_time).split(".")[0])
        unit_2_view = unitdao.get_unit_view(unit_pk)
        unit_2_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_2_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 3
        unit_3_name = unitdao.get_unit_name(unit_pk)
        unit_3_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_3_rec_time = '⏳' + str(str(unit_3_time).split(".")[0])
        unit_3_view = unitdao.get_unit_view(unit_pk)
        unit_3_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_3_max = unitdao.get_unit_max(tg_id, unit_pk)
        return_message = '<code>1</code> 🔱' + str(unit_1_name) + str(unit_1_rec_time) + ' 📈' + str(unit_1_max) + ' ' + str(unit_1_view) + ' ' + str(unit_1_research) + '\n' \
                         '<code>2</code> 🗡' + str(unit_2_name) + str(unit_2_rec_time) + ' 📈' + str(unit_2_max) + ' ' + str(unit_2_view) + ' ' + str(unit_2_research) + '\n' \
                         '<code>3</code> 🔨' + str(unit_3_name) + str(unit_3_rec_time) + ' 📈' + str(unit_3_max) + ' ' + str(unit_3_view) + ' ' + str(unit_3_research) + '\n'
        return return_message
    elif vill.get_structure_level(tg_id, structure) >= 1 and structure == 'archery':
        unit_pk = 4
        unit_1_name = unitdao.get_unit_name(unit_pk)
        unit_1_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_1_rec_time = '⏳' + str(str(unit_1_time).split(".")[0])
        unit_1_view = unitdao.get_unit_view(unit_pk)
        unit_1_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_1_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 8
        unit_2_name = unitdao.get_unit_name(unit_pk)
        unit_2_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_2_rec_time = '⏳' + str(str(unit_2_time).split(".")[0])
        unit_2_view = unitdao.get_unit_view(unit_pk)
        unit_2_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_2_max = unitdao.get_unit_max(tg_id, unit_pk)
        return_message = '<code>4</code> 🏹' + str(unit_1_name) + str(unit_1_rec_time) + ' 📈' + str(unit_1_max) + ' ' + str(unit_1_view) + ' ' + str(unit_1_research) + '\n' \
                         '<code>8</code> 🐎🏹' + str(unit_2_name) + str(unit_2_rec_time) + ' 📈' + str(unit_2_max) + ' ' + str(unit_2_view) + ' ' + str(unit_2_research) + '\n'
        return return_message
    elif vill.get_structure_level(tg_id, structure) >= 1 and structure == 'stable':
        unit_pk = 5
        unit_1_name = unitdao.get_unit_name(unit_pk)
        unit_1_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_1_rec_time = '⏳' + str(str(unit_1_time).split(".")[0])
        unit_1_view = unitdao.get_unit_view(unit_pk)
        unit_1_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_1_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 6
        unit_2_name = unitdao.get_unit_name(unit_pk)
        unit_2_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_2_rec_time = '⏳' + str(str(unit_2_time).split(".")[0])
        unit_2_view = unitdao.get_unit_view(unit_pk)
        unit_2_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_2_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 7
        unit_3_name = unitdao.get_unit_name(unit_pk)
        unit_3_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_3_rec_time = '⏳' + str(str(unit_3_time).split(".")[0])
        unit_3_view = unitdao.get_unit_view(unit_pk)
        unit_3_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_3_max = unitdao.get_unit_max(tg_id, unit_pk)
        return_message = '<code>5</code> 🐁' + str(unit_1_name) + str(unit_1_rec_time) + ' 📈' + str(unit_1_max) + ' ' + str(unit_1_view) + ' ' + str(unit_1_research) + '\n' \
                         '<code>6</code> 🐎' + str(unit_2_name) + str(unit_2_rec_time) + ' 📈' + str(unit_2_max) + ' ' + str(unit_2_view) + ' ' + str(unit_2_research) + '\n' \
                         '<code>7</code> 🎠' + str(unit_3_name) + str(unit_3_rec_time) + ' 📈' + str(unit_3_max) + ' ' + str(unit_3_view) + ' ' + str(unit_3_research) + '\n'
        return return_message
    elif vill.get_structure_level(tg_id, structure) >= 1 and structure == 'siege workshop':
        unit_pk = 9
        unit_1_name = unitdao.get_unit_name(unit_pk)
        unit_1_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_1_rec_time = '⏳' + str(str(unit_1_time).split(".")[0])
        unit_1_view = unitdao.get_unit_view(unit_pk)
        unit_1_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_1_max = unitdao.get_unit_max(tg_id, unit_pk)
        unit_pk = 10
        unit_2_name = unitdao.get_unit_name(unit_pk)
        unit_2_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_2_rec_time = '⏳' + str(str(unit_2_time).split(".")[0])
        unit_2_view = unitdao.get_unit_view(unit_pk)
        unit_2_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_2_max = unitdao.get_unit_max(tg_id, unit_pk)
        return_message = '<code>9</code> 🥊' + str(unit_1_name) + str(unit_1_rec_time) + ' 📈' + str(unit_1_max) + ' ' + str(unit_1_view) + ' ' + str(unit_1_research) + '\n' \
                         '<code>10</code> ☄' + str(unit_2_name) + str(unit_2_rec_time) + ' 📈' + str(unit_2_max) + ' ' + str(unit_2_view) + ' ' + str(unit_2_research) + '\n'
        return return_message
    elif vill.get_structure_level(tg_id, structure) >= 1 and structure == 'castle':
        unit_pk = 11
        unit_1_name = unitdao.get_unit_name(unit_pk)
        unit_1_time = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_pk) / int(100) * get_unit_production_bonus(tg_id,structure)))
        unit_1_rec_time = '⏳' + str(str(unit_1_time).split(".")[0])
        unit_1_view = unitdao.get_unit_view(unit_pk)
        unit_1_research = unitdao.get_unit_research(tg_id,unit_pk)
        unit_1_max = unitdao.get_unit_max(tg_id, unit_pk)
        return_message = '<code>11</code> 👑' + str(unit_1_name) + str(unit_1_rec_time) + ' 📈' + str(unit_1_max) + ' ' + str(unit_1_view) + ' ' + str(unit_1_research) + '\n'
        return return_message
    else:
        return_message = 'Recruitment unavailable.\n'
        return return_message