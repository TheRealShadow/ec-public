import random

from telethon import events

import aiocron
from dao import VillageDao as villagedao
from dao import RecruitmentDao as recruitmentdao
from dao import WarDao as wardao
from dao import ProfileDao as profiledao
from plugins import player_notifier_plugin as player_notify
from models.village import Village
from models.troops import Troops
from models.support import Support
from models.reports import Reports
from models.prepare_marching import Prepare_marching
from service import ProfileService as prof, WarService as war, VillageService as vill, TroopsService as troo

session = None

def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/1 * * * *', func=marchings)

async def marchings():
    due_marchings = wardao.get_all_due_marchings(session)
    if due_marchings:
        for due_march in due_marchings:
            if due_march.type_march == 'SUPPORT':
                make_support = Support()
                make_support.owner = due_march.owner_pk
                make_support.from_village_id = due_march.from_village_id
                make_support.in_village_id = due_march.to_village_id
                make_support.slowest_unit_time = due_march.slowest_unit_time
                make_support.spear_man = due_march.spear_man
                make_support.sword_man = due_march.sword_man
                make_support.brute = due_march.brute
                make_support.archer = due_march.archer
                make_support.scout = due_march.scout
                make_support.light_cav = due_march.light_cav
                make_support.heavy_cav = due_march.heavy_cav
                make_support.mounted_arch = due_march.mounted_arch
                make_support.ram = due_march.ram
                make_support.catapult = due_march.catapult
                make_support.noble = due_march.noble
                make_report = Reports()
                make_report.owner = due_march.owner_pk
                make_report.title = '🛡Your troops arrived at ' + villagedao.get_village_name_by_pk(due_march.to_village_id)
                make_report.report = 'Troops are now supporting ' + villagedao.get_village_owner_player_name(due_march.to_village_id) + '\n' + troo.troop_march_overview(due_march.pk)
                make_report.read = 0
                make_report2 = Reports()
                if due_march.target_owner != None:
                    make_report2.owner = due_march.target_owner
                make_report2.title = '🛡Supporting troops arrived at ' + villagedao.get_village_name_by_pk(due_march.to_village_id)
                make_report2.report = 'Troops from ' + villagedao.get_village_owner_player_name(due_march.from_village_id) + ' are now supporting your village ' + villagedao.get_village_name_by_pk(due_march.to_village_id) + '\n' + troo.troop_march_overview(due_march.pk)
                make_report2.read = 0
                session.add(make_report)
                session.add(make_report2)
                session.add(make_support)
                session.delete(due_march)
                session.commit()
            if due_march.type_march == 'RETURN':
                add_march_back_troops = session.query(Troops).filter_by(village_pk=due_march.from_village_id).first()
                add_march_back_troops.spear_man = add_march_back_troops.spear_man + due_march.spear_man
                add_march_back_troops.sword_man = add_march_back_troops.sword_man + due_march.sword_man
                add_march_back_troops.brute = add_march_back_troops.brute + due_march.brute
                add_march_back_troops.archer = add_march_back_troops.archer + due_march.archer
                add_march_back_troops.scout = add_march_back_troops.scout + due_march.scout
                add_march_back_troops.light_cav = add_march_back_troops.light_cav + due_march.light_cav
                add_march_back_troops.heavy_cav = add_march_back_troops.heavy_cav + due_march.heavy_cav
                add_march_back_troops.mounted_arch = add_march_back_troops.mounted_arch + due_march.mounted_arch
                add_march_back_troops.ram = add_march_back_troops.ram + due_march.ram
                add_march_back_troops.catapult = add_march_back_troops.catapult + due_march.catapult
                add_march_back_troops.noble = add_march_back_troops.noble + due_march.noble
                session.add(add_march_back_troops)
                add_march_back_resources = session.query(Village).filter(Village.pk==due_march.from_village_id).first()
                stock_capacity = wardao.get_current_stock_maximum(due_march.from_village_id)
                add_march_back_resources.wood_stock = add_march_back_resources.wood_stock + due_march.looted_wood
                add_march_back_resources.stone_stock = add_march_back_resources.stone_stock + due_march.looted_stone
                add_march_back_resources.iron_stock = add_march_back_resources.iron_stock + due_march.looted_iron
                if add_march_back_resources.wood_stock > stock_capacity:
                    add_march_back_resources.wood_stock = stock_capacity
                if add_march_back_resources.stone_stock > stock_capacity:
                    add_march_back_resources.stone_stock = stock_capacity
                if add_march_back_resources.iron_stock > stock_capacity:
                    add_march_back_resources.iron_stock = stock_capacity
                notify_setting = prof.fetch_player_notify_on_return_by_pk(due_march.owner_pk)
                # if notify_setting == True:
                #     tg_id = profiledao.get_player_tg_id_by_pk(due_march.owner_pk)
                #     message = 'Troops returned in ' + villagedao.get_village_name_by_pk(due_march.from_village_id) + ' /vil' + str(due_march.from_village_id) + '\n' + troo.troop_march_overview(due_march.pk)
                #     await player_notify.notify_possible_reciever(tg_id, message, session)
                #     session.add(add_march_back_resources)
                #     session.delete(due_march)
                #     session.commit()
                if notify_setting == False or notify_setting == True:
                    session.add(add_march_back_resources)
                    session.delete(due_march)
                    session.commit()
            if due_march.type_march == 'ATTACK':
                calculation = war.calculate_war_outcome(due_march, session)
                if calculation == True:
                    session.delete(due_march)
                    session.commit()