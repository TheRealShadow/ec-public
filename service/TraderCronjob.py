import datetime
import math

import aiocron
from dao import VillageDao as villagedao
from dao import RecruitmentDao as recruitmentdao
from dao import TraderDao as traderdao
from dao import MapGenDao as mapgendao
from models.village import Village
from models.troops import Troops
from models.reports import Reports
from service import ProfileService as prof

session = None

def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/1 * * * *', func=give_resources_to_village)

def give_resources_to_village():
    due_trades = traderdao.get_all_due_trades(session)
    if due_trades:
        for trades in due_trades:
            # logic to add that single recruitment to the village
            if trades:
                if trades.type_trade == 'GOING_TO':
                    add_resources_to_village = session.query(Village).filter_by(pk=trades.to_village_id).first()
                    add_resources_to_village.wood_stock = add_resources_to_village.wood_stock + trades.wood
                    add_resources_to_village.stone_stock = add_resources_to_village.stone_stock + trades.stone
                    add_resources_to_village.iron_stock = add_resources_to_village.iron_stock + trades.iron
                    new_report = Reports()
                    new_report.owner = villagedao.get_village_owner_id(trades.to_village_id)
                    new_report.title = '🎭You received resources on ' + villagedao.get_village_name_by_pk(trades.to_village_id)
                    new_report.read = 0
                    if trades.wood > 0:
                        new_report.report = 'You received 🪓' + str(trades.wood) + ' from ' + villagedao.get_village_owner_player_name(trades.from_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.from_village_id)
                    if trades.stone > 0:
                        new_report.report = 'You received ⛏' + str(trades.stone) + ' from ' + villagedao.get_village_owner_player_name(trades.from_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.from_village_id)
                    if trades.iron > 0:
                        new_report.report = 'You received 📏' + str(trades.iron) + ' from ' + villagedao.get_village_owner_player_name(trades.from_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.from_village_id)
                    new_report_two = Reports()
                    new_report_two.owner = villagedao.get_village_owner_id(trades.from_village_id)
                    new_report_two.title = '🎭Your merchants arrived on ' + villagedao.get_village_name_by_pk(trades.to_village_id)
                    new_report_two.read = 0
                    if trades.wood > 0:
                        new_report_two.report = 'Your merchants gave 🪓' + str(trades.wood) + ' to ' + villagedao.get_village_owner_player_name(trades.to_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.to_village_id)
                    if trades.stone > 0:
                        new_report_two.report = 'Your merchants gave ⛏' + str(trades.stone) + ' to ' + villagedao.get_village_owner_player_name(trades.to_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.to_village_id)
                    if trades.iron > 0:
                        new_report_two.report = 'Your merchants gave 📏' + str(trades.iron) + ' to ' + villagedao.get_village_owner_player_name(trades.to_village_id) + ' in the village '  + villagedao.get_village_name_by_pk(trades.to_village_id)
                    trades.type_trade = 'COMING_BACK'
                    trades.wood = 0
                    trades.stone = 0
                    trades.iron = 0
                    walk_time_in_seconds = 240
                    distance = mapgendao.calculate_village_distance_by_2_pk(trades.from_village_id, trades.to_village_id)
                    trades.arrival_time = trades.arrival_time + datetime.timedelta(seconds=int(distance*walk_time_in_seconds))
                    session.add(trades)
                    session.add(add_resources_to_village)
                    session.add(new_report)
                    session.add(new_report_two)
                    session.commit()
                elif trades.type_trade == 'COMING_BACK':
                    session.delete(trades)
                    session.commit()