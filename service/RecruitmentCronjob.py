from decimal import Decimal

import aiocron
from dao import VillageDao as villagedao
from dao import RecruitmentDao as recruitmentdao
from models.village import Village
from models.troops import Troops
from service import ProfileService as prof

session = None

def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/1 * * * *', func=add_due_recruitments_to_villages)

def add_due_recruitments_to_villages():
    due_recruitments = recruitmentdao.get_all_due_recruitments()
    if due_recruitments:
        for recruitment in due_recruitments:
            # logic to add that single recruitment to the village
            if recruitment.unit_id is 1:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.spear_man = add_unit_to_village.spear_man + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 2:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.sword_man = add_unit_to_village.sword_man + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 3:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.brute = add_unit_to_village.brute + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 4:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.archer = add_unit_to_village.archer + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 5:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.scout = add_unit_to_village.scout + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 6:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.light_cav = add_unit_to_village.light_cav + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 7:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.heavy_cav = add_unit_to_village.heavy_cav + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 8:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.mounted_arch = add_unit_to_village.mounted_arch + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 9:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.ram = add_unit_to_village.ram + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 10:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.catapult = add_unit_to_village.catapult + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
            elif recruitment.unit_id is 11:
                add_unit_to_village = session.query(Troops).filter_by(village_pk=recruitment.village_id).first()
                add_unit_to_village.noble = add_unit_to_village.noble + 1
                session.add(add_unit_to_village)
                session.delete(recruitment)
        session.commit()
