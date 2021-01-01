from decimal import Decimal

import aiocron
from dao import VillageDao as villagedao
from models.village import Village
from service import ProfileService as prof

session = None


def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/15 * * * *', func=push_resource_production)


def push_resource_production():
    village_pks = villagedao.get_all_village_id()
    storage = 'storage'
    woodcutter = 'woodcutter'
    stone_mine = 'stone mine'
    iron_mine = 'iron mine'
    for village_pk in village_pks:
        max_stock = prof.get_current_capacity_limit(village_pk, storage)
        production_wood = prof.get_village_production(village_pk, woodcutter)
        production_stone = prof.get_village_production(village_pk, stone_mine)
        production_iron = prof.get_village_production(village_pk, iron_mine)
        production_wood = Decimal('{0:.8g}'.format(production_wood / 4))
        production_stone = Decimal('{0:.8g}'.format(production_stone / 4))
        production_iron = Decimal('{0:.8g}'.format(production_iron / 4))
        add_resources = session.query(Village).filter_by(pk=village_pk).first()
        if add_resources.wood_stock + production_wood > max_stock:
            add_resources.wood_stock = max_stock
        else:
            add_resources.wood_stock = add_resources.wood_stock + production_wood

        if add_resources.stone_stock + production_stone > max_stock:
            add_resources.stone_stock = max_stock
        else:
            add_resources.stone_stock = add_resources.stone_stock + production_stone

        if add_resources.iron_stock + production_iron > max_stock:
            add_resources.iron_stock = max_stock
        else:
            add_resources.iron_stock = add_resources.iron_stock + production_iron
        session.add(add_resources)
        session.commit()
