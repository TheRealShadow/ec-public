import aiocron
from dao import VillageDao as villagedao
from models.village import Village

session = None


def init(global_session):
    global session
    session = global_session
    aiocron.crontab('*/30 * * * *', func=push_loyalty)


async def push_loyalty():
    village_pks = villagedao.get_all_village_id()
    for village_pk in village_pks:
        loyalty_generation = 1
        add_loyalty = session.query(Village).filter_by(pk=village_pk).first()
        if add_loyalty.loyalty + loyalty_generation > 100:
            add_loyalty.loyalty = 100
        else:
            add_loyalty.loyalty = add_loyalty.loyalty + loyalty_generation
        session.add(add_loyalty)
        session.commit()
