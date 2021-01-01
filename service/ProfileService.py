from dao import ProfileDao as profiledao
from dao import VillageDao as villagedao
from dao import BuildingDao as buildingdao
from models.settings import Settings
from service import ProfileService as prof, BuildingUpgradeService as buup, VillageService as vill


def cur_player(tg_id):
    found_cur_player_name = profiledao.get_player_name(tg_id)

    if found_cur_player_name:
        return found_cur_player_name

def player_name_by_pk(player_pk):
    found_cur_player_name = profiledao.get_player_name_by_pk(player_pk)

    if found_cur_player_name:
        return found_cur_player_name

def cur_player_id(tg_id):
    player_id = profiledao.get_player_pk(tg_id)

    if player_id:
        return player_id

def player_points(tg_id):
    points = profiledao.get_player_points(tg_id)
    if points:
        return points

def player_points_by_pk(player_pk):
    points = profiledao.get_player_points_by_pk(player_pk)
    if points:
        return points

def player_village_points_by_pk(player_pk):
    points = profiledao.player_village_points_by_pk(player_pk)
    if points:
        return points

def fetch_player_telegram_username_by_pk(player_pk):
    username = profiledao.get_username_by_pk(player_pk)
    show_username = profiledao.get_username_setting_by_pk(player_pk)
    if show_username is None or show_username is 0:
        return ''
    elif show_username is 1:
        return_message = '\n🗣 @' + username
        return return_message

def fetch_player_settings(tg_id):
    player_pk = cur_player_id(tg_id)
    setting_name_show = settings_message(player_pk)
    return_message = '<b>⚙Settings</b>\n' \
                     + str(setting_name_show) + '\n<i>/help for help and more information.</i>'
    return return_message

def settings_message(player_pk):
    show_username = profiledao.get_username_setting_by_pk(player_pk)
    show_downgrade = profiledao.get_downgrade_setting_by_pk(player_pk)
    show_notify = profiledao.get_notify_setting_by_pk(player_pk)
    settings_list = []
    if show_username is None or show_username is 0:
        settings_list.append('Display telegram name: ❌ | /enable_name\n')
    if show_username is 1:
        settings_list.append('Display telegram name: ✅ | /disable_name\n')
    if show_downgrade is None or show_username is 0:
        settings_list.append('Display downgrade option: ❌ | /enable_downgrade\n')
    if show_downgrade is 1:
        settings_list.append('Display downgrade option: ✅ | /disable_downgrade\n')
    if show_notify is None or show_username is 0:
        settings_list.append('Get notified on march return: ❌ | /enable_notify\n')
    if show_notify is 1:
        settings_list.append('Get notified on march return: ✅ | /disable_notify\n')
    return ''.join(settings_list)

def set_player_telegram_name_by_pk(tg_id, input, session):
    player_pk = cur_player_id(tg_id)
    if input == '/disable_name':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.show_username = 0
        session.add(set_name)
        session.commit()
        return 'Telegram name won\'t be shown anymore.'
    elif input == '/enable_name':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.show_username = 1
        session.add(set_name)
        session.commit()
        return 'Telegram name is shown on profile.'

def set_player_downgrade_option_by_pk(tg_id, input, session):
    player_pk = cur_player_id(tg_id)
    if input == '/disable_downgrade':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.show_downgrade = 0
        session.add(set_name)
        session.commit()
        return 'downgrade option won\'t be shown anymore.'
    elif input == '/enable_downgrade':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.show_downgrade = 1
        session.add(set_name)
        session.commit()
        return 'downgrade option is shown on buildings.'

def set_disable_notify_option_by_pk(tg_id, input, session):
    player_pk = cur_player_id(tg_id)
    if input == '/disable_notify':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.troop_return_notify = 0
        session.add(set_name)
        session.commit()
        return 'You won\'t be notified anymore when troops returned.'
    elif input == '/enable_notify':
        set_name = session.query(Settings).filter_by(player_pk=player_pk).first()
        set_name.troop_return_notify = 1
        session.add(set_name)
        session.commit()
        return 'You will be notified when troops returned..'

def cur_village(tg_id):
    found_cur_village_name = profiledao.get_cur_village_name(tg_id)

    if found_cur_village_name:
        return found_cur_village_name


def cur_village_id(tg_id):
    found_cur_village_id = profiledao.get_cur_village_id(tg_id)

    if found_cur_village_id:
        return found_cur_village_id

def cur_village_id_by_pk(pk):
    found_cur_village_id = profiledao.get_cur_village_id_by_pk(pk)

    if found_cur_village_id:
        return found_cur_village_id

def cur_march_village_id(tg_id):
    found_cur_march_village_id = profiledao.get_cur_march_village_id(tg_id)

    if found_cur_march_village_id:
        return found_cur_march_village_id


def get_village_points(tg_id):
    current_village = profiledao.get_cur_village_id(tg_id)
    structure = 'headquarters'
    str1 = prof.get_structure_points(tg_id, structure)
    structure = 'barracks'
    str2 = prof.get_structure_points(tg_id, structure)
    structure = 'stable'
    str3 = prof.get_structure_points(tg_id, structure)
    structure = 'siege workshop'
    str4 = prof.get_structure_points(tg_id, structure)
    structure = 'castle'
    str5 = prof.get_structure_points(tg_id, structure)
    structure = 'smithy'
    str6 = prof.get_structure_points(tg_id, structure)
    structure = 'rally point'
    str7 = prof.get_structure_points(tg_id, structure)
    structure = 'market'
    str8 = prof.get_structure_points(tg_id, structure)
    structure = 'woodcutter'
    str9 = prof.get_structure_points(tg_id, structure)
    structure = 'stone mine'
    str10 = prof.get_structure_points(tg_id, structure)
    structure = 'iron mine'
    str11 = prof.get_structure_points(tg_id, structure)
    structure = 'farm'
    str12 = prof.get_structure_points(tg_id, structure)
    structure = 'storage'
    str13 = prof.get_structure_points(tg_id, structure)
    structure = 'wall'
    str14 = prof.get_structure_points(tg_id, structure)
    structure = 'archery'
    str15 = prof.get_structure_points(tg_id, structure)

    if str1:
        points = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11 + str12 + str13 + str14 + str15
        return points

def get_village_overview_points(village_pk):
    structure = 'headquarters'
    str1 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'barracks'
    str2 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'stable'
    str3 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'siege workshop'
    str4 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'castle'
    str5 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'smithy'
    str6 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'rally point'
    str7 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'market'
    str8 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'woodcutter'
    str9 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'stone mine'
    str10 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'iron mine'
    str11 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'farm'
    str12 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'storage'
    str13 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'wall'
    str14 = prof.get_structure_overview_points(village_pk, structure)
    structure = 'archery'
    str15 = prof.get_structure_overview_points(village_pk, structure)

    if str1:
        points = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11 + str12 + str13 + str14 + str15
        return points


def get_structure_points(tg_id, structure):
    level = villagedao.get_structure_level(tg_id, structure)
    base_points = profiledao.get_structure_points_base(structure)
    points_factor = profiledao.get_structure_points_factor(structure)
    if level is None or level == 0:
        level = 0
        return level
    elif base_points is None:
        base_points = 0
        return base_points
    elif level >= 1:
        level = level - 1
        points = base_points * points_factor ** level
        points = int(points)
        return points


def get_structure_overview_points(village_pk, structure):
    level = villagedao.get_structure_overview_level(village_pk, structure)
    base_points = profiledao.get_structure_points_base(structure)
    points_factor = profiledao.get_structure_points_factor(structure)
    if level is None:
        level = 0
        return level
    elif base_points is None:
        base_points = 0
        return base_points
    elif level >= 1:
        level = level - 1
        points = base_points * points_factor ** level
        points = int(points)
        return points

def get_village_used_population(tg_id):
    current_village = profiledao.get_cur_village_id(tg_id)
    structure = 'headquarters'
    str1 = buup.get_used_pop(tg_id, structure)
    structure = 'barracks'
    str2 = buup.get_used_pop(tg_id, structure)
    structure = 'stable'
    str3 = buup.get_used_pop(tg_id, structure)
    structure = 'siege workshop'
    str4 = buup.get_used_pop(tg_id, structure)
    structure = 'castle'
    str5 = buup.get_used_pop(tg_id, structure)
    structure = 'smithy'
    str6 = buup.get_used_pop(tg_id, structure)
    structure = 'rally point'
    str7 = buup.get_used_pop(tg_id, structure)
    structure = 'market'
    str8 = buup.get_used_pop(tg_id, structure)
    structure = 'woodcutter'
    str9 = buup.get_used_pop(tg_id, structure)
    structure = 'stone mine'
    str10 = buup.get_used_pop(tg_id, structure)
    structure = 'iron mine'
    str11 = buup.get_used_pop(tg_id, structure)
    structure = 'farm'
    str12 = buup.get_used_pop(tg_id, structure)
    structure = 'storage'
    str13 = buup.get_used_pop(tg_id, structure)
    structure = 'wall'
    str14 = buup.get_used_pop(tg_id, structure)
    structure = 'archery'
    str15 = buup.get_used_pop(tg_id, structure)

    if str1:
        pop = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11 + str12 + str13 + str14 + str15
        return pop

def get_used_building_population(tg_id, structure):
    level = villagedao.get_structure_level(tg_id, structure)
    base_pop = villagedao.get_population_base()
    pop_factor = villagedao.get_population_factor()
    if level is None:
        level = 0
        return level
    elif base_pop is None:
        base_pop = 0
        return base_pop
    elif level >= 1:
        level = level - 1
        pop = base_pop * pop_factor ** level
        pop = int(pop)
        return pop

def get_structure_id_by_id(structure_pk):
    pk = buildingdao.get_structure_id_by_id(structure_pk)

    if pk:
        return pk

def get_current_population_limit(tg_id, structure):
    structure = 'farm'
    level = villagedao.get_structure_level(tg_id, structure)
    base_pop = villagedao.get_population_base()
    pop_factor = villagedao.get_population_factor()
    if level is None:
        level = 1
        pop = base_pop * pop_factor ** level
        pop = int(pop)
        return pop
    elif level >= 1:
        level = level - 1
        pop = base_pop * pop_factor ** level
        pop = int(pop)
        return pop

def get_current_capacity_limit_overview(tg_id, structure):
    level = villagedao.get_structure_level(tg_id, structure)
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

def get_current_production(tg_id, structure):
    level = villagedao.get_structure_level(tg_id, structure)
    base_pro = villagedao.get_production_base(structure)
    pro_factor = villagedao.get_production_factor(structure)
    if level is None:
        level = 1
        pro = base_pro * pro_factor ** level
        pro = int(pro)
        return pro
    elif level >= 1:
        level = level - 1
        pro = base_pro * pro_factor ** level
        pro = int(pro + 1)
        return pro

def get_village_production(village_pk, structure):
    level = villagedao.get_resource_village_level(village_pk, structure)
    base_pro = villagedao.get_production_base(structure)
    pro_factor = villagedao.get_production_factor(structure)
    if level is None:
        level = 1
        pro = base_pro * pro_factor ** level
        pro = int(pro)
        return pro
    elif level >= 1:
        level = level - 1
        pro = base_pro * pro_factor ** level
        pro = int(pro + 1)
        return pro

def get_current_capacity_limit(village_pk, structure):
    level = villagedao.get_resource_village_level(village_pk, structure)
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

def get_loyalty(village_pk):
    loyalty = villagedao.get_village_loyalty(village_pk)
    if loyalty:
        return loyalty


def fetch_player_notify_on_return_by_pk(player_pk):
    notify_player = profiledao.get_notify_setting_by_pk(player_pk)
    if notify_player is None or notify_player is 0:
        return False
    elif notify_player is 1:
        return True