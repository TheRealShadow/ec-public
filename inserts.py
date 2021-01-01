from service import ConfigService as conf

conf.init()

# 1 - imports

from models.player import Player
from models.village import Village
from models.structure import Structure
from models.building import Building
from models.unit import Unit
from models.structure_resource_production import Structure_Resource_Production
from models.map_gen import Map_Gen
from models.research import Research
from models.troops import Troops
from models.marching import Marching
from models.settings import Settings
from models.recruitment import Recruitment
from models.support import Support
from models.trading import Trading
from models.reports import Reports
from models.prepare_marching import Prepare_marching
from models.basemodel import Session, engine, Base

# CREATE SCHEMA `empireconquest` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci ;

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# create_sample_data(session)
# for instance in session.query(User):
#    print(instance)

# for instance in session.query(Chat):
#    print(instance.name, instance.username, instance.create_date, instance.update_date)

session.close()