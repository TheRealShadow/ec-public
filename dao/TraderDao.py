import datetime
import math

from sqlalchemy import or_, func

from dao import UnitDao as unitdao
from dao import ProfileDao as profiledao
from dao import MapGenDao as mapgendao
from dao import VillageDao as villagedao
from service import VillageService as vill, ProfileService as prof
from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.recruitment import Recruitment
from models.unit import Unit
from models.trading import Trading
from models.structure_resource_production import Structure_Resource_Production

session = None

def init(global_session):
    global session
    session = global_session

def pve_trader(tg_id, give_resource, give_amount, receive_resource, session):
    village_pk = profiledao.get_cur_village_id(tg_id)
    give_amount = int(give_amount)
    current_wood = int(vill.get_wood_storage(tg_id))
    current_stone = int(vill.get_stone_storage(tg_id))
    current_iron = int(vill.get_iron_storage(tg_id))
    market_level = vill.get_structure_level(tg_id, 'market')
    give_resource = give_resource.lower()
    receive_resource = receive_resource.lower()
    if market_level >= 5:
        resource_change = session.query(Village).filter_by(pk=village_pk).first()
        if give_resource == 'wood' and receive_resource == 'wood':
            return_message = 'You can\'t trade the same resources!'
            return return_message
        elif give_resource == 'stone' and receive_resource == 'stone':
            return_message = 'You can\'t trade the same resources!'
            return return_message
        elif give_resource == 'iron' and receive_resource == 'iron':
            return_message = 'You can\'t trade the same resources!'
            return return_message
        elif give_resource == 'wood' and current_wood >= give_amount and receive_resource == 'stone':
            resource_change.wood_stock = resource_change.wood_stock - give_amount
            resource_change.stone_stock = int(resource_change.stone_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        elif give_resource == 'wood' and current_wood >= give_amount and receive_resource == 'iron':
            resource_change.wood_stock = resource_change.wood_stock - give_amount
            resource_change.iron_stock = int(resource_change.iron_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        elif give_resource == 'stone' and current_stone >= give_amount and receive_resource == 'iron':
            resource_change.stone_stock = resource_change.stone_stock - give_amount
            resource_change.iron_stock = int(resource_change.iron_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        elif give_resource == 'stone' and current_stone >= give_amount and receive_resource == 'wood':
            resource_change.stone_stock = resource_change.stone_stock - give_amount
            resource_change.wood_stock = int(resource_change.wood_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        elif give_resource == 'iron' and current_iron >= give_amount and receive_resource == 'wood':
            resource_change.iron_stock = resource_change.iron_stock - give_amount
            resource_change.wood_stock = int(resource_change.wood_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        elif give_resource == 'iron' and current_iron >= give_amount and receive_resource == 'stone':
            resource_change.iron_stock = resource_change.iron_stock - give_amount
            resource_change.stone_stock = int(resource_change.stone_stock) + int((give_amount/2))
            session.add(resource_change)
            session.commit()
            return_message = 'You traded ' + str(give_amount) + ' ' + str(give_resource) + ' for ' + str(int(give_amount/2)) + ' ' + receive_resource
            return return_message
        else:
            return_message = 'I don\'t know what you tried... But it ain\'t right.'
            return return_message
    elif market_level < 5 or market_level is None:
        return_message = 'Your market isn\'t level 5 or higher! Try again once your market has the right requirements.'
        return return_message

def trader_display(tg_id, session):
    maximum = get_trader_amount(tg_id)
    walking_around = traders_walking(tg_id, session)
    can_trade = int(maximum) - int(walking_around)
    return_message = str(can_trade) + '/' + str(maximum)
    return return_message

def free_traders(tg_id, session):
    maximum = get_trader_amount(tg_id)
    walking_around = traders_walking(tg_id, session)
    can_trade = int(maximum) - int(walking_around)
    return can_trade

def traders_walking(tg_id, session):
    owner = prof.cur_player_id(tg_id)
    village_id = prof.cur_village_id(tg_id)
    total = 0
    trades = session.query(Trading).filter_by(owner=owner).filter_by(from_village_id=village_id).all()
    for trade in trades:
        total = total + trade.traders
    merchants_used = total
    return merchants_used

def get_all_due_trades(session):
    trades = session.query(Trading).filter(Trading.arrival_time < datetime.datetime.utcnow()).all()
    if trades:
        return trades

def get_trader_amount(tg_id):
    structure = 'market'
    level = vill.get_structure_level(tg_id, structure)
    if level is None or level is 0:
        traders = '0'
        return traders
    elif level is 1:
        traders = 1
        return traders
    elif level is 2:
        traders = 2
        return traders
    elif level is 3:
        traders = 3
        return traders
    elif level is 4:
        traders = 4
        return traders
    elif level is 5:
        traders = 5
        return traders
    elif level is 6:
        traders = 6
        return traders
    elif level is 7:
        traders = 7
        return traders
    elif level is 8:
        traders = 8
        return traders
    elif level is 9:
        traders = 9
        return traders
    elif level is 10:
        traders = 10
        return traders
    elif level is 11:
        traders = 13
        return traders
    elif level is 12:
        traders = 17
        return traders
    elif level is 13:
        traders = 20
        return traders
    elif level is 14:
        traders = 28
        return traders
    elif level is 15:
        traders = 36
        return traders
    elif level is 16:
        traders = 45
        return traders
    elif level is 17:
        traders = 56
        return traders
    elif level is 18:
        traders = 77
        return traders
    elif level is 19:
        traders = 99
        return traders
    elif level is 20:
        traders = 120
        return traders
    elif level is 21:
        traders = 140
        return traders
    elif level is 22:
        traders = 165
        return traders
    elif level is 23:
        traders = 180
        return traders
    elif level is 24:
        traders = 230
        return traders
    elif level is 25:
        traders = 250
        return traders

def set_trade_now(tg_id, towards_village, give_resource, give_amount, session):
    player_pk = prof.cur_player_id(tg_id)
    give_amount = int(give_amount)
    village_id = profiledao.get_cur_village_id(tg_id)
    village_name = villagedao.get_village_name_by_pk(towards_village)
    wood_stock = int(vill.get_wood_storage(tg_id))
    stone_stock = int(vill.get_stone_storage(tg_id))
    iron_stock = int(vill.get_iron_storage(tg_id))
    distance = mapgendao.calculate_village_distance(tg_id,towards_village)
    walk_time_in_seconds = 240
    current_time = datetime.datetime.utcnow()
    available_traders = free_traders(tg_id, session)
    if village_id != towards_village:
        if available_traders > 0:
            if give_amount <= int(available_traders*1000):
                if give_resource == 'wood':
                    if int(wood_stock) >= int(give_amount):
                        arrival_time = current_time + datetime.timedelta(seconds=int(distance*walk_time_in_seconds))
                        new_trade = Trading()
                        new_trade.owner = player_pk
                        new_trade.from_village_id = village_id
                        new_trade.to_village_id = towards_village
                        new_trade.arrival_time = arrival_time
                        new_trade.wood = give_amount
                        new_trade.stone = 0
                        new_trade.iron = 0
                        new_trade.traders = math.ceil(give_amount / 1000)
                        new_trade.type_trade = 'GOING_TO'
                        pay_resources = session.query(Village).filter_by(pk=village_id).first()
                        pay_resources.wood_stock = pay_resources.wood_stock - give_amount
                        session.add(new_trade)
                        session.add(pay_resources)
                        session.commit()
                        return_message = 'Sending ' + str(int(give_amount)) + ' ' + str(give_resource) + ' towards ' + str(village_name) + '.\nArrival time: ' + str(arrival_time)
                        return return_message
                    else:
                        return 'You can\'t send more than you have!'
                if give_resource == 'stone':
                    if int(stone_stock) >= int(give_amount):
                        arrival_time = current_time + datetime.timedelta(seconds=int(distance*walk_time_in_seconds))
                        new_trade = Trading()
                        new_trade.owner = player_pk
                        new_trade.from_village_id = village_id
                        new_trade.to_village_id = towards_village
                        new_trade.arrival_time = arrival_time
                        new_trade.stone = give_amount
                        new_trade.wood = 0
                        new_trade.iron = 0
                        new_trade.traders = math.ceil(give_amount / 1000)
                        new_trade.type_trade = 'GOING_TO'
                        pay_resources = session.query(Village).filter_by(pk=village_id).first()
                        pay_resources.stone_stock = pay_resources.stone_stock - give_amount
                        session.add(new_trade)
                        session.add(pay_resources)
                        session.commit()
                        return_message = 'Sending ' + str(int(give_amount)) + ' ' + str(give_resource) + ' towards ' + str(village_name) + '.\nArrival time: ' + str(arrival_time)
                        return return_message
                    else:
                        return 'You can\'t send more than you have!'
                if give_resource == 'iron':
                    if int(iron_stock) >= int(give_amount):
                        arrival_time = current_time + datetime.timedelta(seconds=int(distance*walk_time_in_seconds))
                        new_trade = Trading()
                        new_trade.owner = player_pk
                        new_trade.from_village_id = village_id
                        new_trade.to_village_id = towards_village
                        new_trade.arrival_time = arrival_time
                        new_trade.iron = give_amount
                        new_trade.stone = 0
                        new_trade.wood = 0
                        new_trade.traders = math.ceil(give_amount / 1000)
                        new_trade.type_trade = 'GOING_TO'
                        pay_resources = session.query(Village).filter_by(pk=village_id).first()
                        pay_resources.iron_stock = pay_resources.iron_stock - give_amount
                        session.add(new_trade)
                        session.add(pay_resources)
                        session.commit()
                        return_message = 'Sending ' + str(int(give_amount)) + ' ' + str(give_resource) + ' towards ' + str(village_name) + '.\nArrival time: ' + str(arrival_time)
                        return return_message
                    else:
                        return 'You can\'t send more than you have!'
                else:
                    return 'You did something wrong, try again.'
            else:
                return 'Trying to send more than a trader can carry? How cruel...'
        else:
            return 'Trying to send resources without a trader? You maniac!'
    else:
        return 'You can\'t send resources to the village you also have selected!'