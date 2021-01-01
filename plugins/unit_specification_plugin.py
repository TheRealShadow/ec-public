import logging
import datetime

from telethon import events
from telethon.tl.custom import Button

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from dao import UnitDao as unitdao
from dao import RecruitmentDao as recruitmentdao
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 1:
                        unit_id = 1
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'barracks')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🔱' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                            '<i>They are the pikeman of this world, strong against cavalry, weak against archers and brutes. This unit is mostly advised to be used for defense.</i>\n' \
                            '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥1\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                            '\n' \
                            'Increase the barracks level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 2:
                        unit_id = 2
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'barracks')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🗡' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>They are the swords with shields of this world, strong against infantry, weak against cavalry and archers. This unit is mostly advised to be used for defense.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥1\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the barracks level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 3:
                        unit_id = 3
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'barracks')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🔨' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>They are the fierce warriors of this world, strong against spearman, weak against swordman, cavalry and archers. This unit is mostly advised to be used for attacks.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥1\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the barracks level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 4:
                        unit_id = 4
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'archery')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🏹' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>The ones who will call down the rain of arrows, strong against infantry and cavalry, weak against mounted archers. This unit is mostly advised to be used for defense.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥1\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the archery level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 8:
                        unit_id = 8
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'archery')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🐎🏹' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>The best way to counter a bow, is by being mounted and having a bow! Strong against archers and swordman, weak against spearman. This unit is mostly advised to be used for attacks.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥5\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the archery level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 5:
                        unit_id = 5
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'stable')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🐁' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>Known for stealth operations. Have no attack damage, only gives intel! Horrible in defending. This unit is mostly advised to be used for gathering intel.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥2\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the stable level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 6:
                        unit_id = 6
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'stable')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🐎' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>A fast offensive unit. Strong against swordsman and Heavy cavalry, but weak against spearman and archers. This unit is mostly advised to be used for attack.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥4\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the stable level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 7:
                        unit_id = 7
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'stable')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦' + str(unitdao.get_unit_loot(unit_id))
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🎠' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>Known for their great armor and speed. Strong against infantry and archers, but weak against light cavalry. This unit is mostly advised to be used for defense.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥6\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the stable level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 9:
                        unit_id = 9
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'siege workshop')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦0'
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🥊' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>Ramming every wall down, They have no big value for bonus attack damage, but they will decrease the wall level and this results in a lower bonus defense for the enemy! This unit is mostly advised to be used for attack.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥5\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the siege workshop level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 10:
                        unit_id = 10
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'siege workshop')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦0'
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>☄' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>Raining down boulders of death and destruction. But on the same time, when you have many. They will be great on the defense as well.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥8\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Increase the siege workshop level to speed up recruitment time.'
                        ), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/unit_(\d+)(@.*)?'))
    async def handler(event):
        unit_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(unit_pk) == 11:
                        unit_id = 11
                        unit_name = unitdao.get_unit_name(unit_id)
                        unit_rec_time_calc = str(datetime.timedelta(seconds=unitdao.get_unit_time(unit_id) / 100 * recruitmentdao.get_unit_production_bonus(from_id,'castle')))
                        unit_rec_time = '⏳' + str(str(unit_rec_time_calc).split(".")[0])
                        unit_atk = '⚔' + str(unitdao.get_unit_atk(unit_id))
                        unit_def = '🛡' + str(unitdao.get_unit_def(unit_id))
                        unit_def_cav = ' 🛡🐎' + str(unitdao.get_unit_def_cav(unit_id))
                        unit_def_arc = ' 🛡🏹' + str(unitdao.get_unit_def_arc(unit_id))
                        unit_cost = '🪓' + str(unitdao.get_unit_wood(unit_id)) + ' ⛏' + str(unitdao.get_unit_stone(unit_id)) + ' 📏' + str(unitdao.get_unit_iron(unit_id))
                        unit_loot = ' 📦0'
                        unit_speed = '💨 ' + str(datetime.timedelta(seconds=unitdao.get_unit_speed(unit_id))) + ' per tile'
                        unit_research = unitdao.get_unit_research(from_id, unit_id)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>👑' + str(unit_name) + ' ' + str(unit_research) + '</b>\n' \
                                                                                  '<i>They are the kingsman of this world, They have no actual value for strength in attack or defense and needs to be protected. This unit is used to drop the loyalty of other villages. Once it reaches 0 or lower, this village is yours.</i>\n' \
                                                                                  '\n' \
                            + str(unit_rec_time) + '\n' \
                            + str(unit_cost) + '\n' \
                            + str(unit_atk) + str(unit_loot) + ' 👥100\n' \
                            + str(unit_def) + str(unit_def_cav) + str(unit_def_arc) + '\n' \
                            + str(unit_speed) + '\n' \
                                                '\n' \
                                                'Have a castle level 1 to build one.'
                        ), parse_mode='html')