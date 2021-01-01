import logging
import re

from sqlalchemy import func
from telethon import events
from telethon.tl.custom import Button

from dao.WarDao import convert_seconds_to_HH_MM_SS
from models.player import Player
from models.support import Support
from models.village import Village
from models.building import Building
from models.structure import Structure
from dao import TraderDao as traderdao
from dao import VillageDao as villagedao
from dao import ProfileDao as profiledao
from dao import WarDao as wardao
from dao import MapGenDao as mapgendao
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as troo

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 1:
                        structure = 'headquarters'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🏛' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>Upgrading the ' + structure + ' will help you unlock other buildings in the village and will earn you points!</i>\n' \
                                                                                                                                                                                            '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 1:
                        structure = 'headquarters'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 1:
                        structure = 'headquarters'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 2:
                        structure = 'barracks'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>⚔' + structure + ' level ' + str(structure_level) + '</b>\n' \
                            '<i>' + structure + ' will allow you to build infantry. Also upgrading the ' + structure + ' speed up the recruitment time needed for new units</i>\n' \
                            '\n' + str(structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 2:
                        structure = 'barracks'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 2:
                        structure = 'barracks'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 3:
                        structure = 'archery'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🏹' + structure + ' level ' + str(structure_level) + '</b>\n' \
                            '<i>' + structure + ' will allow you to build ranged units. Also upgrading the ' + structure + ' speed up the recruitment time needed for new units</i>\n' \
                            '\n' + str(structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 3:
                        structure = 'archery'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 3:
                        structure = 'archery'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 4:
                        structure = 'stable'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🐎' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' will allow you to build cavalry. Also upgrading the ' + structure + ' speed up the recruitment time needed for new units</i>\n' \
                                                                                                                                                                               '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 4:
                        structure = 'stable'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 4:
                        structure = 'stable'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 5:
                        structure = 'siege workshop'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>💣' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' will allow you to build siege units. Also upgrading the ' + structure + ' speed up the recruitment time needed for new units</i>\n' \
                                                                                                                                                                                   '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 5:
                        structure = 'siege workshop'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 5:
                        structure = 'siege workshop'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 6:
                        structure = 'castle'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🏰' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' will allow you to recruit 👑nobles. To create 1 noble you need one pouch, for a second noble you need 2 pouches and so on...</i>\nUse /create_pouch to make one if you have a castle level 1!\nOne pouch costs 🪓28000 ⛏30000 📏25000\n' \
                                                                                                         '\n' + str(
                                structure_cost)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 6:
                        structure = 'castle'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 6:
                        structure = 'castle'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 7:
                        structure = 'smithy'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>⚒' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                    '<i>' + structure + ' will allow you to research units ' + structure + ' speed up the research time needed for researches.</i>\n' \
                                                                                                                                                           '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 7:
                        structure = 'smithy'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 7:
                        structure = 'smithy'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 8:
                        structure = 'rally point'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 8:
                        structure = 'rally point'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 9:
                        structure = 'market'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        traders = traderdao.trader_display(from_id, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>⚖' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                    '<i>' + structure + ' will allow you to send resources to other villages. Once it\'s destroyed you can\'t send resources and you need to rebuild it.</i>\n\nAvailable 🎭traders: ' + traders + '\n📦1000 💨 0:04:00 per tile /trades \nIf you wish to trade with the NPC, use /pve_trader\n' \
                                                                                                        '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 9:
                        structure = 'market'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 9:
                        structure = 'market'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 10:
                        structure = 'woodcutter'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🪓' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' will get wood for your village, the amount it will harvest will be displayed in hours on the village overview.</i>\n' \
                                                                                                         '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 10:
                        structure = 'woodcutter'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 10:
                        structure = 'woodcutter'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 11:
                        structure = 'stone mine'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>⛏' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                    '<i>' + structure + ' will get stone for your village, the amount it will harvest will be displayed in hours on the village overview.</i>\n' \
                                                                                                        '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 11:
                        structure = 'stone mine'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 11:
                        structure = 'stone mine'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 12:
                        structure = 'iron mine'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>📏' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' will get iron for your village, the amount it will harvest will be displayed in hours on the village overview.</i>\n' \
                                                                                                         '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 12:
                        structure = 'iron mine'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 12:
                        structure = 'iron mine'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 13:
                        structure = 'farm'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        building_pop = str(prof.get_village_used_population(from_id))
                        troop_pop = str(villagedao.get_all_troops_population(from_id)-villagedao.get_used_troops_in_recruitment_pop(from_id))
                        recruit_pop = str(villagedao.get_used_troops_in_recruitment_pop(from_id))
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🌾' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' decides how much population you can have in your village, once full you can\'t upgrade buildings or recruit anymore units!</i>\n' \
                                                                                                         '\npopulation in buildings: ' + building_pop +
                                                                                                         '\npopulation in troops: ' + troop_pop +
                                                                                                         '\npopulation in recruitment: ' + recruit_pop +
                                                                                                         '\n\n' + str(structure_cost)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 13:
                        structure = 'farm'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 13:
                        structure = 'farm'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 14:
                        structure = 'storage'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>📦' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' decides how much resources you can have in your village, once full you can\'t get more resources from the woodcutter, stone mine or iron mine!</i>\n' \
                                                                                                         '\n' + str(
                                structure_cost)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 14:
                        structure = 'storage'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 14:
                        structure = 'storage'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 15:
                        structure = 'wall'
                        structure_level = vill.get_structure_level(from_id, structure)
                        structure_cost = buup.get_structure_upgrade(from_id, structure)
                        downgrade = buup.get_structure_downgrade(from_id, structure, session)
                        village_pk = prof.cur_village_id(from_id)
                        wall_bonus = villagedao.get_wall_bonus(village_pk)
                        wall_text = 'Current wall defense effectiveness: ' + str(round(wall_bonus*100)-100) + '%'
                        await bot.send_message(entity=int(event.chat_id), message=str(
                            '<b>🧱' + structure + ' level ' + str(structure_level) + '</b>\n' \
                                                                                     '<i>' + structure + ' gives a defensive bonus to the village! The lower the level is, the less effect defending units have.</i>\n' \
                                                                                                         '\n'
                                                                                                         + str(wall_text) + '\n'
                                                                                                         '\n' + str(
                                structure_cost) + '\n' + str(downgrade)), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/upg(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 15:
                        structure = 'wall'
                        upgrade_check = buup.upgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(upgrade_check), parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/dow(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True and int(building_pk) == 15:
                        structure = 'wall'
                        downgrade_check = buup.downgrade_check_action(from_id, structure, session)
                        await bot.send_message(entity=int(event.chat_id), message=str(downgrade_check),
                                               parse_mode='html')

    @bot.on(events.NewMessage(incoming=True, pattern=r'/str(\d+)(@.*)?'))
    async def handler(event):
        building_pk = event.pattern_match.group(1)
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    player_pk = prof.cur_player_id(from_id)
                    if auth.is_registered(from_id) is True and int(building_pk) is 8:
                        await create_support_overview(1, event, True, session, player_pk, bot, from_id)

    @bot.on(events.CallbackQuery(pattern=re.compile(r"supjump_(\d+)", re.DOTALL)))
    async def handler(event):
        page = event.pattern_match.group(1).decode('utf-8')
        from_id = event.sender_id
        if from_id:
            if auth.is_registered(from_id) is True:
                player_pk = prof.cur_player_id(from_id)
                if page:
                    await create_support_overview(int(page), event, False, session, player_pk, bot, from_id)

async def create_support_overview(page, event, send_new, session, player_pk, bot, from_id):
    page_size = 10
    structure = 'rally point'
    structure_level = vill.get_structure_level(from_id, structure)
    structure_cost = buup.get_structure_upgrade(from_id, structure)
    village_id = prof.prof.cur_village_id(from_id)
    offset = ((int(page) - 1) * page_size)
    support_count = session.query(func.count(Support.from_village_id)).filter(Support.from_village_id==village_id).order_by(Support.pk.asc()).scalar()
    if support_count >= 0:
        max_pages = (support_count // page_size)
        if (support_count % page_size) >= 0:
            max_pages += 1
        if page <= max_pages:
            supports = session.query(Support).filter(Support.from_village_id==village_id).order_by(Support.pk.asc()).limit(page_size).offset(offset).all()
            supports_overview_list = ['<b>⛲' + structure + ' level ' + str(structure_level) + '</b>\n<i>' + structure + ' will allow you to send units to attack or support other villages. Once it\'s destroyed you can\'t and need to rebuild it as soon as possible!</i>\n\n' + str(structure_cost) + '\n\n<b>Units Supporting:</b>\n']
            if supports:
                for support in supports:
                    distance = mapgendao.calculate_village_distance_by_2_pk(support.from_village_id, support.in_village_id)
                    travel_time_in_seconds = int(support.slowest_unit_time) * int(distance)
                    travel_time_in_minutes = convert_seconds_to_HH_MM_SS(travel_time_in_seconds)
                    supports_overview_list.append('📍')
                    supports_overview_list.append(str(distance))
                    supports_overview_list.append(' - ')
                    supports_overview_list.append(str(travel_time_in_minutes))
                    supports_overview_list.append(' | <b>🏯')
                    supports_overview_list.append(str(villagedao.get_village_name_by_pk(support.in_village_id)))
                    supports_overview_list.append('</b> - 👤')
                    supports_overview_list.append(str(villagedao.get_village_owner_player_name(support.in_village_id)))
                    supports_overview_list.append('\n')
                    supports_overview_list.append(str(troo.village_overview_rally_point_support(support.pk,support.from_village_id)))
                    supports_overview_list.append('/withdraw_')
                    supports_overview_list.append(str(support.pk))
                    supports_overview_list.append('\n\n')

                supports_overview_list.append('Showing ')
                supports_overview_list.append(str(offset + 1))
                supports_overview_list.append(' to ')
                supports_overview_list.append(str(offset + len(supports)))
                supports_overview_list.append(' from ')
                supports_overview_list.append(str(support_count))
                supports_overview_list.append(' supporting action(s).')

            else:
                supports_overview_list.append('<i>None</i>')


            supports_overview_text = ''.join(supports_overview_list)

            supports_paging_buttons = []

            if page > 1:
                prev_all_button = Button.inline('⏮', bytes('supjump_1', encoding='utf-8'))
                supports_paging_buttons.append(prev_all_button)
                if page >= 6:
                    prev_5_button = Button.inline('⏪', bytes('supjump_' + str(int(page) - 5), encoding='utf-8'))
                    supports_paging_buttons.append(prev_5_button)
                prev_1_button = Button.inline('◀️', bytes('supjump_' + str(int(page) - 1), encoding='utf-8'))
                supports_paging_buttons.append(prev_1_button)

            if page < max_pages:
                next_1_button = Button.inline('▶️', bytes('supjump_' + str(int(page) + 1), encoding='utf-8'))
                supports_paging_buttons.append(next_1_button)

                if (page + 5) <= max_pages:
                    next_5_button = Button.inline('⏩', bytes('supjump_' + str(int(page) + 5), encoding='utf-8'))
                    supports_paging_buttons.append(next_5_button)
                next_all_button = Button.inline('⏭', bytes('supjump_' + str(max_pages), encoding='utf-8'))
                supports_paging_buttons.append(next_all_button)

            if send_new:
                if len(supports_paging_buttons) > 0:
                    await bot.send_message(entity=event.chat_id, message=supports_overview_text, buttons=supports_paging_buttons, parse_mode='html')
                else:
                    await bot.send_message(entity=event.chat_id, message=supports_overview_text, parse_mode='html')
            else:
                if len(supports_paging_buttons) > 0:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=supports_overview_text, buttons=supports_paging_buttons, parse_mode='html')
                else:
                    await bot.edit_message(entity=event.chat_id, message=event.message_id, text=supports_overview_text, parse_mode='html')

