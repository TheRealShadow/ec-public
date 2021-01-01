import random

from telethon import events
from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from dao import ProfileDao as profiledao
from dao import ResearchDao as researchdao
from dao import UnitDao as unitdao
from dao import WarDao as wardao
from dao import MapGenDao as mapgendao
from models.player import Player
from models.village import Village
from models.building import Building
from models.research import Research
from models.marching import Marching
from models.prepare_marching import Prepare_marching
from models.unit import Unit
from models.troops import Troops
from models.support import Support
from models.reports import Reports
from models.recruitment import Recruitment
from service import VillageService as vill, ProfileService as prof, TroopsService as troo
from plugins import player_notifier_plugin as player_notify

def generate_prepare_marching_overview(tg_id):
    target_village = prof.cur_march_village_id(tg_id)
    if target_village == None:
        return 'You don\'t have a target selected. Select a target first.'
    target_name = villagedao.get_village_name_by_pk(target_village)
    own_village_alert = wardao.attack_on_own_alert(tg_id, target_village)
    current_village = prof.cur_village_id(tg_id)
    current_village_troops = troo.village_overview_prepare_march(current_village)
    selected_village_troops = troo.village_overview_prepare_march_selected(current_village)
    ETA = wardao.calculate_eta_on_slowest_unit(current_village, target_village)
    if target_village != current_village:
        message = [str(own_village_alert) ,'Which troops do you want to send towards ', str(target_name), ' (ID: ', str(target_village), ')?\n<i>To add multiple troops at once: /add_id amount or /add_all.\nTo reset all selected units use /reset.\n</i>', current_village_troops, '\n\n<b>Selected:</b>\n', selected_village_troops, ETA ,'\n\n/send_attack or /send_support']
        return ''.join(message)
    else:
        return 'You can\'t attack nor support the same village.'

def add_unit_to_march(tg_id, unit, amount, session):
    village_id = prof.cur_village_id(tg_id)
    if unit in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        amount_in_village = 0
        if unit == 1:
            amount_in_village = session.query(Troops.spear_man).filter_by(village_pk=village_id).first()
        elif unit == 2:
            amount_in_village = session.query(Troops.sword_man).filter_by(village_pk=village_id).first()
        elif unit == 3:
            amount_in_village = session.query(Troops.brute).filter_by(village_pk=village_id).first()
        elif unit == 4:
            amount_in_village = session.query(Troops.archer).filter_by(village_pk=village_id).first()
        elif unit == 5:
            amount_in_village = session.query(Troops.scout).filter_by(village_pk=village_id).first()
        elif unit == 6:
            amount_in_village = session.query(Troops.light_cav).filter_by(village_pk=village_id).first()
        elif unit == 7:
            amount_in_village = session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first()
        elif unit == 8:
            amount_in_village = session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first()
        elif unit == 9:
            amount_in_village = session.query(Troops.ram).filter_by(village_pk=village_id).first()
        elif unit == 10:
            amount_in_village = session.query(Troops.catapult).filter_by(village_pk=village_id).first()
        elif unit == 11:
            amount_in_village = session.query(Troops.noble).filter_by(village_pk=village_id).first()
        if amount_in_village[0] >= amount:
            available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit).filter_by(sending_village=village_id).first()
            if not available_prepared_marching:
                available_prepared_marching = Prepare_marching()
                available_prepared_marching.amount = int(amount)
            else:
                new_amount = available_prepared_marching.amount + int(amount)
                if amount_in_village[0] < new_amount:
                    return 'Amount you inserted is greater than you currently have.'
                else:
                    available_prepared_marching.amount = new_amount
            available_prepared_marching.sending_village = int(village_id)
            available_prepared_marching.unit = int(unit)
            session.add(available_prepared_marching)
            session.commit()
            return generate_prepare_marching_overview(tg_id)
        else:
            return 'Amount you inserted is greater than you currently have.'
    else:
        return 'Unit does not exist.'

def all_unit_to_march(tg_id, unit, session):
    village_id = prof.cur_village_id(tg_id)
    if unit in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        spear_man_amount_in_village = 0
        sword_man_amount_in_village = 0
        brute_amount_in_village = 0
        archer_amount_in_village = 0
        scout_amount_in_village = 0
        light_cav_amount_in_village = 0
        heavy_cav_amount_in_village = 0
        mounted_arch_amount_in_village = 0
        ram_amount_in_village = 0
        catapult_amount_in_village = 0
        noble_amount_in_village = 0
        unit_1 = 1
        spear_man_amount_in_village = session.query(Troops.spear_man).filter_by(village_pk=village_id).first()
        unit_2 = 2
        sword_man_amount_in_village = session.query(Troops.sword_man).filter_by(village_pk=village_id).first()
        unit_3 = 3
        brute_amount_in_village = session.query(Troops.brute).filter_by(village_pk=village_id).first()
        unit_4 = 4
        archer_amount_in_village = session.query(Troops.archer).filter_by(village_pk=village_id).first()
        unit_5 = 5
        scout_amount_in_village = session.query(Troops.scout).filter_by(village_pk=village_id).first()
        unit_6 = 6
        light_cav_amount_in_village = session.query(Troops.light_cav).filter_by(village_pk=village_id).first()
        unit_7 = 7
        heavy_cav_amount_in_village = session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first()
        unit_8 = 8
        mounted_arch_amount_in_village = session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first()
        unit_9 = 9
        ram_amount_in_village = session.query(Troops.ram).filter_by(village_pk=village_id).first()
        unit_10 = 10
        catapult_amount_in_village = session.query(Troops.catapult).filter_by(village_pk=village_id).first()
        unit_11 = 11
        noble_amount_in_village = session.query(Troops.noble).filter_by(village_pk=village_id).first()
        if unit == unit_1:
            if spear_man_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_1).filter_by(sending_village=village_id).first()
            if not available_prepared_marching:
                available_prepared_marching = Prepare_marching()
                available_prepared_marching.amount = int(spear_man_amount_in_village[0])
            else:
                available_prepared_marching.amount = spear_man_amount_in_village[0]
            available_prepared_marching.sending_village = int(village_id)
            available_prepared_marching.unit = int(unit_1)
            session.add(available_prepared_marching)
            session.commit()
        if unit == unit_2:
            if sword_man_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_2).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(sword_man_amount_in_village[0])
                else:
                    available_prepared_marching.amount = sword_man_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_2)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_3:
            if brute_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_3).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(brute_amount_in_village[0])
                else:
                    available_prepared_marching.amount = brute_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_3)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_4:
            if archer_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_4).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(archer_amount_in_village[0])
                else:
                    available_prepared_marching.amount = archer_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_4)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_5:
            if scout_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_5).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(scout_amount_in_village[0])
                else:
                    available_prepared_marching.amount = scout_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_5)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_6:
            if light_cav_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_6).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(light_cav_amount_in_village[0])
                else:
                    available_prepared_marching.amount = light_cav_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_6)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_7:
            if heavy_cav_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_7).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(heavy_cav_amount_in_village[0])
                else:
                    available_prepared_marching.amount = heavy_cav_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_7)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_8:
            if mounted_arch_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_8).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(mounted_arch_amount_in_village[0])
                else:
                    available_prepared_marching.amount = mounted_arch_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_8)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_9:
            if ram_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_9).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(ram_amount_in_village[0])
                else:
                    available_prepared_marching.amount = ram_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_9)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_10:
            if catapult_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_10).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(catapult_amount_in_village[0])
                else:
                    available_prepared_marching.amount = catapult_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_10)
                session.add(available_prepared_marching)
                session.commit()
        if unit == unit_11:
            if noble_amount_in_village[0] > 0:
                available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_11).filter_by(sending_village=village_id).first()
                if not available_prepared_marching:
                    available_prepared_marching = Prepare_marching()
                    available_prepared_marching.amount = int(noble_amount_in_village[0])
                else:
                    available_prepared_marching.amount = noble_amount_in_village[0]
                available_prepared_marching.sending_village = int(village_id)
                available_prepared_marching.unit = int(unit_11)
                session.add(available_prepared_marching)
                session.commit()

    return generate_prepare_marching_overview(tg_id)

def add_all_units_to_march(tg_id, session):
    village_id = prof.cur_village_id(tg_id)
    unit_1 = 1
    spear_man_amount_in_village = session.query(Troops.spear_man).filter_by(village_pk=village_id).first()
    unit_2 = 2
    sword_man_amount_in_village = session.query(Troops.sword_man).filter_by(village_pk=village_id).first()
    unit_3 = 3
    brute_amount_in_village = session.query(Troops.brute).filter_by(village_pk=village_id).first()
    unit_4 = 4
    archer_amount_in_village = session.query(Troops.archer).filter_by(village_pk=village_id).first()
    unit_5 = 5
    scout_amount_in_village = session.query(Troops.scout).filter_by(village_pk=village_id).first()
    unit_6 = 6
    light_cav_amount_in_village = session.query(Troops.light_cav).filter_by(village_pk=village_id).first()
    unit_7 = 7
    heavy_cav_amount_in_village = session.query(Troops.heavy_cav).filter_by(village_pk=village_id).first()
    unit_8 = 8
    mounted_arch_amount_in_village = session.query(Troops.mounted_arch).filter_by(village_pk=village_id).first()
    unit_9 = 9
    ram_amount_in_village = session.query(Troops.ram).filter_by(village_pk=village_id).first()
    unit_10 = 10
    catapult_amount_in_village = session.query(Troops.catapult).filter_by(village_pk=village_id).first()
    unit_11 = 11
    noble_amount_in_village = session.query(Troops.noble).filter_by(village_pk=village_id).first()
    if spear_man_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_1).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(spear_man_amount_in_village[0])
        else:
            available_prepared_marching.amount = spear_man_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_1)
        session.add(available_prepared_marching)
        session.commit()
    if sword_man_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_2).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(sword_man_amount_in_village[0])
        else:
            available_prepared_marching.amount = sword_man_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_2)
        session.add(available_prepared_marching)
        session.commit()
    if brute_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_3).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(brute_amount_in_village[0])
        else:
            available_prepared_marching.amount = brute_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_3)
        session.add(available_prepared_marching)
        session.commit()
    if archer_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_4).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(archer_amount_in_village[0])
        else:
            available_prepared_marching.amount = archer_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_4)
        session.add(available_prepared_marching)
        session.commit()
    if scout_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_5).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(scout_amount_in_village[0])
        else:
            available_prepared_marching.amount = scout_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_5)
        session.add(available_prepared_marching)
        session.commit()
    if light_cav_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_6).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(light_cav_amount_in_village[0])
        else:
            available_prepared_marching.amount = light_cav_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_6)
        session.add(available_prepared_marching)
        session.commit()
    if heavy_cav_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_7).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(heavy_cav_amount_in_village[0])
        else:
            available_prepared_marching.amount = heavy_cav_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_7)
        session.add(available_prepared_marching)
        session.commit()
    if mounted_arch_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_8).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(mounted_arch_amount_in_village[0])
        else:
            available_prepared_marching.amount = mounted_arch_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_8)
        session.add(available_prepared_marching)
        session.commit()
    if ram_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_9).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(ram_amount_in_village[0])
        else:
            available_prepared_marching.amount = ram_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_9)
        session.add(available_prepared_marching)
        session.commit()
    if catapult_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_10).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(catapult_amount_in_village[0])
        else:
            available_prepared_marching.amount = catapult_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_10)
        session.add(available_prepared_marching)
        session.commit()
    if noble_amount_in_village[0] > 0:
        available_prepared_marching = session.query(Prepare_marching).filter_by(unit=unit_11).filter_by(sending_village=village_id).first()
        if not available_prepared_marching:
            available_prepared_marching = Prepare_marching()
            available_prepared_marching.amount = int(noble_amount_in_village[0])
        else:
            available_prepared_marching.amount = noble_amount_in_village[0]
        available_prepared_marching.sending_village = int(village_id)
        available_prepared_marching.unit = int(unit_11)
        session.add(available_prepared_marching)
        session.commit()

    return generate_prepare_marching_overview(tg_id)

def rem_unit_to_march(tg_id, unit, amount, session):
    village_id = prof.cur_village_id(tg_id)
    if unit in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        prepared_marching = session.query(Prepare_marching).filter_by(sending_village=village_id).filter_by(unit=unit).first()
        if prepared_marching:
            amount_in_preparation = prepared_marching.amount
            if amount_in_preparation >= amount:
                new_amount = amount_in_preparation - int(amount)
                if amount_in_preparation < new_amount:
                    return 'Amount you inserted is greater than you currently have.'
                elif new_amount <= 0:
                    session.delete(prepared_marching)
                    session.commit()
                else:
                    prepared_marching.amount = new_amount
                    session.add(prepared_marching)
                    session.commit()
                return generate_prepare_marching_overview(tg_id)
            else:
                return 'Amount you inserted is greater than you currently have.'
        else:
            return 'Preparation doesn\'t exist in preparations'
    else:
        return 'Unit doesn\'t exist in preparations'

def rem_all_unit_to_march(tg_id, session):
    village_id = prof.cur_village_id(tg_id)
    prepared_marching = session.query(Prepare_marching.pk).filter(Prepare_marching.sending_village == village_id).all()
    for value in prepared_marching:
        if value != None:
            remove_prep = session.query(Prepare_marching).filter_by(pk=value).first()
            session.delete(remove_prep)
            session.commit()
    return generate_prepare_marching_overview(tg_id)

def rem_all_unit_send_march(tg_id, session):
    village_id = prof.cur_village_id(tg_id)
    prepared_marching = session.query(Prepare_marching.pk).filter(Prepare_marching.sending_village == village_id).all()
    for value in prepared_marching:
        if value != None:
            remove_prep = session.query(Prepare_marching).filter_by(pk=value).first()
            session.delete(remove_prep)
            session.commit()

async def send_units_marching(tg_id, march_type, session, bot):
    village_id = prof.cur_village_id(tg_id)
    target_id = prof.cur_march_village_id(tg_id)
    if target_id == None:
        return 'You need to select a target first.'
    if village_id == target_id:
        return 'You can\'t attack nor support the same village.'
    target_name = villagedao.get_village_name_by_pk(target_id)
    arrival_time = wardao.calculate_arrival_time_on_slowest_unit(village_id, target_id)
    slowest_speed = wardao.get_slowest_unit_from_prep_march(village_id)
    prepared_marching = session.query(Prepare_marching).filter(Prepare_marching.sending_village == village_id).all()
    if prepared_marching:
        if march_type == 'attack':
            march_type = 'ATTACK'
            new_march = Marching()
            new_march.owner_pk = prof.cur_player_id(tg_id)
            new_march.from_village_id = prof.cur_village_id(tg_id)
            new_march.target_owner = villagedao.get_village_owner_id(target_id)
            new_march.to_village_id = target_id
            new_march.arrival_time = arrival_time
            new_march.slowest_unit_time = slowest_speed
            new_march.type_march = march_type
            new_march.spear_man = wardao.get_unit_from_preparation(1, village_id)
            new_march.sword_man = wardao.get_unit_from_preparation(2, village_id)
            new_march.brute = wardao.get_unit_from_preparation(3, village_id)
            new_march.archer = wardao.get_unit_from_preparation(4, village_id)
            new_march.scout = wardao.get_unit_from_preparation(5, village_id)
            new_march.light_cav = wardao.get_unit_from_preparation(6, village_id)
            new_march.heavy_cav = wardao.get_unit_from_preparation(7, village_id)
            new_march.mounted_arch = wardao.get_unit_from_preparation(8, village_id)
            new_march.ram = wardao.get_unit_from_preparation(9, village_id)
            new_march.catapult = wardao.get_unit_from_preparation(10, village_id)
            new_march.noble = wardao.get_unit_from_preparation(11, village_id)
            new_march.looted_wood = 0
            new_march.looted_stone = 0
            new_march.looted_iron = 0
            remove_unit_from_village = session.query(Troops).filter_by(village_pk=village_id).first()
            remove_unit_from_village.spear_man = remove_unit_from_village.spear_man - wardao.get_unit_from_preparation(1, village_id)
            remove_unit_from_village.sword_man = remove_unit_from_village.sword_man - wardao.get_unit_from_preparation(2, village_id)
            remove_unit_from_village.brute = remove_unit_from_village.brute - wardao.get_unit_from_preparation(3, village_id)
            remove_unit_from_village.archer = remove_unit_from_village.archer - wardao.get_unit_from_preparation(4, village_id)
            remove_unit_from_village.scout = remove_unit_from_village.scout - wardao.get_unit_from_preparation(5, village_id)
            remove_unit_from_village.light_cav = remove_unit_from_village.light_cav - wardao.get_unit_from_preparation(6, village_id)
            remove_unit_from_village.heavy_cav = remove_unit_from_village.heavy_cav - wardao.get_unit_from_preparation(7, village_id)
            remove_unit_from_village.mounted_arch = remove_unit_from_village.mounted_arch - wardao.get_unit_from_preparation(8, village_id)
            remove_unit_from_village.ram = remove_unit_from_village.ram - wardao.get_unit_from_preparation(9, village_id)
            remove_unit_from_village.catapult = remove_unit_from_village.catapult - wardao.get_unit_from_preparation(10, village_id)
            remove_unit_from_village.noble = remove_unit_from_village.noble - wardao.get_unit_from_preparation(11, village_id)
            session.add(new_march)
            session.add(remove_unit_from_village)
            rem_all_unit_send_march(tg_id, session)
            session.commit()
            message = 'Troops started marching towards ' + target_name + ' as ' + march_type + '.'
            sender_pk = prof.cur_player_id(tg_id)
            sender_name = prof.player_name_by_pk(sender_pk)
            sender_village = villagedao.get_village_name_by_pk(village_id)
            receiver_pk = villagedao.get_village_owner_id(target_id)
            if receiver_pk != None and sender_pk != receiver_pk:
                receiver_tgid = profiledao.get_player_tg_id_by_pk(receiver_pk)
                receiver_message = 'Your village ' + target_name + ' is being ⚔attacked!\n' \
                                                                   '👤' + str(sender_name) + '(/pp' + str(sender_pk) + ') from ' + str(sender_village) + ' /view_vil' + str(village_id)
                await player_notify.notify_possible_reciever(receiver_tgid, receiver_message, session)
            return message
        if march_type == 'support':
            march_type = 'SUPPORT'
            new_march = Marching()
            new_march.owner_pk = prof.cur_player_id(tg_id)
            new_march.from_village_id = prof.cur_village_id(tg_id)
            new_march.target_owner = villagedao.get_village_owner_id(target_id)
            new_march.to_village_id = target_id
            new_march.arrival_time = arrival_time
            new_march.slowest_unit_time = slowest_speed
            new_march.type_march = march_type
            new_march.spear_man = wardao.get_unit_from_preparation(1, village_id)
            new_march.sword_man = wardao.get_unit_from_preparation(2, village_id)
            new_march.brute = wardao.get_unit_from_preparation(3, village_id)
            new_march.archer = wardao.get_unit_from_preparation(4, village_id)
            new_march.scout = wardao.get_unit_from_preparation(5, village_id)
            new_march.light_cav = wardao.get_unit_from_preparation(6, village_id)
            new_march.heavy_cav = wardao.get_unit_from_preparation(7, village_id)
            new_march.mounted_arch = wardao.get_unit_from_preparation(8, village_id)
            new_march.ram = wardao.get_unit_from_preparation(9, village_id)
            new_march.catapult = wardao.get_unit_from_preparation(10, village_id)
            new_march.noble = wardao.get_unit_from_preparation(11, village_id)
            new_march.looted_wood = 0
            new_march.looted_stone = 0
            new_march.looted_iron = 0
            remove_unit_from_village = session.query(Troops).filter_by(village_pk=village_id).first()
            remove_unit_from_village.spear_man = remove_unit_from_village.spear_man - wardao.get_unit_from_preparation(1, village_id)
            remove_unit_from_village.sword_man = remove_unit_from_village.sword_man - wardao.get_unit_from_preparation(2, village_id)
            remove_unit_from_village.brute = remove_unit_from_village.brute - wardao.get_unit_from_preparation(3, village_id)
            remove_unit_from_village.archer = remove_unit_from_village.archer - wardao.get_unit_from_preparation(4, village_id)
            remove_unit_from_village.scout = remove_unit_from_village.scout - wardao.get_unit_from_preparation(5, village_id)
            remove_unit_from_village.light_cav = remove_unit_from_village.light_cav - wardao.get_unit_from_preparation(6, village_id)
            remove_unit_from_village.heavy_cav = remove_unit_from_village.heavy_cav - wardao.get_unit_from_preparation(7, village_id)
            remove_unit_from_village.mounted_arch = remove_unit_from_village.mounted_arch - wardao.get_unit_from_preparation(8, village_id)
            remove_unit_from_village.ram = remove_unit_from_village.ram - wardao.get_unit_from_preparation(9, village_id)
            remove_unit_from_village.catapult = remove_unit_from_village.catapult - wardao.get_unit_from_preparation(10, village_id)
            remove_unit_from_village.noble = remove_unit_from_village.noble - wardao.get_unit_from_preparation(11, village_id)
            session.add(new_march)
            session.add(remove_unit_from_village)
            rem_all_unit_send_march(tg_id, session)
            session.commit()
            message = 'Troops started marching towards ' + target_name + ' as ' + march_type + '.'
            sender_pk = prof.cur_player_id(tg_id)
            sender_name = prof.player_name_by_pk(sender_pk)
            sender_village = villagedao.get_village_name_by_pk(village_id)
            receiver_pk = villagedao.get_village_owner_id(target_id)
            if receiver_pk != None and sender_pk != receiver_pk:
                receiver_tgid = profiledao.get_player_tg_id_by_pk(receiver_pk)
                receiver_message = 'Your village ' + target_name + ' is being 🛡supported!\n' \
                                                                   '👤' + str(sender_name) + '(/pp' + str(sender_pk) + ') from ' + str(sender_village) + ' /view_vil' + str(village_id)
                await player_notify.notify_possible_reciever(receiver_tgid, receiver_message, session)
            return message
        if march_type is not 'attack' or march_type is not 'support':
            return 'Something did go wrong. Try /send_attack or /send_support.'

def withdraw_support(support_id, session):
    owner = wardao.grab_support_owner_by_pk(support_id)
    from_village_id = wardao.get_from_village_support(support_id)
    from_village_name = villagedao.get_village_name_by_pk(from_village_id)
    target_village_id = wardao.get_in_village_support(support_id)
    target_village_name = villagedao.get_village_name_by_pk(target_village_id)
    arrival_time = wardao.calculate_arrival_time_on_slowest_unit_support(support_id, from_village_id, target_village_id)
    support = session.query(Support).filter(Support.pk==support_id).first()
    new_march = Marching()
    new_march.owner_pk = owner
    new_march.from_village_id = from_village_id
    new_march.target_owner = villagedao.get_village_owner_id(target_village_id)
    new_march.to_village_id = target_village_id
    new_march.arrival_time = arrival_time
    new_march.slowest_unit_time = 0
    new_march.type_march = 'RETURN'
    new_march.spear_man = wardao.get_unit_from_support(1, support_id)
    new_march.sword_man = wardao.get_unit_from_support(2, support_id)
    new_march.brute = wardao.get_unit_from_support(3, support_id)
    new_march.archer = wardao.get_unit_from_support(4, support_id)
    new_march.scout = wardao.get_unit_from_support(5, support_id)
    new_march.light_cav = wardao.get_unit_from_support(6, support_id)
    new_march.heavy_cav = wardao.get_unit_from_support(7, support_id)
    new_march.mounted_arch = wardao.get_unit_from_support(8, support_id)
    new_march.ram = wardao.get_unit_from_support(9, support_id)
    new_march.catapult = wardao.get_unit_from_support(10, support_id)
    new_march.noble = wardao.get_unit_from_support(11, support_id)
    new_march.looted_wood = 0
    new_march.looted_stone = 0
    new_march.looted_iron = 0
    session.add(new_march)
    session.delete(support)
    session.commit()
    message = 'Your troops from ' + target_village_name + ' are going back to ' + from_village_name
    return message


def calculate_war_outcome(due_march, session):
    #   Create database needed sessions:
    attacking_player = session.query(Player).filter(Player.pk == due_march.owner_pk).first()
    defending_player = session.query(Player).filter(Player.pk == due_march.target_owner).first()
    defending_troops = session.query(Troops).filter(Troops.village_pk == due_march.to_village_id).first()
    defending_building = session.query(Building).filter(Building.village_pk == due_march.to_village_id).first()
    new_attacker_report = Reports()
    new_defender_report = Reports()
    new_march = Marching()

    #   Random needed call features
    attacker_name = villagedao.get_village_owner_player_name(due_march.from_village_id)
    attacker_id = str(due_march.owner_pk)
    defender_name = villagedao.get_village_owner_player_name(due_march.to_village_id)
    defender_id = str(due_march.target_owner)
    if defender_id == None:
        defender_id = '?'
    sender_village_name = villagedao.get_village_name_by_pk(due_march.from_village_id)
    sender_village_id = str(due_march.from_village_id)
    target_village_name = villagedao.get_village_name_by_pk(due_march.to_village_id)
    target_village_id = str(due_march.to_village_id)

    #   Get all values from the attackers side
    total_attack_amount = 0
    total_attack_population = 0
    if due_march.spear_man >= 0:
        
        attacking_spear_man_amount = due_march.spear_man
        total_attack_amount = total_attack_amount + attacking_spear_man_amount
        total_attack_population = total_attack_population + attacking_spear_man_amount
        spear_man_attack = unitdao.get_unit_atk(1)
        spear_man_loot_cap = unitdao.get_unit_loot(1)
    if due_march.sword_man >= 0:
        attacking_sword_man_amount = due_march.sword_man
        total_attack_amount = total_attack_amount + attacking_sword_man_amount
        total_attack_population = total_attack_population + attacking_sword_man_amount
        sword_man_attack = unitdao.get_unit_atk(2)
        sword_man_loot_cap = unitdao.get_unit_loot(2)
    if due_march.brute >= 0:
        attacking_brute_amount = due_march.brute
        total_attack_amount = total_attack_amount + attacking_brute_amount
        total_attack_population = total_attack_population + attacking_brute_amount
        brute_attack = unitdao.get_unit_atk(3)
        brute_loot_cap = unitdao.get_unit_loot(3)
    if due_march.archer >= 0:
        attacking_archer_amount = due_march.archer
        total_attack_amount = total_attack_amount + attacking_archer_amount
        total_attack_population = total_attack_population + attacking_archer_amount
        archer_attack = unitdao.get_unit_atk(4)
        archer_loot_cap = unitdao.get_unit_loot(4)
    if due_march.light_cav >= 0:
        attacking_light_cav_amount = due_march.light_cav
        total_attack_amount = total_attack_amount + attacking_light_cav_amount
        total_attack_population = total_attack_population + (attacking_light_cav_amount * 4)
        light_cav_attack = unitdao.get_unit_atk(6)
        light_cav_loot_cap = unitdao.get_unit_loot(6)
    if due_march.heavy_cav >= 0:
        attacking_heavy_cav_amount = due_march.heavy_cav
        total_attack_amount = total_attack_amount + attacking_heavy_cav_amount
        total_attack_population = total_attack_population + (attacking_heavy_cav_amount * 6)
        heavy_cav_attack = unitdao.get_unit_atk(7)
        heavy_cav_loot_cap = unitdao.get_unit_loot(7)
    if due_march.mounted_arch >= 0:
        attacking_mounted_arch_amount = due_march.mounted_arch
        total_attack_amount = total_attack_amount + attacking_mounted_arch_amount
        total_attack_population = total_attack_population + (attacking_mounted_arch_amount * 5)
        mounted_arch_attack = unitdao.get_unit_atk(8)
        mounted_arch_loot_cap = unitdao.get_unit_loot(8)
    if due_march.catapult >= 0:
        attacking_catapult_amount = due_march.catapult
        total_attack_amount = total_attack_amount + attacking_catapult_amount
        total_attack_population = total_attack_population + (attacking_catapult_amount * 8)
        catapult_attack = unitdao.get_unit_atk(10)

    #   #   specials
    if due_march.ram >= 0:
        attacking_ram_amount = due_march.ram
        total_attack_amount = total_attack_amount + attacking_ram_amount
        total_attack_population = total_attack_population + (attacking_ram_amount * 5)
        ram_attack = unitdao.get_unit_atk(9)
    if due_march.noble >= 0:
        attacking_noble_amount = due_march.noble
        total_attack_amount = total_attack_amount + attacking_noble_amount
        total_attack_population = total_attack_population + (attacking_noble_amount * 100)
    if due_march.scout >= 0:
        attacking_scout_amount = due_march.scout
        total_attack_amount = total_attack_amount + attacking_scout_amount
        total_attack_population = total_attack_population + (attacking_scout_amount * 2)


    #   get defending troops:
    defending_spear_man_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 1)
    defending_sword_man_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 2)
    defending_brute_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 3)
    defending_archer_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 4)
    defending_scout_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 5)
    defending_light_cav_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 6)
    defending_heavy_cav_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 7)
    defending_mounted_arch_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 8)
    defending_ram_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 9)
    defending_catapult_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 10)
    defending_noble_amount = unitdao.get_unit_amount_defending_village(due_march.to_village_id, 11)

    #   Clone them for the report
    pre_war_spear_man_amount = defending_spear_man_amount
    pre_war_sword_man_amount = defending_sword_man_amount
    pre_war_brute_amount = defending_brute_amount
    pre_war_archer_amount = defending_archer_amount
    pre_war_scout_amount = defending_scout_amount
    pre_war_light_cav_amount = defending_light_cav_amount
    pre_war_heavy_cav_amount = defending_heavy_cav_amount
    pre_war_mounted_arch_amount = defending_mounted_arch_amount
    pre_war_ram_amount = defending_ram_amount
    pre_war_catapult_amount = defending_catapult_amount
    pre_war_noble_amount = defending_noble_amount
    total_defense_population = 0

    #   Defense multiplier bonuses:
    wall_defense_multiplier = villagedao.get_wall_bonus(due_march.to_village_id)

    #   # Get defensive stats:
    if defending_spear_man_amount >= 0:
        total_defense_population = total_defense_population + defending_spear_man_amount
        spear_man_inf_defense = unitdao.get_unit_def(1)
        spear_man_cav_defense = unitdao.get_unit_def_cav(1)
        spear_man_arc_defense = unitdao.get_unit_def_arc(1)
    if defending_sword_man_amount >= 0:
        total_defense_population = total_defense_population + defending_sword_man_amount
        sword_man_inf_defense = unitdao.get_unit_def(2)
        sword_man_cav_defense = unitdao.get_unit_def_cav(2)
        sword_man_arc_defense = unitdao.get_unit_def_arc(2)
    if defending_brute_amount >= 0:
        total_defense_population = total_defense_population + defending_brute_amount
        brute_inf_defense = unitdao.get_unit_def(3)
        brute_cav_defense = unitdao.get_unit_def_cav(3)
        brute_arc_defense = unitdao.get_unit_def_arc(3)
    if defending_archer_amount >= 0:
        total_defense_population = total_defense_population + defending_archer_amount
        archer_inf_defense = unitdao.get_unit_def(4)
        archer_cav_defense = unitdao.get_unit_def_cav(4)
        archer_arc_defense = unitdao.get_unit_def_arc(4)
    if defending_scout_amount >= 0:
        total_defense_population = total_defense_population + (defending_scout_amount*2)
        scout_inf_defense = unitdao.get_unit_def(5)
        scout_cav_defense = unitdao.get_unit_def_cav(5)
        scout_arc_defense = unitdao.get_unit_def_arc(5)
    if defending_light_cav_amount >= 0:
        total_defense_population = total_defense_population + (defending_light_cav_amount*4)
        light_cav_inf_defense = unitdao.get_unit_def(6)
        light_cav_cav_defense = unitdao.get_unit_def_cav(6)
        light_cav_arc_defense = unitdao.get_unit_def_arc(6)
    if defending_heavy_cav_amount >= 0:
        total_defense_population = total_defense_population + (defending_heavy_cav_amount*6)
        heavy_cav_inf_defense = unitdao.get_unit_def(7)
        heavy_cav_cav_defense = unitdao.get_unit_def_cav(7)
        heavy_cav_arc_defense = unitdao.get_unit_def_arc(7)
    if defending_mounted_arch_amount >= 0:
        total_defense_population = total_defense_population + (defending_mounted_arch_amount*5)
        mounted_arch_inf_defense = unitdao.get_unit_def(8)
        mounted_arch_cav_defense = unitdao.get_unit_def_cav(8)
        mounted_arch_arc_defense = unitdao.get_unit_def_arc(8)
    if defending_ram_amount >= 0:
        total_defense_population = total_defense_population + (defending_ram_amount*5)
        ram_inf_defense = unitdao.get_unit_def(9)
        ram_cav_defense = unitdao.get_unit_def_cav(9)
        ram_arc_defense = unitdao.get_unit_def_arc(9)
    if defending_catapult_amount >= 0:
        total_defense_population = total_defense_population + (defending_catapult_amount*8)
        catapult_inf_defense = unitdao.get_unit_def(10)
        catapult_cav_defense = unitdao.get_unit_def_cav(10)
        catapult_arc_defense = unitdao.get_unit_def_arc(10)
    if defending_noble_amount >= 0:
        total_defense_population = total_defense_population + (defending_noble_amount*100)
        noble_inf_defense = unitdao.get_unit_def(11)
        noble_cav_defense = unitdao.get_unit_def_cav(11)
        noble_arc_defense = unitdao.get_unit_def_arc(11)

    # set graveyard here
    att_dead_spear_man_amount = 0
    att_dead_sword_man_amount = 0
    att_dead_brute_amount = 0
    att_dead_archer_amount = 0
    att_dead_scout_amount = 0
    att_dead_light_cav_amount = 0
    att_dead_heavy_cav_amount = 0
    att_dead_mounted_arch_amount = 0
    att_dead_ram_amount = 0
    att_dead_catapult_amount = 0
    att_dead_noble_amount = 0
    def_dead_spear_man_amount = 0
    def_dead_sword_man_amount = 0
    def_dead_brute_amount = 0
    def_dead_archer_amount = 0
    def_dead_scout_amount = 0
    def_dead_light_cav_amount = 0
    def_dead_heavy_cav_amount = 0
    def_dead_mounted_arch_amount = 0
    def_dead_ram_amount = 0
    def_dead_catapult_amount = 0
    def_dead_noble_amount = 0

    # set def standard:
    defending_spear_man_inf = 0
    defending_sword_man_inf = 0
    defending_brute_inf = 0
    defending_archer_inf = 0
    defending_scout_inf = 0
    defending_light_cav_inf = 0
    defending_heavy_cav_inf = 0
    defending_mounted_arch_inf = 0
    defending_ram_inf = 0
    defending_catapult_inf = 0
    defending_noble_inf = 0
    defending_spear_man_cav = 0
    defending_sword_man_cav = 0
    defending_brute_cav = 0
    defending_archer_cav = 0
    defending_scout_cav = 0
    defending_light_cav_cav = 0
    defending_heavy_cav_cav = 0
    defending_mounted_arch_cav = 0
    defending_ram_cav = 0
    defending_catapult_cav = 0
    defending_noble_cav = 0
    defending_spear_man_arc = 0
    defending_sword_man_arc = 0
    defending_brute_arc = 0
    defending_archer_arc = 0
    defending_scout_arc = 0
    defending_light_cav_arc = 0
    defending_heavy_cav_arc = 0
    defending_mounted_arch_arc = 0
    defending_ram_arc = 0
    defending_catapult_arc = 0
    defending_noble_arc = 0

    # insert loop here
    both_parties_have_units = True
    while both_parties_have_units is True:
        # calculate attack powers
        att_power_inf = 0
        if attacking_spear_man_amount and spear_man_attack:
            att_power_inf = att_power_inf + (attacking_spear_man_amount*spear_man_attack)
        if attacking_sword_man_amount and sword_man_attack:
            att_power_inf = att_power_inf + (attacking_sword_man_amount*sword_man_attack)
        if attacking_brute_amount and brute_attack:
            att_power_inf = att_power_inf + (attacking_brute_amount*brute_attack)
        if attacking_ram_amount and ram_attack:
            att_power_inf = att_power_inf + (attacking_ram_amount*ram_attack)

        att_power_cav = 0
        if attacking_light_cav_amount and light_cav_attack:
            att_power_cav = att_power_cav + (attacking_light_cav_amount*light_cav_attack)
        if attacking_heavy_cav_amount and heavy_cav_attack:
            att_power_cav = att_power_cav + (attacking_heavy_cav_amount*heavy_cav_attack)

        att_power_arc = 0
        if attacking_archer_amount and archer_attack:
            att_power_arc = att_power_arc + (attacking_archer_amount*archer_attack)
        if attacking_mounted_arch_amount and mounted_arch_attack:
            att_power_arc = att_power_arc + (attacking_mounted_arch_amount*mounted_arch_attack)
        if attacking_catapult_amount and catapult_attack:
            att_power_arc = att_power_arc + (attacking_catapult_amount*catapult_attack)

        total_att_power = att_power_inf + att_power_cav + att_power_arc

        percentage_defending_against_inf = (wardao.percentage_devided_by_amount(100, total_att_power)*att_power_inf)/100
        percentage_defending_against_cav = (wardao.percentage_devided_by_amount(100, total_att_power)*att_power_cav)/100
        percentage_defending_against_arc = (wardao.percentage_devided_by_amount(100, total_att_power)*att_power_arc)/100

        #   getting the defensive powers
        def_power_inf = 0
        def_power_cav = 0
        def_power_arc = 0

        if defending_spear_man_amount >= 0:
            defending_spear_man_inf = int(float(defending_spear_man_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_spear_man_inf) * float(spear_man_inf_defense))
            defending_spear_man_cav = int(float(defending_spear_man_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_spear_man_cav) * float(spear_man_cav_defense))
            defending_spear_man_arc = int(float(defending_spear_man_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_spear_man_arc) * float(spear_man_arc_defense))
        if defending_sword_man_amount >= 0:
            defending_sword_man_inf = int(float(defending_sword_man_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_sword_man_inf) * float(sword_man_inf_defense))
            defending_sword_man_cav = int(float(defending_sword_man_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_sword_man_cav) * float(sword_man_cav_defense))
            defending_sword_man_arc = int(float(defending_sword_man_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_sword_man_arc) * float(sword_man_arc_defense))
        if defending_brute_amount >= 0:
            defending_brute_inf = int(float(defending_brute_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_brute_inf) * float(brute_inf_defense))
            defending_brute_cav = int(float(defending_brute_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_brute_cav) * float(brute_cav_defense))
            defending_brute_arc = int(float(defending_brute_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_brute_arc) * float(brute_arc_defense))
        if defending_archer_amount >= 0:
            defending_archer_inf = int(float(defending_archer_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_archer_inf) * float(archer_inf_defense))
            defending_archer_cav = int(float(defending_archer_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_archer_cav) * float(archer_cav_defense))
            defending_archer_arc = int(float(defending_archer_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_archer_arc) * float(archer_arc_defense))
        if defending_scout_amount >= 0:
            defending_scout_inf = int(float(defending_scout_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_scout_inf) * float(scout_inf_defense))
            defending_scout_cav = int(float(defending_scout_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_scout_cav) * float(scout_cav_defense))
            defending_scout_arc = int(float(defending_scout_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_scout_arc) * float(scout_arc_defense))
        if defending_light_cav_amount >= 0:
            defending_light_cav_inf = int(float(defending_light_cav_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_light_cav_inf) * float(light_cav_inf_defense))
            defending_light_cav_cav = int(float(defending_light_cav_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_light_cav_cav) * float(light_cav_cav_defense))
            defending_light_cav_arc = int(float(defending_light_cav_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_light_cav_arc) * float(light_cav_arc_defense))
        if defending_heavy_cav_amount >= 0:
            defending_heavy_cav_inf = int(float(defending_heavy_cav_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_heavy_cav_inf) * float(heavy_cav_inf_defense))
            defending_heavy_cav_cav = int(float(defending_heavy_cav_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_heavy_cav_cav) * float(heavy_cav_cav_defense))
            defending_heavy_cav_arc = int(float(defending_heavy_cav_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_heavy_cav_arc) * float(heavy_cav_arc_defense))
        if defending_mounted_arch_amount >= 0:
            defending_mounted_arch_inf = int(float(defending_mounted_arch_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_mounted_arch_inf) * float(mounted_arch_inf_defense))
            defending_mounted_arch_cav = int(float(defending_mounted_arch_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_mounted_arch_cav) * float(mounted_arch_cav_defense))
            defending_mounted_arch_arc = int(float(defending_mounted_arch_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_mounted_arch_arc) * float(mounted_arch_arc_defense))
        if defending_ram_amount >= 0:
            defending_ram_inf = int(float(defending_ram_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_ram_inf) * float(ram_inf_defense))
            defending_ram_cav = int(float(defending_ram_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_ram_cav) * float(ram_cav_defense))
            defending_ram_arc = int(float(defending_ram_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_ram_arc) * float(ram_arc_defense))
        if defending_catapult_amount >= 0:
            defending_catapult_inf = int(float(defending_catapult_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_catapult_inf) * float(catapult_inf_defense))
            defending_catapult_cav = int(float(defending_catapult_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_catapult_cav) * float(catapult_cav_defense))
            defending_catapult_arc = int(float(defending_catapult_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_catapult_arc) * float(catapult_arc_defense))
        if defending_noble_amount >= 0:
            defending_noble_inf = int(float(defending_noble_amount) * float(percentage_defending_against_inf))
            def_power_inf = def_power_inf + int(float(defending_noble_inf) * float(noble_inf_defense))
            defending_noble_cav = int(float(defending_noble_amount) * float(percentage_defending_against_cav))
            def_power_cav = def_power_cav + int(float(defending_noble_cav) * float(noble_cav_defense))
            defending_noble_arc = int(float(defending_noble_amount) * float(percentage_defending_against_arc))
            def_power_arc = def_power_arc + int(float(defending_noble_arc) * float(noble_arc_defense))



    #   Adding in bonusses for the defender
        def_power_inf = def_power_inf * wall_defense_multiplier
        def_power_cav = def_power_cav * wall_defense_multiplier
        def_power_arc = def_power_arc * wall_defense_multiplier

        #   War calculations

        if attacking_scout_amount > 0 and defending_scout_amount > 0:
            defending_scout_defense = defending_scout_amount*2
            if attacking_scout_amount > defending_scout_defense:
                att_dead_scout_amount = att_dead_scout_amount + defending_scout_defense
                attacking_scout_amount = attacking_scout_amount - att_dead_scout_amount
            elif attacking_scout_amount <= defending_scout_defense:
                att_dead_scout_amount = att_dead_scout_amount + attacking_scout_amount
                attacking_scout_amount = 0

        new_att_power_inf = int(att_power_inf - def_power_inf)
        ded_att_power_inf = int(att_power_inf - new_att_power_inf)
        new_def_power_inf = int(def_power_inf - att_power_inf)
        ded_def_power_inf = int(def_power_inf - new_def_power_inf)

        if new_att_power_inf <= 0:
            att_power_inf = 0
            try:
                def_power_inf_amount = 100 / def_power_inf
            except ZeroDivisionError:
                def_power_inf_amount = 100
            defense_which_died = def_power_inf_amount*ded_def_power_inf/100
            if attacking_spear_man_amount >0:
                att_dead_spear_man_amount = att_dead_spear_man_amount + attacking_spear_man_amount
                attacking_spear_man_amount = attacking_spear_man_amount - att_dead_spear_man_amount
            if attacking_sword_man_amount >0:
                att_dead_sword_man_amount = att_dead_sword_man_amount + attacking_sword_man_amount
                attacking_sword_man_amount = attacking_sword_man_amount - att_dead_sword_man_amount
            if attacking_brute_amount >0:
                att_dead_brute_amount = att_dead_brute_amount + attacking_brute_amount
                attacking_brute_amount = attacking_brute_amount - att_dead_brute_amount
            if attacking_ram_amount >0:
                att_dead_ram_amount = att_dead_ram_amount + attacking_ram_amount  
                attacking_ram_amount = attacking_ram_amount - attacking_ram_amount
            if defending_spear_man_inf > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + round(defending_spear_man_inf*defense_which_died)
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_inf > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + round(defending_sword_man_inf*defense_which_died)
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_inf > 0:
                def_dead_brute_amount = def_dead_brute_amount + round(defending_brute_inf*defense_which_died)
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_inf > 0:
                def_dead_archer_amount = def_dead_archer_amount + round(defending_archer_inf*defense_which_died)
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_inf > 0:
                def_dead_scout_amount = def_dead_scout_amount + round(defending_scout_inf*defense_which_died)
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_inf > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + round(defending_light_cav_inf*defense_which_died)
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_inf > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + round(defending_heavy_cav_inf*defense_which_died)
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_inf > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + round(defending_mounted_arch_inf*defense_which_died)
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_inf > 0:
                def_dead_ram_amount = def_dead_ram_amount + round(defending_ram_inf*defense_which_died)
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_inf > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + round(defending_catapult_inf*defense_which_died)
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_inf > 0:
                def_dead_noble_amount = def_dead_noble_amount + round(defending_noble_inf*defense_which_died)
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0
        if new_def_power_inf <= 0:
            def_power_inf = 0
            try:
                att_power_inf_amount = 100 / att_power_inf
            except ZeroDivisionError:
                att_power_inf_amount = 100
            attack_which_died = att_power_inf_amount*ded_att_power_inf/100
            if attacking_spear_man_amount > 0:
                att_dead_spear_man_amount = att_dead_spear_man_amount + int(attacking_spear_man_amount*attack_which_died)
                attacking_spear_man_amount = attacking_spear_man_amount - int(att_dead_spear_man_amount)
                if attacking_spear_man_amount <= 0:
                    attacking_spear_man_amount = 0
            if attacking_sword_man_amount > 0:
                att_dead_sword_man_amount = att_dead_sword_man_amount + int(attacking_sword_man_amount*attack_which_died)
                attacking_sword_man_amount = attacking_sword_man_amount - int(att_dead_sword_man_amount)
                if attacking_sword_man_amount <= 0:
                    attacking_sword_man_amount = 0
            if attacking_brute_amount > 0:
                att_dead_brute_amount = att_dead_brute_amount + int(attacking_brute_amount*attack_which_died)
                attacking_brute_amount = attacking_brute_amount - int(att_dead_brute_amount)
                if attacking_brute_amount <= 0:
                    attacking_brute_amount = 0
            if attacking_ram_amount > 0:
                att_dead_ram_amount = att_dead_ram_amount + int(attacking_ram_amount*attack_which_died)
                attacking_ram_amount = attacking_ram_amount - int(att_dead_ram_amount)
                if attacking_ram_amount <= 0:
                    attacking_ram_amount = 0
            if defending_spear_man_inf > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + defending_spear_man_inf
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_inf > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + defending_sword_man_inf
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_inf > 0:
                def_dead_brute_amount = def_dead_brute_amount + defending_brute_inf
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_inf > 0:
                def_dead_archer_amount = def_dead_archer_amount + defending_archer_inf
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_inf > 0:
                def_dead_scout_amount = def_dead_scout_amount + defending_scout_inf
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_inf > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + defending_light_cav_inf
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_inf > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + defending_heavy_cav_inf
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_inf > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + defending_mounted_arch_inf
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_inf > 0:
                def_dead_ram_amount = def_dead_ram_amount + defending_ram_inf
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_inf > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + defending_catapult_inf
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_inf > 0:
                def_dead_noble_amount = def_dead_noble_amount + defending_noble_inf
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0


        new_att_power_cav = att_power_cav - def_power_cav
        ded_att_power_cav = att_power_cav - new_att_power_cav
        new_def_power_cav = def_power_cav - att_power_cav
        ded_def_power_cav = def_power_cav - new_def_power_cav

        if new_att_power_cav <= 0:
            att_power_cav = 0
            try:
                def_power_cav_amount = 100 / def_power_cav
            except ZeroDivisionError:
                def_power_cav_amount = 100
            defense_which_died = def_power_cav_amount*ded_def_power_cav/100
            if attacking_light_cav_amount >0:
                att_dead_light_cav_amount = att_dead_light_cav_amount + attacking_light_cav_amount
                attacking_light_cav_amount = attacking_light_cav_amount - att_dead_light_cav_amount
            if attacking_heavy_cav_amount >0:
                att_dead_heavy_cav_amount = att_dead_heavy_cav_amount + attacking_heavy_cav_amount
                attacking_heavy_cav_amount = attacking_heavy_cav_amount - att_dead_heavy_cav_amount
            if defending_spear_man_cav > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + round(defending_spear_man_cav*defense_which_died)
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_cav > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + round(defending_sword_man_cav*defense_which_died)
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_cav > 0:
                def_dead_brute_amount = def_dead_brute_amount + round(defending_brute_cav*defense_which_died)
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_cav > 0:
                def_dead_archer_amount = def_dead_archer_amount + round(defending_archer_cav*defense_which_died)
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_cav > 0:
                def_dead_scout_amount = def_dead_scout_amount + round(defending_scout_cav*defense_which_died)
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_cav > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + round(defending_light_cav_cav*defense_which_died)
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_cav > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + round(defending_heavy_cav_cav*defense_which_died)
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_cav > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + round(defending_mounted_arch_cav*defense_which_died)
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_cav > 0:
                def_dead_ram_amount = def_dead_ram_amount + round(defending_ram_cav*defense_which_died)
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_cav > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + round(defending_catapult_cav*defense_which_died)
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_cav > 0:
                def_dead_noble_amount = def_dead_noble_amount + round(defending_noble_cav*defense_which_died)
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0
        if new_def_power_cav <= 0:
            def_power_cav = 0
            try:
                att_power_cav_amount = 100 / att_power_cav
            except ZeroDivisionError:
                att_power_cav_amount = 100
            attack_which_died = att_power_cav_amount*ded_att_power_cav/100
            if attacking_light_cav_amount > 0:
                att_dead_light_cav_amount = att_dead_light_cav_amount + int(attacking_light_cav_amount*attack_which_died)
                attacking_light_cav_amount = attacking_light_cav_amount - int(att_dead_light_cav_amount)
                if attacking_light_cav_amount <= 0:
                    attacking_light_cav_amount = 0
            if attacking_heavy_cav_amount > 0:
                att_dead_heavy_cav_amount = att_dead_heavy_cav_amount + int(attacking_heavy_cav_amount*attack_which_died)
                attacking_heavy_cav_amount = attacking_heavy_cav_amount - int(att_dead_heavy_cav_amount)
                if attacking_heavy_cav_amount <= 0:
                    attacking_heavy_cav_amount = 0
            if defending_spear_man_cav > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + defending_spear_man_cav
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_cav > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + defending_sword_man_cav
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_cav > 0:
                def_dead_brute_amount = def_dead_brute_amount + defending_brute_cav
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_cav > 0:
                def_dead_archer_amount = def_dead_archer_amount + defending_archer_cav
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_cav > 0:
                def_dead_scout_amount = def_dead_scout_amount + defending_scout_cav
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_cav > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + defending_light_cav_cav
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_cav > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + defending_heavy_cav_cav
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_cav > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + defending_mounted_arch_cav
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_cav > 0:
                def_dead_ram_amount = def_dead_ram_amount + defending_ram_cav
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_cav > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + defending_catapult_cav
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_cav > 0:
                def_dead_noble_amount = def_dead_noble_amount + defending_noble_cav
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0

        new_att_power_arc = att_power_arc - def_power_arc
        ded_att_power_arc = att_power_arc - new_att_power_arc
        new_def_power_arc = def_power_arc - att_power_arc
        ded_def_power_arc = def_power_arc - new_def_power_arc

        if new_att_power_arc <= 0:
            att_power_arc = 0
            try:
                def_power_arc_amount = 100 / def_power_arc
            except ZeroDivisionError:
                def_power_arc_amount = 100
            defense_which_died = def_power_arc_amount*ded_def_power_arc/100
            if attacking_archer_amount >0:
                att_dead_archer_amount = att_dead_archer_amount + attacking_archer_amount
                attacking_archer_amount = attacking_archer_amount - att_dead_archer_amount
            if attacking_mounted_arch_amount >0:
                att_dead_mounted_arch_amount = att_dead_mounted_arch_amount + attacking_mounted_arch_amount
                attacking_mounted_arch_amount = attacking_mounted_arch_amount - att_dead_mounted_arch_amount
            if attacking_catapult_amount >0:
                att_dead_catapult_amount = att_dead_catapult_amount + attacking_catapult_amount
                attacking_catapult_amount = attacking_catapult_amount - att_dead_catapult_amount
            if defending_spear_man_arc > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + round(defending_spear_man_arc*defense_which_died)
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_arc > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + round(defending_sword_man_arc*defense_which_died)
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_arc > 0:
                def_dead_brute_amount = def_dead_brute_amount + round(defending_brute_arc*defense_which_died)
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_arc > 0:
                def_dead_archer_amount = def_dead_archer_amount + round(defending_archer_arc*defense_which_died)
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_arc > 0:
                def_dead_scout_amount = def_dead_scout_amount + round(defending_scout_arc*defense_which_died)
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_arc > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + round(defending_light_cav_arc*defense_which_died)
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_arc > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + round(defending_heavy_cav_arc*defense_which_died)
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_arc > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + round(defending_mounted_arch_arc*defense_which_died)
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_arc > 0:
                def_dead_ram_amount = def_dead_ram_amount + round(defending_ram_arc*defense_which_died)
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_arc > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + round(defending_catapult_arc*defense_which_died)
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_arc > 0:
                def_dead_noble_amount = def_dead_noble_amount + round(defending_noble_arc*defense_which_died)
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0
        if new_def_power_arc <= 0:
            def_power_arc = 0
            try:
                att_power_arc_amount = 100 / att_power_arc
            except ZeroDivisionError:
                att_power_arc_amount = 100
            attack_which_died = att_power_arc_amount*ded_att_power_arc/100
            if attacking_archer_amount > 0:
                att_dead_archer_amount = att_dead_archer_amount + int(attacking_archer_amount*attack_which_died)
                attacking_archer_amount = attacking_archer_amount - int(att_dead_archer_amount)
                if attacking_archer_amount <= 0:
                    attacking_archer_amount = 0
            if attacking_mounted_arch_amount > 0:
                att_dead_mounted_arch_amount = att_dead_mounted_arch_amount + int(attacking_mounted_arch_amount*attack_which_died)
                attacking_mounted_arch_amount = attacking_mounted_arch_amount - int(att_dead_mounted_arch_amount)
                if attacking_mounted_arch_amount <= 0:
                    attacking_mounted_arch_amount = 0
            if attacking_catapult_amount > 0:
                att_dead_catapult_amount = att_dead_catapult_amount + int(attacking_catapult_amount*attack_which_died)
                attacking_catapult_amount = attacking_catapult_amount - int(att_dead_catapult_amount)
                if attacking_catapult_amount <= 0:
                    attacking_catapult_amount = 0
            if defending_spear_man_arc > 0:
                def_dead_spear_man_amount = def_dead_spear_man_amount + defending_spear_man_arc
                defending_spear_man_amount = pre_war_spear_man_amount - int(def_dead_spear_man_amount)
                if defending_spear_man_amount <= 0:
                    defending_spear_man_amount = 0
            if defending_sword_man_arc > 0:
                def_dead_sword_man_amount = def_dead_sword_man_amount + defending_sword_man_arc
                defending_sword_man_amount = pre_war_sword_man_amount - int(def_dead_sword_man_amount)
                if defending_sword_man_amount <= 0:
                    defending_sword_man_amount = 0
            if defending_brute_arc > 0:
                def_dead_brute_amount = def_dead_brute_amount + defending_brute_arc
                defending_brute_amount = pre_war_brute_amount - int(def_dead_brute_amount)
                if defending_brute_amount <= 0:
                    defending_brute_amount = 0
            if defending_archer_arc > 0:
                def_dead_archer_amount = def_dead_archer_amount + defending_archer_arc
                defending_archer_amount = pre_war_archer_amount - int(def_dead_archer_amount)
                if defending_archer_amount <= 0:
                    defending_archer_amount = 0
            if defending_scout_arc > 0:
                def_dead_scout_amount = def_dead_scout_amount + defending_scout_arc
                defending_scout_amount = pre_war_scout_amount - int(def_dead_scout_amount)
                if defending_scout_amount <= 0:
                    defending_scout_amount = 0
            if defending_light_cav_arc > 0:
                def_dead_light_cav_amount = def_dead_light_cav_amount + defending_light_cav_arc
                defending_light_cav_amount = pre_war_light_cav_amount - int(def_dead_light_cav_amount)
                if defending_light_cav_amount <= 0:
                    defending_light_cav_amount = 0
            if defending_heavy_cav_arc > 0:
                def_dead_heavy_cav_amount = def_dead_heavy_cav_amount + defending_heavy_cav_arc
                defending_heavy_cav_amount = pre_war_heavy_cav_amount - int(def_dead_heavy_cav_amount)
                if defending_heavy_cav_amount <= 0:
                    defending_heavy_cav_amount = 0
            if defending_mounted_arch_arc > 0:
                def_dead_mounted_arch_amount = def_dead_mounted_arch_amount + defending_mounted_arch_arc
                defending_mounted_arch_amount = pre_war_mounted_arch_amount - int(def_dead_mounted_arch_amount)
                if defending_mounted_arch_amount <= 0:
                    defending_mounted_arch_amount = 0
            if defending_ram_arc > 0:
                def_dead_ram_amount = def_dead_ram_amount + defending_ram_arc
                defending_ram_amount = pre_war_ram_amount - int(def_dead_ram_amount)
                if defending_ram_amount <= 0:
                    defending_ram_amount = 0
            if defending_catapult_arc > 0:
                def_dead_catapult_amount = def_dead_catapult_amount + defending_catapult_arc
                defending_catapult_amount = pre_war_catapult_amount - int(def_dead_catapult_amount)
                if defending_catapult_amount <= 0:
                    defending_catapult_amount = 0
            if defending_noble_arc > 0:
                def_dead_noble_amount = def_dead_noble_amount + defending_noble_arc
                defending_noble_amount = pre_war_noble_amount - int(def_dead_noble_amount)
                if defending_noble_amount <= 0:
                    defending_noble_amount = 0

            #   Stopping the loop
        if (def_power_inf == 0 and def_power_cav == 0 and def_power_arc == 0) or (att_power_inf == 0 and att_power_cav == 0 and att_power_arc == 0):
            break

    old_wall_level = villagedao.get_wall_level(due_march.to_village_id)
    loyalty_text = ''
    conquest_text = ''
    attack_loot_text = 'You looted:\n<i>None</i>'
    defend_loot_text = 'You lost:\n<i>None</i>'
    old_wall_level = 0
    new_wall_level = 0
    old_scout_wall_level = 0
    new_scout_wall_level = 0
    scout_report_text = '👁Intel:\n<i>None</i>'
    check_if_support = wardao.check_if_village_contains_support(due_march.to_village_id)
    attacker_opponents_defeated = 0
    defender_opponents_defeated = 0
    attacker_opponents_defeated = (def_dead_spear_man_amount + def_dead_sword_man_amount + def_dead_brute_amount + def_dead_archer_amount) + (def_dead_scout_amount*2) + (def_dead_light_cav_amount*4) + (def_dead_heavy_cav_amount*6) + ((def_dead_mounted_arch_amount + def_dead_ram_amount)*5) + (def_dead_catapult_amount*8) + (def_dead_noble_amount*100)
    defender_opponents_defeated = (att_dead_spear_man_amount + att_dead_sword_man_amount + att_dead_brute_amount + att_dead_archer_amount) + (att_dead_scout_amount*2) + (att_dead_light_cav_amount*4) + (att_dead_heavy_cav_amount*6) + ((att_dead_mounted_arch_amount + att_dead_ram_amount)*5) + (att_dead_catapult_amount*8) + (att_dead_noble_amount*100)
    looted_resources = '<i>No resources looted</i>'

    if att_power_inf == 0 and att_power_cav == 0 and att_power_arc == 0:
        attacker_report_title = '🔴Attack on ' + target_village_name + ' lost'
        if due_march.target_owner != None:
            defending_player.defeated_units_defense = defending_player.defeated_units_defense + defender_opponents_defeated
            session.add(defending_player)
        if total_att_power > 0:
            defending_troops.spear_man = int(defending_troops.spear_man*(wardao.percentage_devided_by_amount(100, pre_war_spear_man_amount)*defending_spear_man_amount/100))
            defending_troops.sword_man = int(defending_troops.sword_man*(wardao.percentage_devided_by_amount(100, pre_war_sword_man_amount)*defending_sword_man_amount/100))
            defending_troops.brute = int(defending_troops.brute*(wardao.percentage_devided_by_amount(100, pre_war_brute_amount)*defending_brute_amount/100))
            defending_troops.archer = int(defending_troops.archer*(wardao.percentage_devided_by_amount(100, pre_war_archer_amount)*defending_archer_amount/100))
            defending_troops.scout = int(defending_troops.scout*(wardao.percentage_devided_by_amount(100, pre_war_scout_amount)*defending_scout_amount/100))
            defending_troops.light_cav = int(defending_troops.light_cav*(wardao.percentage_devided_by_amount(100, pre_war_light_cav_amount)*defending_light_cav_amount/100))
            defending_troops.heavy_cav = int(defending_troops.heavy_cav*(wardao.percentage_devided_by_amount(100, pre_war_heavy_cav_amount)*defending_heavy_cav_amount/100))
            defending_troops.mounted_arch = int(defending_troops.mounted_arch*(wardao.percentage_devided_by_amount(100, pre_war_mounted_arch_amount)*defending_mounted_arch_amount/100))
            defending_troops.ram = int(defending_troops.ram*(wardao.percentage_devided_by_amount(100, pre_war_ram_amount)*defending_ram_amount/100))
            defending_troops.catapult = int(defending_troops.catapult*(wardao.percentage_devided_by_amount(100, pre_war_catapult_amount)*defending_catapult_amount/100))
            defending_troops.noble = round(defending_troops.noble*(wardao.percentage_devided_by_amount(100, pre_war_noble_amount)*defending_noble_amount/100))
            session.add(defending_troops)
        if check_if_support != None:
            for grab_support in session.query(Support).filter(Support.in_village_id == due_march.to_village_id).all():
                update_support = session.query(Support).filter(Support.pk == grab_support.pk).first()
                support_report = Reports()
                units_defending = troo.village_overview_rally_point_support(update_support.pk,update_support.in_village_id)
                update_support.spear_man = int(update_support.spear_man*(wardao.percentage_devided_by_amount(100, pre_war_spear_man_amount)*defending_spear_man_amount/100))
                update_support.sword_man = int(update_support.sword_man*(wardao.percentage_devided_by_amount(100, pre_war_sword_man_amount)*defending_sword_man_amount/100))
                update_support.brute = int(update_support.brute*(wardao.percentage_devided_by_amount(100, pre_war_brute_amount)*defending_brute_amount/100))
                update_support.archer = int(update_support.archer*(wardao.percentage_devided_by_amount(100, pre_war_archer_amount)*defending_archer_amount/100))
                update_support.scout = int(update_support.scout*(wardao.percentage_devided_by_amount(100, pre_war_scout_amount)*defending_scout_amount/100))
                update_support.light_cav = int(update_support.light_cav*(wardao.percentage_devided_by_amount(100, pre_war_light_cav_amount)*defending_light_cav_amount/100))
                update_support.heavy_cav = int(update_support.heavy_cav*(wardao.percentage_devided_by_amount(100, pre_war_heavy_cav_amount)*defending_heavy_cav_amount/100))
                update_support.mounted_arch = int(update_support.mounted_arch*(wardao.percentage_devided_by_amount(100, pre_war_mounted_arch_amount)*defending_mounted_arch_amount/100))
                update_support.ram = int(update_support.ram*(wardao.percentage_devided_by_amount(100, pre_war_ram_amount)*defending_ram_amount/100))
                update_support.catapult = int(update_support.catapult*(wardao.percentage_devided_by_amount(100, pre_war_catapult_amount)*defending_catapult_amount/100))
                update_support.noble = round(update_support.noble*(wardao.percentage_devided_by_amount(100, pre_war_noble_amount)*defending_noble_amount/100))
                support_loses_list = []
                unit1 = str(update_support.spear_man)
                unit2 = str(update_support.sword_man)
                unit3 = str(update_support.brute)
                unit4 = str(update_support.archer)
                unit5 = str(update_support.scout)
                unit6 = str(update_support.light_cav)
                unit7 =  str(update_support.heavy_cav)
                unit8 = str(update_support.mounted_arch)
                unit9 = str(update_support.ram)
                unit10 = str(update_support.catapult)
                unit11 = str(update_support.noble)
                support_loses_list.append(unit1)
                support_loses_list.append(unit2)
                support_loses_list.append(unit3)
                support_loses_list.append(unit4)
                support_loses_list.append(unit5)
                support_loses_list.append(unit6)
                support_loses_list.append(unit7)
                support_loses_list.append(unit8)
                support_loses_list.append(unit9)
                support_loses_list.append(unit10)
                support_loses_list.append(unit11)
                filter_list = []
                for value in support_loses_list:
                    if value != None:
                        filter_list.append(value)
                filter_list = list(filter(None, filter_list))
                if not filter_list:
                    support_units_death = 'None'
                support_units_death = ''.join(filter_list)
                check_if_support_left = update_support.spear_man + update_support.sword_man + update_support.brute + update_support.archer + update_support.scout + update_support.light_cav + update_support.heavy_cav + update_support.mounted_arch + update_support.ram + update_support.catapult + update_support.noble
                if check_if_support_left > 0:
                    support_report.owner = update_support.owner
                    support_report.title = '🛡💥Support in ' + target_village_name + ' under attack'
                    support_report.report = '<i>But there are still some alive!</i>'
                    support_report.read = 0
                    session.add(support_report)
                    session.add(update_support)
                    session.commit()
                if check_if_support_left == 0:
                    support_report.owner = update_support.owner
                    support_report.title = '🛡☠Support in ' + target_village_name + ' died'
                    support_report.report = '<i>They fought with honour.</i>'
                    support_report.read = 0
                    session.add(support_report)
                    session.delete(update_support)
                    session.commit()

        if attacker_opponents_defeated > 0:
            attacking_player.defeated_units_attack = attacking_player.defeated_units_attack + attacker_opponents_defeated
            session.add(attacking_player)
            defender_report_title = '🟠Defence in ' + target_village_name + ' won'
        if attacker_opponents_defeated == 0:
            defender_report_title = '🟢Defence in ' + target_village_name + ' won'
        if attacking_ram_amount > 0:
            old_wall_level = villagedao.get_wall_level(due_march.to_village_id)
            new_wall_level = old_wall_level - int(attacking_ram_amount/(4*1.09**old_wall_level))
            if new_wall_level > 20:
                new_wall_level = 20
            if new_wall_level < 0:
                new_wall_level = 0
            defending_building.wall_level = new_wall_level
            session.add(defending_building)
        if attacking_noble_amount > 0:
            att_dead_noble_amount = attacking_noble_amount
            attacking_noble_amount = attacking_noble_amount - attacking_noble_amount
        if total_att_power > 0:
            if attacking_scout_amount > 0:
                arrival_time = wardao.calculate_arrival_time_manual(due_march.from_village_id, due_march.to_village_id, due_march.slowest_unit_time)
                #   Setting return for scouts if any
                new_march.owner_pk = due_march.owner_pk
                new_march.from_village_id = due_march.from_village_id
                new_march.target_owner = due_march.target_owner
                new_march.to_village_id = due_march.to_village_id
                new_march.arrival_time = arrival_time
                new_march.type_march = 'RETURN'
                new_march.slowest_unit_time = due_march.slowest_unit_time
                new_march.spear_man = 0
                new_march.sword_man = 0
                new_march.brute = 0
                new_march.archer = 0
                new_march.scout = attacking_scout_amount
                new_march.light_cav = 0
                new_march.heavy_cav = 0
                new_march.mounted_arch = 0
                new_march.ram = 0
                new_march.catapult = 0
                new_march.noble = 0
                new_march.looted_wood = 0
                new_march.looted_stone = 0
                new_march.looted_iron = 0
                session.add(new_march)
                total_scouts = attacking_scout_amount + att_dead_scout_amount
                scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
                if scouts_percentage > 75 and scouts_percentage <=100:
                    old_scout_wall_level = old_wall_level
                    new_scout_wall_level = new_wall_level
                    wall_message = ''
                    troops_in_village = troo.village_overview_rally_point(due_march.to_village_id)
                    if attacking_ram_amount > 0:
                        if old_scout_wall_level > new_scout_wall_level:
                            wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + str(int(new_wall_level)) + '.\n'
                            resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                            scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                    if attacking_ram_amount == 0:
                        old_wall_level = int(villagedao.get_wall_level(due_march.to_village_id))
                        wall_message = 'Wall level ' + str(int(old_wall_level)) + '.\n'
                        resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                        scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                if scouts_percentage >= 51 and scouts_percentage <=75:
                    old_scout_wall_level = old_wall_level
                    new_scout_wall_level = new_wall_level
                    wall_message = ''
                    if old_scout_wall_level > new_scout_wall_level:
                        wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + new_wall_level + '.\n'
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + wall_message + resources
                if scouts_percentage >= 25 and scouts_percentage <= 50:
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + resources
                if scouts_percentage < 25:
                    scout_report_text = '👁Intel:\n<i>None</i>'
        if total_att_power == 0:
            if attacking_scout_amount > 0:
                arrival_time = wardao.calculate_arrival_time_manual(due_march.from_village_id, due_march.to_village_id, due_march.slowest_unit_time)
                #   Setting return for scouts if any
                new_march.owner_pk = due_march.owner_pk
                new_march.from_village_id = due_march.from_village_id
                new_march.target_owner = due_march.target_owner
                new_march.to_village_id = due_march.to_village_id
                new_march.arrival_time = arrival_time
                new_march.slowest_unit_time = due_march.slowest_unit_time
                new_march.type_march = 'RETURN'
                new_march.spear_man = 0
                new_march.sword_man = 0
                new_march.brute = 0
                new_march.archer = 0
                new_march.scout = attacking_scout_amount
                new_march.light_cav = 0
                new_march.heavy_cav = 0
                new_march.mounted_arch = 0
                new_march.ram = 0
                new_march.catapult = 0
                new_march.noble = 0
                new_march.looted_wood = 0
                new_march.looted_stone = 0
                new_march.looted_iron = 0
                session.add(new_march)
                total_scouts = attacking_scout_amount + att_dead_scout_amount
                scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
                if scouts_percentage > 75 and scouts_percentage <=100:
                    old_scout_wall_level = old_wall_level
                    wall_message = ''
                    troops_in_village = troo.village_overview_rally_point(due_march.to_village_id)
                    if attacking_ram_amount > 0:
                        new_scout_wall_level = new_wall_level
                        if old_scout_wall_level > new_scout_wall_level:
                            wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + new_wall_level + '.\n'
                            resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                            scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                            attacker_report_title = '🔵Scout succeeded on ' + target_village_name
                            defender_report_title = '🔵Scout by enemy succeeded on ' + target_village_name
                    if attacking_ram_amount == 0:
                        old_wall_level = villagedao.get_wall_level(due_march.to_village_id)
                        wall_message = 'Wall level ' + str(int(old_wall_level)) + '.\n'
                        resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                        scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                        attacker_report_title = '🔵Scout succeeded on ' + target_village_name
                        defender_report_title = '🔵Scout by enemy succeeded on ' + target_village_name
                if scouts_percentage >= 51 and scouts_percentage <=75:
                    old_scout_wall_level = old_wall_level
                    wall_message = ''
                    if old_scout_wall_level > new_scout_wall_level:
                        wall_message = 'Wall level ' + str(int(old_scout_wall_level)) + '.\n'
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + wall_message + resources
                    attacker_report_title = '🔵Scout partly succeeded on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy partly succeeded on ' + target_village_name
                if scouts_percentage >= 25 and scouts_percentage <= 50:
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + resources
                    attacker_report_title = '🔵Scout slightly succeeded on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy slightly succeeded on ' + target_village_name
                if scouts_percentage < 25:
                    scout_report_text = '👁Intel:\n<i>None</i>'
                    attacker_report_title = '🔵Scout failed on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy failed on ' + target_village_name

    if (att_power_inf > 0 or att_power_cav > 0 or att_power_arc > 0) and def_power_inf == 0 and def_power_cav == 0 and def_power_arc == 0:
        defender_report_title = '🔴Defense in ' + target_village_name + ' lost'
        if due_march.target_owner != None:
            defending_player.defeated_units_defense = defending_player.defeated_units_defense + defender_opponents_defeated
            session.add(defending_player)
        if total_att_power > 0:
            defending_troops.spear_man = 0
            defending_troops.sword_man = 0
            defending_troops.brute = 0
            defending_troops.archer = 0
            defending_troops.scout = 0
            defending_troops.light_cav = 0
            defending_troops.heavy_cav = 0
            defending_troops.mounted_arch = 0
            defending_troops.ram = 0
            defending_troops.catapult = 0
            defending_troops.noble = 0
            session.add(defending_troops)
        if check_if_support != None:
            for grab_support in session.query(Support).filter(Support.in_village_id == due_march.to_village_id).all():
                update_support = session.query(Support).filter(Support.pk == grab_support.pk).first()
                support_report = Reports()
                units_defending = troo.village_overview_rally_point_support(update_support.pk,update_support.in_village_id)

                update_support.spear_man = int(update_support.spear_man*(wardao.percentage_devided_by_amount(100, pre_war_spear_man_amount)*defending_spear_man_amount/100))
                update_support.sword_man = int(update_support.sword_man*(wardao.percentage_devided_by_amount(100, pre_war_sword_man_amount)*defending_sword_man_amount/100))
                update_support.brute = int(update_support.brute*(wardao.percentage_devided_by_amount(100, pre_war_brute_amount)*defending_brute_amount/100))
                update_support.archer = int(update_support.archer*(wardao.percentage_devided_by_amount(100, pre_war_archer_amount)*defending_archer_amount/100))
                update_support.scout = int(update_support.scout*(wardao.percentage_devided_by_amount(100, pre_war_scout_amount)*defending_scout_amount/100))
                update_support.light_cav = int(update_support.light_cav*(wardao.percentage_devided_by_amount(100, pre_war_light_cav_amount)*defending_light_cav_amount/100))
                update_support.heavy_cav = int(update_support.heavy_cav*(wardao.percentage_devided_by_amount(100, pre_war_heavy_cav_amount)*defending_heavy_cav_amount/100))
                update_support.mounted_arch = int(update_support.mounted_arch*(wardao.percentage_devided_by_amount(100, pre_war_mounted_arch_amount)*defending_mounted_arch_amount/100))
                update_support.ram = int(update_support.ram*(wardao.percentage_devided_by_amount(100, pre_war_ram_amount)*defending_ram_amount/100))
                update_support.catapult = int(update_support.catapult*(wardao.percentage_devided_by_amount(100, pre_war_catapult_amount)*defending_catapult_amount/100))
                update_support.noble = round(update_support.noble*(wardao.percentage_devided_by_amount(100, pre_war_noble_amount)*defending_noble_amount/100))
                support_loses_list = []
                unit1 = str(update_support.spear_man)
                unit2 = str(update_support.sword_man)
                unit3 = str(update_support.brute)
                unit4 = str(update_support.archer)
                unit5 = str(update_support.scout)
                unit6 = str(update_support.light_cav)
                unit7 =  str(update_support.heavy_cav)
                unit8 = str(update_support.mounted_arch)
                unit9 = str(update_support.ram)
                unit10 = str(update_support.catapult)
                unit11 = str(update_support.noble)
                support_loses_list.append(unit1)
                support_loses_list.append(unit2)
                support_loses_list.append(unit3)
                support_loses_list.append(unit4)
                support_loses_list.append(unit5)
                support_loses_list.append(unit6)
                support_loses_list.append(unit7)
                support_loses_list.append(unit8)
                support_loses_list.append(unit9)
                support_loses_list.append(unit10)
                support_loses_list.append(unit11)
                filter_list = []
                for value in support_loses_list:
                    if value != None:
                        filter_list.append(value)
                filter_list = list(filter(None, filter_list))
                if not filter_list:
                    support_units_death = 'None'
                support_units_death = ''.join(filter_list)
                check_if_support_left = update_support.spear_man + update_support.sword_man + update_support.brute + update_support.archer + update_support.scout + update_support.light_cav + update_support.heavy_cav + update_support.mounted_arch + update_support.ram + update_support.catapult + update_support.noble
                if check_if_support_left >= 0:
                    support_report.owner = update_support.owner
                    support_report.title = '🛡☠Support in ' + target_village_name + ' died'
                    support_report.report = '<i>They fought with honour.</i>'
                    support_report.read = 0
                    session.add(support_report)
                    session.delete(update_support)
                    session.commit()
        if attacker_opponents_defeated > 0:
            attacking_player.defeated_units_attack = attacking_player.defeated_units_attack + attacker_opponents_defeated
            session.add(attacking_player)
            attacker_report_title = '🟠Attack on ' + target_village_name + ' won'
        if attacker_opponents_defeated == 0:
            attacker_report_title = '🟢Attack on ' + target_village_name + ' won'
        if attacking_ram_amount > 0:
            new_wall_level = old_wall_level - int(attacking_ram_amount/(4*1.09**int(old_wall_level)))
            if new_wall_level > 20:
                new_wall_level = 20
            if new_wall_level < 0:
                new_wall_level = 0
            defending_building.wall_level = new_wall_level
            session.add(defending_building)
        conquest_text = ''
        if attacking_noble_amount > 0:
            get_all_dead_att_units = att_dead_spear_man_amount + att_dead_sword_man_amount + att_dead_brute_amount + att_dead_archer_amount + att_dead_scout_amount + att_dead_light_cav_amount + att_dead_heavy_cav_amount + att_dead_mounted_arch_amount + att_dead_ram_amount + att_dead_catapult_amount
            calculate_if_noble_survives = int(100/total_attack_amount*get_all_dead_att_units)
            if calculate_if_noble_survives <= 50:
                update_loyalty = session.query(Village).filter(Village.pk == due_march.to_village_id).first()
                old_loyalty_value = update_loyalty.loyalty
                new_loyalty_value = update_loyalty.loyalty - (random.randint(25,35))
                loyalty_text = 'loyalty dropped from ' + str(int(old_loyalty_value)) + ' to ' + str(int(new_loyalty_value))
                update_loyalty.loyalty = int(new_loyalty_value)
                if update_loyalty.loyalty > 0:
                    session.add(update_loyalty)
                if update_loyalty.loyalty <= 0:
                    conquest_text = '👑'
                    update_loyalty.loyalty = 50
                    update_loyalty.owner_pk = due_march.owner_pk
                    for queue in session.query(Recruitment).filter(Recruitment.village_id==target_village_id).all():
                        killing_queue = session.query(Recruitment).filter(Recruitment.pk==queue.pk).first()
                        session.delete(killing_queue)
                        session.commit()
                    for marches in session.query(Marching).filter(Marching.from_village_id==target_village_id).all():
                        killing_marches = session.query(Marching).filter(Marching.pk==marches.pk).first()
                        session.delete(killing_marches)
                        session.commit()
                    for support in session.query(Support).filter(Support.from_village_id==target_village_id).all():
                        killing_support = session.query(Support).filter(Support.pk==support.pk).first()
                        session.delete(killing_support)
                        session.commit()
                    attacking_noble_amount = 0
                    session.add(update_loyalty)
            if calculate_if_noble_survives > 50:
                att_dead_noble_amount = attacking_noble_amount
                attacking_noble_amount = attacking_noble_amount - attacking_noble_amount
        if total_att_power > 0:
            if attacking_scout_amount >= 0:
                arrival_time = wardao.calculate_arrival_time_manual(due_march.from_village_id, due_march.to_village_id, due_march.slowest_unit_time)
                #   Setting return for scouts if any
                new_march.owner_pk = due_march.owner_pk
                new_march.from_village_id = due_march.from_village_id
                new_march.target_owner = due_march.target_owner
                new_march.to_village_id = due_march.to_village_id
                new_march.arrival_time = arrival_time
                new_march.type_march = 'RETURN'
                new_march.slowest_unit_time = due_march.slowest_unit_time
                new_march.spear_man = due_march.spear_man - int(att_dead_spear_man_amount)
                new_march.sword_man = due_march.sword_man - int(att_dead_sword_man_amount)
                new_march.brute = due_march.brute - int(att_dead_brute_amount)
                new_march.archer = due_march.archer - int(att_dead_archer_amount)
                new_march.scout = due_march.scout - int(att_dead_scout_amount)
                new_march.light_cav = due_march.light_cav - int(att_dead_light_cav_amount)
                new_march.heavy_cav = due_march.heavy_cav - int(att_dead_heavy_cav_amount)
                new_march.mounted_arch = due_march.mounted_arch - int(att_dead_mounted_arch_amount)
                new_march.ram = due_march.ram - int(att_dead_ram_amount)
                new_march.catapult = due_march.catapult - int(att_dead_catapult_amount)
                new_march.noble = attacking_noble_amount
                village_wood = villagedao.get_wood_storage_by_pk(due_march.to_village_id)
                if village_wood == None:
                    village_wood = 0
                village_stone = villagedao.get_stone_storage_by_pk(due_march.to_village_id)
                if village_stone == None:
                    village_stone = 0
                village_iron = villagedao.get_iron_storage_by_pk(due_march.to_village_id)
                if village_iron == None:
                    village_iron = 0
                village_total = village_wood + village_stone + village_iron
                wood_perc = wardao.percentage_devided_by_amount(100,village_total)*village_wood/100
                stone_perc = wardao.percentage_devided_by_amount(100,village_total)*village_stone/100
                iron_perc = wardao.percentage_devided_by_amount(100,village_total)*village_iron/100
                loot_cap = (attacking_spear_man_amount * spear_man_loot_cap) + (attacking_sword_man_amount * sword_man_loot_cap) + (attacking_brute_amount * brute_loot_cap) + (attacking_archer_amount * archer_loot_cap) + (attacking_light_cav_amount * light_cav_loot_cap) + (attacking_heavy_cav_amount * heavy_cav_loot_cap) + (attacking_mounted_arch_amount * mounted_arch_loot_cap)
                village_resource = session.query(Village).filter(Village.pk == due_march.to_village_id).first()
                wood_calculation = wood_perc*loot_cap
                if wood_calculation >= village_wood:
                    wood_calculation = village_wood
                if wood_calculation == 0 or wood_calculation == None:
                    wood_calculation = 0
                stone_calculation = stone_perc*loot_cap
                if stone_calculation >= village_stone:
                    stone_calculation = village_stone
                if stone_calculation == 0 or stone_calculation == None:
                    stone_calculation = 0
                iron_calculation = iron_perc*loot_cap
                if iron_calculation >= village_iron:
                    iron_calculation = village_iron
                if iron_calculation == 0 or iron_calculation == None:
                    iron_calculation = 0
                loot = '🪓' + str(int(wood_calculation)) +' ⛏' + str(int(stone_calculation)) +' 📏' + str(int(iron_calculation))
                attack_loot_text = 'You looted:\n' + loot + '\n'
                defend_loot_text = 'You lost:\n' + loot + '\n'
                village_resource.wood_stock = village_resource.wood_stock - int(wood_calculation)
                village_resource.stone_stock = village_resource.stone_stock - int(stone_calculation)
                village_resource.iron_stock = village_resource.iron_stock - int(iron_calculation)
                new_march.looted_wood = int(wood_calculation)
                new_march.looted_stone = int(stone_calculation)
                new_march.looted_iron = int(iron_calculation)
                session.add(new_march)
                session.add(village_resource)
                total_scouts = attacking_scout_amount + att_dead_scout_amount
                scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
                if scouts_percentage > 75 and scouts_percentage <=100:
                    old_scout_wall_level = old_wall_level
                    wall_message = ''
                    troops_in_village = troo.village_overview_rally_point(due_march.to_village_id)
                    if attacking_ram_amount > 0:
                        new_scout_wall_level = new_wall_level
                        if old_scout_wall_level > new_scout_wall_level:
                            wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + str(int(new_wall_level)) + '.\n'
                            resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                            scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                    if attacking_ram_amount == 0:
                        old_wall_level = villagedao.get_wall_level(due_march.to_village_id)
                        wall_message = 'Wall level ' + str(int(old_wall_level)) + '.\n'
                        resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                        scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                if scouts_percentage >= 51 and scouts_percentage <=75:
                    old_scout_wall_level = old_wall_level
                    wall_message = ''
                    if old_scout_wall_level > new_scout_wall_level:
                        wall_message = 'Wall level ' + str(int(old_scout_wall_level)) + '.\n'
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + wall_message + resources
                if scouts_percentage >= 25 and scouts_percentage <= 50:
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + resources
                if scouts_percentage < 25:
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n<i>None</i>'
        if total_att_power == 0:
            if attacking_scout_amount > 0:
                arrival_time = wardao.calculate_arrival_time_manual(due_march.from_village_id, due_march.to_village_id, due_march.slowest_unit_time)
                #   Setting return for scouts if any
                new_march.owner_pk = due_march.owner_pk
                new_march.from_village_id = due_march.from_village_id
                new_march.target_owner = due_march.target_owner
                new_march.to_village_id = due_march.to_village_id
                new_march.arrival_time = arrival_time
                new_march.type_march = 'RETURN'
                new_march.slowest_unit_time = due_march.slowest_unit_time
                new_march.spear_man = attacking_spear_man_amount
                new_march.sword_man = attacking_sword_man_amount
                new_march.brute = attacking_brute_amount
                new_march.archer = attacking_archer_amount
                new_march.scout = attacking_scout_amount
                new_march.light_cav = attacking_light_cav_amount
                new_march.heavy_cav = attacking_heavy_cav_amount
                new_march.mounted_arch = attacking_mounted_arch_amount
                new_march.ram = attacking_ram_amount
                new_march.catapult = attacking_catapult_amount
                new_march.noble = attacking_noble_amount
                new_march.looted_wood = 0
                new_march.looted_stone = 0
                new_march.looted_iron = 0
                session.add(new_march)
                total_scouts = attacking_scout_amount + att_dead_scout_amount
                scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
                if scouts_percentage > 75 and scouts_percentage <=100:
                    old_scout_wall_level = old_wall_level
                    wall_message = ''
                    troops_in_village = troo.village_overview_rally_point(due_march.to_village_id)
                    if attacking_ram_amount > 0:
                        new_scout_wall_level = new_wall_level
                        if old_scout_wall_level > new_scout_wall_level:
                            wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + new_wall_level + '.\n'
                            resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                            scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                            attacker_report_title = '🔵Scout succeeded on ' + target_village_name
                            defender_report_title = '🔵Scout by enemy succeeded on ' + target_village_name
                    if attacking_ram_amount == 0:
                        old_wall_level = villagedao.get_wall_level(due_march.to_village_id)
                        wall_message = 'Wall level ' + str(int(old_wall_level)) + '.\n'
                        resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                        scout_report_text = '👁Intel:\n' + wall_message + resources + '\nUnits in village:\n' + troops_in_village
                        attacker_report_title = '🔵Scout succeeded on ' + target_village_name
                        defender_report_title = '🔵Scout by enemy succeeded on ' + target_village_name
                if scouts_percentage >= 51 and scouts_percentage <=75:
                    old_scout_wall_level = old_wall_level
                    new_scout_wall_level = new_wall_level
                    wall_message = ''
                    if old_scout_wall_level > new_scout_wall_level:
                        wall_message = 'Wall has decreased from level ' + str(int(old_wall_level)) + ' to ' + new_wall_level + '.\n'
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + wall_message + resources
                    attacker_report_title = '🔵Scout partly succeeded on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy partly succeeded on ' + target_village_name
                if scouts_percentage >= 25 and scouts_percentage <= 50:
                    resources = vill.get_current_stock_by_village_pk(due_march.to_village_id)
                    scout_report_text = '👁Intel:\n' + resources
                    attacker_report_title = '🔵Scout slightly succeeded on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy slightly succeeded on ' + target_village_name
                if scouts_percentage < 25:
                    scout_report_text = '👁Intel:\n<i>None</i>'
                    attacker_report_title = '🔵Scout failed on ' + target_village_name
                    defender_report_title = '🔵Scout by enemy failed on ' + target_village_name

    attacker_damage = '🔱' + str(int(due_march.spear_man)) + ' 💀' + str(int(att_dead_spear_man_amount)) + '\n' + '🗡' + str(int(due_march.sword_man)) + ' 💀' + str(int(att_dead_sword_man_amount)) + '\n' + '🔨' + str(int(due_march.brute)) + ' 💀' + str(int(att_dead_brute_amount)) + '\n' + '🏹' + str(int(due_march.archer)) + ' 💀' + str(int(att_dead_archer_amount)) + '\n' + '🐁' + str(int(due_march.scout)) + ' 💀' + str(int(att_dead_scout_amount)) + '\n' + '🐎' + str(int(due_march.light_cav)) + ' 💀' + str(int(att_dead_light_cav_amount)) + '\n' + '🎠' + str(int(due_march.heavy_cav)) + ' 💀' + str(int(att_dead_heavy_cav_amount)) + '\n' + '🏹🐎' + str(int(due_march.mounted_arch)) + ' 💀' + str(int(att_dead_mounted_arch_amount)) + '\n' + '🥊' + str(int(due_march.ram)) + ' 💀' + str(int(att_dead_ram_amount)) + '\n' + '☄' + str(int(due_march.catapult)) + ' 💀' + str(int(att_dead_catapult_amount)) + '\n' + '👑' + str(int(due_march.noble)) + ' 💀' + str(int(att_dead_noble_amount)) + '\n'
    defender_damage = '🔱' + str(int(pre_war_spear_man_amount)) + ' 💀' + str(int(def_dead_spear_man_amount)) + '\n' + '🗡' + str(int(pre_war_sword_man_amount)) + ' 💀' + str(int(def_dead_sword_man_amount)) + '\n' + '🔨' + str(int(pre_war_brute_amount)) + ' 💀' + str(int(def_dead_brute_amount)) + '\n' + '🏹' + str(int(pre_war_archer_amount)) + ' 💀' + str(int(def_dead_archer_amount)) + '\n' + '🐁' + str(int(pre_war_scout_amount)) + ' 💀' + str(int(def_dead_scout_amount)) + '\n' + '🐎' + str(int(pre_war_light_cav_amount)) + ' 💀' + str(int(def_dead_light_cav_amount)) + '\n' + '🎠' + str(int(pre_war_heavy_cav_amount)) + ' 💀' + str(int(def_dead_heavy_cav_amount)) + '\n' + '🏹🐎' + str(int(pre_war_mounted_arch_amount)) + ' 💀' + str(int(def_dead_mounted_arch_amount)) + '\n' + '🥊' + str(int(pre_war_ram_amount)) + ' 💀' + str(int(def_dead_ram_amount)) + '\n' + '☄' + str(int(pre_war_catapult_amount)) + ' 💀' + str(int(def_dead_catapult_amount)) + '\n' + '👑' + str(int(pre_war_noble_amount)) + ' 💀' + str(int(def_dead_noble_amount)) + '\n'

    attack_view_defender_damage = '🌫🌫🌫🌫🌫'

    if attacking_scout_amount > 0:
        total_scouts = attacking_scout_amount + att_dead_scout_amount
        scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
        if scouts_percentage > 75 and scouts_percentage <=100 or (def_power_inf == 0 and def_power_arc == 0 and def_power_cav == 0):
            attack_view_defender_damage = '🔱' + ' 💀' + str(int(def_dead_spear_man_amount)) + '\n' + '🗡'  + ' 💀' + str(int(def_dead_sword_man_amount)) + '\n' + '🔨' + ' 💀' + str(int(def_dead_brute_amount)) + '\n' + '🏹' + ' 💀' + str(int(def_dead_archer_amount)) + '\n' + '🐁' + ' 💀' + str(int(def_dead_scout_amount)) + '\n' + '🐎' + ' 💀' + str(int(def_dead_light_cav_amount)) + '\n' + '🎠' + ' 💀' + str(int(def_dead_heavy_cav_amount)) + '\n' + '🏹🐎' + ' 💀' + str(int(def_dead_mounted_arch_amount)) + '\n' + '🥊' + ' 💀' + str(int(def_dead_ram_amount)) + '\n' + '☄' + ' 💀' + str(int(def_dead_catapult_amount)) + '\n' + '👑' + ' 💀' + str(int(def_dead_noble_amount)) + '\n'
        elif scouts_percentage <= 75:
            attack_view_defender_damage = '<i>No intel on troops.</i>'
    attacker_report_text = '⚔' + attacker_name + ' <i>ID:' + attacker_id + '</i> VS 🛡' + defender_name + ' <i>ID:' + defender_id + '</i>\n\n⚔<b>' + sender_village_name + '</b> <i>/vil' + sender_village_id + '</i>\n' + attacker_damage + '\n🛡<b>' + target_village_name + '</b> <i>/view_vil' + target_village_id + '</i>\n' + attack_view_defender_damage + '\n' + attack_loot_text + '\n' + scout_report_text + '\n\n' + loyalty_text
    if attacking_scout_amount > 0:
        total_scouts = attacking_scout_amount + att_dead_scout_amount
        scouts_percentage = int(wardao.percentage_devided_by_amount(100, total_scouts)*attacking_scout_amount)
        if scouts_percentage > 75 and scouts_percentage <=100 or (def_power_inf == 0 and def_power_arc == 0 and def_power_cav == 0):
            attacker_report_text = '⚔' + attacker_name + ' <i>ID:' + attacker_id + '</i> VS 🛡' + defender_name + ' <i>ID:' + defender_id + '</i>\n\n⚔<b>' + sender_village_name + '</b> <i>/vil' + sender_village_id + '</i>\n' + attacker_damage + '\n🛡<b>' + target_village_name + '</b> <i>/view_vil' + target_village_id + '</i>\n' + defender_damage + '\n' + attack_loot_text + '\n' + scout_report_text + '\n\n' + loyalty_text
    defender_report_text = '⚔' + attacker_name + ' <i>ID:' + attacker_id + '</i> VS 🛡' + defender_name + ' <i>ID:' + defender_id + '</i>\n\n⚔<b>' + sender_village_name + '</b> <i>/view_vil' + sender_village_id + '</i>\n' + attacker_damage + '\n🛡<b>' + target_village_name + '</b> <i>/vil' + target_village_id + '</i>\n' + defender_damage + '\n' + defend_loot_text + '\n' + scout_report_text + '\n\n' + loyalty_text
    new_attacker_report.owner = due_march.owner_pk
    new_attacker_report.title = conquest_text + attacker_report_title
    new_attacker_report.report = attacker_report_text
    new_attacker_report.read = 0
    session.add(new_attacker_report)
    if due_march.target_owner != None:
        new_defender_report.owner = due_march.target_owner
        new_defender_report.title = conquest_text + defender_report_title
        new_defender_report.report = defender_report_text
        new_defender_report.read = 0
        session.add(new_defender_report)
    session.commit()
    return True

    #attacks
    #infantry = spear, sword, brute, ram
    #cavalry = light_cav, heavy_cav
    #archery = archer, mounted_arch, catapult


    #
    # while both_parties_have_units(attacker, defender):
    # # calculate next iteration of war
    # #here
    #
    # generate_report
    #
    # atk_power = {
    #     'infantry': {
    #         'amount': 7000,
    #         'power': 40,
    #         'total': 280000,
    #         'percentage': 0.4242
    #     },
    #     'cavalary': {
    #
    #     }
    # }
    # attakcers_infantries = atk_power['infantry']
    # attakcers_infantries['percentage']
    # attakcers_infantries['amount'] = calculated_losses
    #
    # atk_power = calculate_offensive_power(due_march)
    # def_power = calculate_defensive_power(attacked_village_id)
    #
    #
    # power_differences = calculate_power_differences(atk_power, def_power)
    #
    # return None