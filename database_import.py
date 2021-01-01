from models.structure import Structure
from models.unit import Unit
from models.structure_resource_production import Structure_Resource_Production
from models.map_gen import Map_Gen
from models.basemodel import Session

# Database pre-loader for structure data

session = Session()

# -------------------------------------------------------
# STRUCTURES WILL BE LOADED FROM HERE WITH BASE STATS:
# -------------------------------------------------------
# Headquarters
new_structure = Structure()
new_structure.structure_name = 'Headquarters'
new_structure.structure_base_points = '10'
new_structure.structure_points_factor = '1.15'
new_structure.structure_min_level = '1'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '90'
new_structure.structure_base_stone_cost = '80'
new_structure.structure_base_iron_cost = '70'
new_structure.structure_base_population_cost = '5'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '900'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Barracks
new_structure = Structure()
new_structure.structure_name = 'Barracks'
new_structure.structure_base_points = '16'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '25'
new_structure.structure_base_wood_cost = '200'
new_structure.structure_base_stone_cost = '170'
new_structure.structure_base_iron_cost = '90'
new_structure.structure_base_population_cost = '7'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.28'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '1800'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Archery
new_structure = Structure()
new_structure.structure_name = 'Archery'
new_structure.structure_base_points = '18'
new_structure.structure_points_factor = '1.14'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '20'
new_structure.structure_base_wood_cost = '220'
new_structure.structure_base_stone_cost = '200'
new_structure.structure_base_iron_cost = '150'
new_structure.structure_base_population_cost = '2'
new_structure.structure_wood_factor = '1.3'
new_structure.structure_stone_factor = '1.32'
new_structure.structure_iron_factor = '1.28'
new_structure.structure_population_factor = '1.1'
new_structure.structure_base_building_time = '3000'
new_structure.structure_building_time_factor = '1.4'
session.add(new_structure)
# Stable
new_structure = Structure()
new_structure.structure_name = 'Stable'
new_structure.structure_base_points = '20'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '20'
new_structure.structure_base_wood_cost = '270'
new_structure.structure_base_stone_cost = '240'
new_structure.structure_base_iron_cost = '260'
new_structure.structure_base_population_cost = '8'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.28'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '6000'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Siege Workshop
new_structure = Structure()
new_structure.structure_name = 'Siege Workshop'
new_structure.structure_base_points = '24'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '15'
new_structure.structure_base_wood_cost = '300'
new_structure.structure_base_stone_cost = '240'
new_structure.structure_base_iron_cost = '260'
new_structure.structure_base_population_cost = '8'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.28'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '6000'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Castle
new_structure = Structure()
new_structure.structure_name = 'Castle'
new_structure.structure_base_points = '512'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '1'
new_structure.structure_base_wood_cost = '15000'
new_structure.structure_base_stone_cost = '25000'
new_structure.structure_base_iron_cost = '10000'
new_structure.structure_base_population_cost = '80'
new_structure.structure_wood_factor = '2'
new_structure.structure_stone_factor = '2'
new_structure.structure_iron_factor = '2'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '64800'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Smithy
new_structure = Structure()
new_structure.structure_name = 'Smithy'
new_structure.structure_base_points = '19'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '20'
new_structure.structure_base_wood_cost = '220'
new_structure.structure_base_stone_cost = '180'
new_structure.structure_base_iron_cost = '240'
new_structure.structure_base_population_cost = '20'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '6000'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Rally Point
new_structure = Structure()
new_structure.structure_name = 'Rally Point'
new_structure.structure_base_points = '0'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '1'
new_structure.structure_base_wood_cost = '10'
new_structure.structure_base_stone_cost = '40'
new_structure.structure_base_iron_cost = '30'
new_structure.structure_base_population_cost = '0'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.26'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '1200'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Market
new_structure = Structure()
new_structure.structure_name = 'Market'
new_structure.structure_base_points = '10'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '25'
new_structure.structure_base_wood_cost = '100'
new_structure.structure_base_stone_cost = '100'
new_structure.structure_base_iron_cost = '100'
new_structure.structure_base_population_cost = '20'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '2700'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Woodcutter
new_structure = Structure()
new_structure.structure_name = 'Woodcutter'
new_structure.structure_base_points = '6'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '50'
new_structure.structure_base_stone_cost = '60'
new_structure.structure_base_iron_cost = '40'
new_structure.structure_base_population_cost = '5'
new_structure.structure_wood_factor = '1.25'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.245'
new_structure.structure_population_factor = '1.155'
new_structure.structure_base_building_time = '900'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Stone Mine
new_structure = Structure()
new_structure.structure_name = 'Stone Mine'
new_structure.structure_base_points = '6'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '65'
new_structure.structure_base_stone_cost = '50'
new_structure.structure_base_iron_cost = '40'
new_structure.structure_base_population_cost = '10'
new_structure.structure_wood_factor = '1.27'
new_structure.structure_stone_factor = '1.265'
new_structure.structure_iron_factor = '1.24'
new_structure.structure_population_factor = '1.14'
new_structure.structure_base_building_time = '900'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Iron Mine
new_structure = Structure()
new_structure.structure_name = 'Iron Mine'
new_structure.structure_base_points = '6'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '75'
new_structure.structure_base_stone_cost = '65'
new_structure.structure_base_iron_cost = '70'
new_structure.structure_base_population_cost = '10'
new_structure.structure_wood_factor = '1.252'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.24'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '1080'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Farm
new_structure = Structure()
new_structure.structure_name = 'Farm'
new_structure.structure_base_points = '5'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '1'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '45'
new_structure.structure_base_stone_cost = '40'
new_structure.structure_base_iron_cost = '30'
new_structure.structure_base_population_cost = '0'
new_structure.structure_wood_factor = '1.3'
new_structure.structure_stone_factor = '1.32'
new_structure.structure_iron_factor = '1.29'
new_structure.structure_population_factor = '1'
new_structure.structure_base_building_time = '1200'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Storage
new_structure = Structure()
new_structure.structure_name = 'Storage'
new_structure.structure_base_points = '6'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '1'
new_structure.structure_max_level = '30'
new_structure.structure_base_wood_cost = '60'
new_structure.structure_base_stone_cost = '50'
new_structure.structure_base_iron_cost = '40'
new_structure.structure_base_population_cost = '0'
new_structure.structure_wood_factor = '1.265'
new_structure.structure_stone_factor = '1.27'
new_structure.structure_iron_factor = '1.245'
new_structure.structure_population_factor = '1.15'
new_structure.structure_base_building_time = '1020'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
# Wall
new_structure = Structure()
new_structure.structure_name = 'Wall'
new_structure.structure_base_points = '8'
new_structure.structure_points_factor = '1.2'
new_structure.structure_min_level = '0'
new_structure.structure_max_level = '20'
new_structure.structure_base_wood_cost = '50'
new_structure.structure_base_stone_cost = '100'
new_structure.structure_base_iron_cost = '20'
new_structure.structure_base_population_cost = '5'
new_structure.structure_wood_factor = '1.26'
new_structure.structure_stone_factor = '1.275'
new_structure.structure_iron_factor = '1.26'
new_structure.structure_population_factor = '1.17'
new_structure.structure_base_building_time = '3600'
new_structure.structure_building_time_factor = '1.2'
session.add(new_structure)
session.commit()

# -------------------------------------------------------
# UNITS WILL BE LOADED FROM HERE WITH BASE STATS:
# -------------------------------------------------------
# Spearman
new_unit = Unit()
new_unit.unit_name = 'Spearman'
new_unit.wood_cost = '50'
new_unit.stone_cost = '30'
new_unit.iron_cost = '10'
new_unit.population_cost = '1'
new_unit.speed = '1080'
new_unit.attack = '10'
new_unit.defence = '15'
new_unit.defence_cav = '45'
new_unit.defence_arc = '20'
new_unit.loot_carry = '25'
new_unit.recruit_time = '1020'
session.add(new_unit)
session.commit()
# Swordman
new_unit = Unit()
new_unit.unit_name = 'Swordman'
new_unit.wood_cost = '30'
new_unit.stone_cost = '30'
new_unit.iron_cost = '70'
new_unit.population_cost = '1'
new_unit.speed = '1320'
new_unit.attack = '25'
new_unit.defence = '50'
new_unit.defence_cav = '15'
new_unit.defence_arc = '40'
new_unit.loot_carry = '15'
new_unit.recruit_time = '1500'
session.add(new_unit)
session.commit()
# Brute
new_unit = Unit()
new_unit.unit_name = 'Brute'
new_unit.wood_cost = '60'
new_unit.stone_cost = '30'
new_unit.iron_cost = '40'
new_unit.population_cost = '1'
new_unit.speed = '1080'
new_unit.attack = '40'
new_unit.defence = '10'
new_unit.defence_cav = '5'
new_unit.defence_arc = '10'
new_unit.loot_carry = '10'
new_unit.recruit_time = '1320'
session.add(new_unit)
session.commit()
# Archer
new_unit = Unit()
new_unit.unit_name = 'Archer'
new_unit.wood_cost = '100'
new_unit.stone_cost = '30'
new_unit.iron_cost = '60'
new_unit.population_cost = '1'
new_unit.speed = '1080'
new_unit.attack = '15'
new_unit.defence = '50'
new_unit.defence_cav = '40'
new_unit.defence_arc = '5'
new_unit.loot_carry = '10'
new_unit.recruit_time = '1800'
session.add(new_unit)
session.commit()
# Scout
new_unit = Unit()
new_unit.unit_name = 'Scout'
new_unit.wood_cost = '50'
new_unit.stone_cost = '50'
new_unit.iron_cost = '20'
new_unit.population_cost = '2'
new_unit.speed = '540'
new_unit.attack = '0'
new_unit.defence = '2'
new_unit.defence_cav = '1'
new_unit.defence_arc = '2'
new_unit.loot_carry = '0'
new_unit.recruit_time = '900'
session.add(new_unit)
session.commit()
# Light Cavalry
new_unit = Unit()
new_unit.unit_name = 'Light Cavalry'
new_unit.wood_cost = '125'
new_unit.stone_cost = '100'
new_unit.iron_cost = '250'
new_unit.population_cost = '4'
new_unit.speed = '600'
new_unit.attack = '130'
new_unit.defence = '30'
new_unit.defence_cav = '40'
new_unit.defence_arc = '30'
new_unit.loot_carry = '80'
new_unit.recruit_time = '1800'
session.add(new_unit)
session.commit()
# Heavy Cavalry
new_unit = Unit()
new_unit.unit_name = 'Heavy Cavalry'
new_unit.wood_cost = '200'
new_unit.stone_cost = '150'
new_unit.iron_cost = '600'
new_unit.population_cost = '6'
new_unit.speed = '660'
new_unit.attack = '150'
new_unit.defence = '200'
new_unit.defence_cav = '80'
new_unit.defence_arc = '180'
new_unit.loot_carry = '50'
new_unit.recruit_time = '3600'
session.add(new_unit)
session.commit()
# Mounted Archer
new_unit = Unit()
new_unit.unit_name = 'Mounted Archer'
new_unit.wood_cost = '250'
new_unit.stone_cost = '100'
new_unit.iron_cost = '150'
new_unit.population_cost = '5'
new_unit.speed = '600'
new_unit.attack = '120'
new_unit.defence = '40'
new_unit.defence_cav = '30'
new_unit.defence_arc = '50'
new_unit.loot_carry = '50'
new_unit.recruit_time = '2700'
session.add(new_unit)
session.commit()
# Ram
new_unit = Unit()
new_unit.unit_name = 'Ram'
new_unit.wood_cost = '300'
new_unit.stone_cost = '200'
new_unit.iron_cost = '200'
new_unit.population_cost = '5'
new_unit.speed = '1800'
new_unit.attack = '2'
new_unit.defence = '20'
new_unit.defence_cav = '50'
new_unit.defence_arc = '20'
new_unit.loot_carry = '0'
new_unit.recruit_time = '4800'
session.add(new_unit)
session.commit()
# Catapult
new_unit = Unit()
new_unit.unit_name = 'Catapult'
new_unit.wood_cost = '320'
new_unit.stone_cost = '400'
new_unit.iron_cost = '100'
new_unit.population_cost = '8'
new_unit.speed = '1800'
new_unit.attack = '150'
new_unit.defence = '250'
new_unit.defence_cav = '400'
new_unit.defence_arc = '100'
new_unit.loot_carry = '0'
new_unit.recruit_time = '7200'
session.add(new_unit)
session.commit()
# Noble
new_unit = Unit()
new_unit.unit_name = 'Noble'
new_unit.wood_cost = '40000'
new_unit.stone_cost = '50000'
new_unit.iron_cost = '50000'
new_unit.population_cost = '100'
new_unit.speed = '2100'
new_unit.attack = '30'
new_unit.defence = '100'
new_unit.defence_cav = '50'
new_unit.defence_arc = '100'
new_unit.loot_carry = '0'
new_unit.recruit_time = '18000'
session.add(new_unit)
session.commit()

# -------------------------------------------------------
# RESOURCE PRODUCTION WILL BE LOADED FROM HERE WITH BASE STATS:
# -------------------------------------------------------
# woodcutter
new_structure_resource = Structure_Resource_Production()
new_structure_resource.name = 'woodcutter'
new_structure_resource.base_production_production = '45'
new_structure_resource.base_population_production = '0'
new_structure_resource.base_capacity = '0'
new_structure_resource.production_factor = '1.163115'
new_structure_resource.population_factor = '0'
new_structure_resource.capacity_factor = '0'
session.add(new_structure_resource)
session.commit()
# stone mine
new_structure_resource = Structure_Resource_Production()
new_structure_resource.name = 'stone mine'
new_structure_resource.base_production_production = '45'
new_structure_resource.base_population_production = '0'
new_structure_resource.base_capacity = '0'
new_structure_resource.production_factor = '1.163115'
new_structure_resource.population_factor = '0'
new_structure_resource.capacity_factor = '0'
session.add(new_structure_resource)
session.commit()
# iron mine
new_structure_resource = Structure_Resource_Production()
new_structure_resource.name = 'iron mine'
new_structure_resource.base_production_production = '45'
new_structure_resource.base_population_production = '0'
new_structure_resource.base_capacity = '0'
new_structure_resource.production_factor = '1.163115'
new_structure_resource.population_factor = '0'
new_structure_resource.capacity_factor = '0'
session.add(new_structure_resource)
session.commit()
# farm
new_structure_resource = Structure_Resource_Production()
new_structure_resource.name = 'farm'
new_structure_resource.base_production_production = '0'
new_structure_resource.base_population_production = '240'
new_structure_resource.base_capacity = '0'
new_structure_resource.production_factor = '0'
new_structure_resource.population_factor = '1.172103'
new_structure_resource.capacity_factor = '0'
session.add(new_structure_resource)
session.commit()
# storage
new_structure_resource = Structure_Resource_Production()
new_structure_resource.name = 'storage'
new_structure_resource.base_production_production = '0'
new_structure_resource.base_population_production = '0'
new_structure_resource.base_capacity = '1000'
new_structure_resource.production_factor = '0'
new_structure_resource.population_factor = '0'
new_structure_resource.capacity_factor = '1.22949345'
session.add(new_structure_resource)
session.commit()
# -------------------------------------------------------
# MAP GENERATION VALUES WILL BE LOADED FROM HERE WITH BASE STATS:
# -------------------------------------------------------
default_map = Map_Gen()
default_map.center_x = '500'
default_map.center_y = '500'
default_map.radius = '1'
default_map.radius_filling = '0.2'
default_map.base_slots = '8'
default_map.attempts = '0'
session.add(default_map)
session.commit()

session.close()
