import datetime

from sqlalchemy import or_, func

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.troops import Troops
from models.recruitment import Recruitment
from models.structure_resource_production import Structure_Resource_Production
from models.marching import Marching
from models.reports import Reports
from models.support import Support
from models.unit import Unit
from models.marching import Marching
from models.prepare_marching import Prepare_marching
from service import ProfileService as prof, AuthenticationService as auth, VillageService as vill
from dao import RecruitmentDao as recruitmentdao
from dao import VillageDao as villagedao
from dao import MapGenDao as mapgendao
from dao import ProfileDao as profiledao

session = None

def init(global_session):
    global session
    session = global_session

def get_all_due_marchings(session):
    march = session.query(Marching).filter(Marching.arrival_time < datetime.datetime.utcnow()).all()
    if march:
        return march

def get_all_due_preparations(session):
    preparation = session.query(Marching).filter((Marching.update_date + datetime.timedelta(minutes=5)) < datetime.datetime.utcnow()).all()
    if preparation:
        return preparation

def get_spear_from_march(march_id):
    unit = session.query(func.sum(Marching.spear_man)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_sword_from_march(march_id):
    unit = session.query(func.sum(Marching.sword_man)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_brute_from_march(march_id):
    unit = session.query(func.sum(Marching.brute)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_archer_from_march(march_id):
    unit = session.query(func.sum(Marching.archer)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_scout_from_march(march_id):
    unit = session.query(func.sum(Marching.scout)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_light_cav_from_march(march_id):
    unit = session.query(func.sum(Marching.light_cav)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_heavy_cav_from_march(march_id):
    unit = session.query(func.sum(Marching.heavy_cav)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_mounted_arch_from_march(march_id):
    unit = session.query(func.sum(Marching.mounted_arch)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_ram_from_march(march_id):
    unit = session.query(func.sum(Marching.ram)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_catapult_from_march(march_id):
    unit = session.query(func.sum(Marching.catapult)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_noble_from_march(march_id):
    unit = session.query(func.sum(Marching.noble)).filter_by(pk=march_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_spear_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.spear_man)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_sword_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.sword_man)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit
    
def get_brute_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.brute)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit
    
def get_archer_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.archer)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_scout_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.scout)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_light_cav_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.light_cav)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_heavy_cav_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.heavy_cav)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_mounted_arch_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.mounted_arch)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_ram_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.ram)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_catapult_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.catapult)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_noble_from_march_by_from_village_id(village_id):
    unit = session.query(func.sum(Marching.noble)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_spear_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.spear_man)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_sword_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.sword_man)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_brute_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.brute)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_archer_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.archer)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_scout_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.scout)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_light_cav_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.light_cav)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_heavy_cav_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.heavy_cav)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_mounted_arch_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.mounted_arch)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_ram_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.ram)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_catapult_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.catapult)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def get_noble_from_support_from_village_id(village_id):
    unit = session.query(func.sum(Support.noble)).filter_by(from_village_id=village_id).scalar()
    if unit is None or unit == 0:
        unit = 0
        return unit
    elif unit > 0:
        return unit

def fetch_report_title(report_id):
    for text in session.query(Reports.title).filter_by(pk=report_id).first():
        if text:
            return text

def fetch_report(report_id):
    for text in session.query(Reports.report).filter_by(pk=report_id).first():
        if text:
            return text

def attack_on_own_alert(tg_id, target_village):
    owner = prof.cur_player_id(tg_id)
    target_owner = villagedao.get_village_owner_id(target_village)
    if owner == target_owner:
        message = '❗You\'re preparing a march towards yourself!\n'
        return message
    if owner != target_owner:
        return ''

def get_slowest_unit_from_prep_march(current_village):
    prepared_units = []
    for unit_pk in session.query(Prepare_marching.unit).filter_by(sending_village=current_village).all():
        if unit_pk:
            unit = session.query(Unit).filter_by(pk=unit_pk).first()
            if unit:
                prepared_units.append(unit)
    if len(prepared_units) > 0:
        slowest_speed = max(prepared_units, key=lambda unit: unit.speed)
        return slowest_speed.speed
    else:
        return 0

def convert_seconds_to_HH_MM_SS(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def calculate_eta_on_slowest_unit(current_village, target_village):
    slowest_speed = get_slowest_unit_from_prep_march(current_village)
    distance = mapgendao.calculate_village_distance_by_2_pk(current_village, target_village)
    if slowest_speed > 0:
        travel_time_in_seconds = int(slowest_speed) * distance
        travel_time_in_minutes = convert_seconds_to_HH_MM_SS(travel_time_in_seconds)
        current_time = datetime.datetime.utcnow()
        possible_eta = current_time + datetime.timedelta(seconds=travel_time_in_seconds)
        fixed_eta = str(possible_eta).split('.')[0]
        message = ['\nETA: ', fixed_eta, ' UTC | ', travel_time_in_minutes]
        return ''.join(message)
    elif slowest_speed == 0:
        return ''

def calculate_arrival_time_on_slowest_unit(current_village, target_village):
    slowest_speed = get_slowest_unit_from_prep_march(current_village)
    distance = mapgendao.calculate_village_distance_by_2_pk(current_village, target_village)
    if slowest_speed > 0:
        travel_time_in_seconds = int(slowest_speed) * distance
        current_time = datetime.datetime.utcnow()
        possible_eta = current_time + datetime.timedelta(seconds=travel_time_in_seconds)
        return possible_eta

def calculate_arrival_time_manual(current_village, target_village, slowest_speed):
    distance = mapgendao.calculate_village_distance_by_2_pk(current_village, target_village)
    if slowest_speed > 0:
        travel_time_in_seconds = int(slowest_speed) * distance
        current_time = datetime.datetime.utcnow()
        possible_eta = current_time + datetime.timedelta(seconds=travel_time_in_seconds)
        return possible_eta

def get_slowest_unit_from_support(support_id):
    support = session.query(Support).filter(Support.pk==support_id).first()
    if support:
        return support.slowest_unit_time

def calculate_arrival_time_on_slowest_unit_support(support_id, current_village, target_village):
    slowest_speed = get_slowest_unit_from_support(support_id)
    distance = mapgendao.calculate_village_distance_by_2_pk(current_village, target_village)
    if slowest_speed >= 0:
        travel_time_in_seconds = int(slowest_speed) * distance
        current_time = datetime.datetime.utcnow()
        possible_eta = current_time + datetime.timedelta(seconds=travel_time_in_seconds)
        return possible_eta

def get_unit_from_preparation_filtered(unit_pk, village_id):
    marching = session.query(Prepare_marching).filter(Prepare_marching.sending_village==village_id).filter(Prepare_marching.unit==unit_pk).first()
    if marching:
        return marching.amount

def get_unit_from_preparation(unit_pk, village_id):
    marching = get_unit_from_preparation_filtered(unit_pk, village_id)
    if marching is None or marching == 0:
        marching = 0
        return marching
    elif marching > 0:
        return marching

def grab_support_owner_by_pk(support_id):
    support_owner = session.query(Support).filter(Support.pk==support_id).first()
    if support_owner:
        return support_owner.owner

def get_from_village_support(support_id):
    support_owner = session.query(Support).filter(Support.pk==support_id).first()
    if support_owner:
        return support_owner.from_village_id

def get_in_village_support(support_id):
    support_owner = session.query(Support).filter(Support.pk==support_id).first()
    if support_owner:
        return support_owner.in_village_id
    
def get_unit_from_march_id_filtered(march_id, unit):
    marching = session.query(Marching).filter(Marching.pk == march_id).first()
    if marching and unit == 1:
        return marching.spear_man
    if marching and unit == 2:
        return marching.sword_man
    if marching and unit == 3:
        return marching.brute
    if marching and unit == 4:
        return marching.archer
    if marching and unit == 5:
        return marching.scout
    if marching and unit == 6:
        return marching.light_cav
    if marching and unit == 7:
        return marching.heavy_cav
    if marching and unit == 8:
        return marching.mounted_arch
    if marching and unit == 9:
        return marching.ram
    if marching and unit == 10:
        return marching.catapult
    if marching and unit == 11:
        return marching.noble

def get_unit_from_march_id(march_id, unit):
    amount = get_unit_from_march_id_filtered(march_id, unit)
    if amount is None or amount == 0:
        amount = 0
        amount = str(amount)
        return amount
    elif amount > 0:
        if unit == 1:
            return '🔱' + str(amount) + ' '
        if unit == 2:
            return '🗡' + str(amount) + ' '
        if unit == 3:
            return '🔨' + str(amount) + ' '
        if unit == 4:
            return '🏹' + str(amount) + ' '
        if unit == 5:
            return '🐁' + str(amount) + ' '
        if unit == 6:
            return '🐎' + str(amount) + ' '
        if unit == 7:
            return '🎠' + str(amount) + ' '
        if unit == 8:
            return '🏹🐎' + str(amount) + ' '
        if unit == 9:
            return '🥊' + str(amount) + ' '
        if unit == 10:
            return '☄' + str(amount) + ' '
        if unit == 11:
            return '👑' + str(amount) + ' '

def get_unit_from_support_filtered(unit, support_id):
    support_troops = session.query(Support).filter(Support.pk == support_id).first()
    if support_troops and unit == 1:
        return support_troops.spear_man
    if support_troops and unit == 2:
        return support_troops.sword_man
    if support_troops and unit == 3:
        return support_troops.brute
    if support_troops and unit == 4:
        return support_troops.archer
    if support_troops and unit == 5:
        return support_troops.scout
    if support_troops and unit == 6:
        return support_troops.light_cav
    if support_troops and unit == 7:
        return support_troops.heavy_cav
    if support_troops and unit == 8:
        return support_troops.mounted_arch
    if support_troops and unit == 9:
        return support_troops.ram
    if support_troops and unit == 10:
        return support_troops.catapult
    if support_troops and unit == 11:
        return support_troops.noble

def get_unit_from_support(unit, support_id):
    support_troops = get_unit_from_support_filtered(unit, support_id)
    if support_troops is None or support_troops == 0:
        support_troops = 0
        return support_troops
    elif support_troops > 0:
        return support_troops

def get_village_list_status(village_id):
    outgoing_troops = session.query(Marching).filter(Marching.from_village_id==village_id).first()
    attack = session.query(Marching).filter(Marching.to_village_id==village_id).filter(Marching.type_march=='ATTACK').first()
    defense = session.query(Marching).filter(Marching.to_village_id==village_id).filter(Marching.type_march=='SUPPORT').first()
    returning = session.query(Marching).filter(Marching.from_village_id==village_id).filter(Marching.type_march=='RETURN').first()
    markup = []
    if outgoing_troops:
        markup.append('⏩')
    if attack:
        markup.append('🔥')
    if defense:
        markup.append('💧')
    if returning:
        markup.append('↩')
    return ''.join(markup)


def get_defending_units():
    return None

def check_if_village_contains_support(to_village_id):
    support = session.query(Support).filter(Support.in_village_id == to_village_id).first()
    if support:
        return support.pk


def percentage_devided_by_amount(percentage, amount):
    try:
        att_power_arc_amount = percentage / amount
        return att_power_arc_amount
    except ZeroDivisionError:
        att_power_arc_amount = percentage
        return att_power_arc_amount

def get_current_stock_maximum(village_pk):
    structure = 'storage'
    level = villagedao.get_structure_overview_level(village_pk, structure)
    base_cap = villagedao.get_capacity_base()
    cap_factor = villagedao.get_capacity_factor()
    if level is None:
        level = 1
        cap = base_cap * cap_factor ** level
        cap = int(cap)
        return cap
    elif level >= 1:
        level = level - 1
        cap = base_cap * cap_factor ** level
        cap = int(cap)
        return cap

def unread_reports_counter(player_pk):
    unread_int = 0
    unread = session.query(func.count(Reports.read)).filter(Reports.owner==player_pk).filter(Reports.read==unread_int).scalar()
    if unread == 0 or unread == None:
        return 0
    if unread > 0:
        return unread

def unread_reports_counter_button(tg_id):
    player_pk = profiledao.get_player_pk(tg_id)
    counted_reports = unread_reports_counter(player_pk)
    button_text = []
    button_text.append('📯Reports')
    if counted_reports > 0:
        button_text.append(' (')
        button_text.append(str(counted_reports))
        button_text.append(')')
    return ''.join(button_text)

def get_all_defeated_opponents(player_pk):
    opponents_defeated = session.query(Player.total_defeated_units).filter(Player.pk==player_pk).first()
    if opponents_defeated:
        return opponents_defeated[0]

def get_att_defeated_opponents(player_pk):
    opponents_defeated = session.query(Player.defeated_units_attack).filter(Player.pk==player_pk).first()
    if opponents_defeated:
        return opponents_defeated[0]

def get_def_defeated_opponents(player_pk):
    opponents_defeated = session.query(Player.defeated_units_defense).filter(Player.pk==player_pk).first()
    if opponents_defeated:
        return opponents_defeated[0]