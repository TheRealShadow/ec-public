import logging

from telethon import events
from telethon.tl.custom import Button

from dao import RecruitmentDao as recruitmentdao
from dao import VillageDao as villagedao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, RecruitmentService as rec

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🎓Recruitment|/recruitment)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if auth.village_owner_from_selected_village(from_id) is True:
                            # Pre-loading all variables
                            village_name = prof.cur_village(from_id)
                            structure = 'barracks'
                            barracks = vill.get_structure_level(from_id, structure)
                            barracks_units = recruitmentdao.get_building_units(from_id, structure)
                            structure = 'archery'
                            archery = vill.get_structure_level(from_id, structure)
                            archery_units = recruitmentdao.get_building_units(from_id, structure)
                            structure = 'stable'
                            stable = vill.get_structure_level(from_id, structure)
                            stable_units = recruitmentdao.get_building_units(from_id, structure)
                            structure = 'siege workshop'
                            siege_workshop = vill.get_structure_level(from_id, structure)
                            siege_workshop_units = recruitmentdao.get_building_units(from_id, structure)
                            structure = 'castle'
                            castle = vill.get_structure_level(from_id, structure)
                            castle_units = recruitmentdao.get_building_units(from_id, structure)
                            queue = rec.get_current_unit_queue(from_id, session)
                            default_buttons = buttons.get_recruitment_keyboard()
                            await bot.send_message(entity=int(event.chat_id), message=str('<b>🎓Recruitment overview 🏯' + village_name + '</b>\n'
                            '<i>You can recruit multiple units at once by using /recruit_id amount!</i>\n\n'
                            '<b>⚔ Barracks ' + str(barracks) + '\n</b>'
                            + str(barracks_units) +'\n'
                            '<b>🏹 Archery ' + str(archery) + '\n</b>'
                            + str(archery_units) +'\n'
                            '<b>🐎 Stable ' + str(stable) + '\n</b>'
                            + str(stable_units) +'\n'
                            '<b>💣 Siege workshop ' + str(siege_workshop) + '\n</b>'
                            + str(siege_workshop_units) +'\n'
                            '<b>🏰 castle ' + str(castle) + '\n</b>'
                            + str(castle_units) +'\n'
                            '<b>⏳Current queue:</b>\n'
                            + queue + ''), parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r'/recruit_(\d+)( (.*))?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        amount = event.pattern_match.group(3)
        if not amount:
            amount = 1
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        if amount is None:
                            default_buttons = buttons.get_recruitment_keyboard()
                            recruitment = rec.set_recruitment_now(from_id, unit_pk, session)
                            await bot.send_message(entity=event.chat_id,
                                                   message=str(
                                                       recruitment)
                                                   , parse_mode='html', buttons=default_buttons)
                        elif amount:
                            default_buttons = buttons.get_recruitment_keyboard()
                            recruitment = rec.set_recruitment_now_loop(from_id, unit_pk, amount, session)
                            await bot.send_message(entity=event.chat_id,
                                                   message=str(
                                                       recruitment)
                                                   , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(/create_pouch|👝Create pouch)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        pouch_creation = rec.generate_a_pouch(from_id, session)
                        default_buttons = buttons.get_noble_keyboard()
                        await bot.send_message(entity=event.chat_id,
                                               message=str(
                                                   pouch_creation)
                                               , parse_mode='html', buttons=default_buttons)

    @bot.on(events.NewMessage(incoming=True, pattern=r"(🎪Units)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_buttons = buttons.get_recruitment_keyboard()
                        await bot.send_message(entity=event.chat_id,
                                               message=str('Want to check your current troops or research troops? Please check further.')
                                               , parse_mode='html', buttons=default_buttons)