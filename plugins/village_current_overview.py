import logging

from telethon import events
from telethon.tl.custom import Button

from dao import VillageDao as villagedao
from dao import ResearchDao as researchdao
from models.player import Player
from models.village import Village
from models.building import Building
from service import AuthenticationService as auth, ButtonService as buttons, ProfileService as prof, \
    VillageService as vill, BuildingUpgradeService as buup, TroopsService as tro

logger = logging.getLogger(__name__)

async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(🏛Overview|⬅Back)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    if auth.is_registered(from_id) is True:
                        default_keyboard = buttons.get_default_keyboard(from_id)
                        if auth.village_owner_from_selected_village(from_id) is True:
                            # Pre-loading all variables
                            player = prof.cur_player(from_id)
                            village_name = prof.cur_village(from_id)
                            village_id = prof.cur_village_id(from_id)
                            village_points = prof.get_village_points(from_id)
                            coordinates = villagedao.get_overview_coordinates(village_id)
                            structure = 'headquarters'
                            headquarters = vill.get_structure_level(from_id, structure)
                            headquarters_view = buup.upgrade_view(structure)
                            structure = 'barracks'
                            barracks = vill.get_structure_level(from_id, structure)
                            barracks_view = buup.upgrade_view(structure)
                            barracks_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'archery'
                            archery = vill.get_structure_level(from_id, structure)
                            archery_view = buup.upgrade_view(structure)
                            archery_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'stable'
                            stable = vill.get_structure_level(from_id, structure)
                            stable_view = buup.upgrade_view(structure)
                            stable_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'siege workshop'
                            siege_workshop = vill.get_structure_level(from_id, structure)
                            siege_workshop_view = buup.upgrade_view(structure)
                            siege_workshop_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'castle'
                            castle = vill.get_structure_level(from_id, structure)
                            castle_view = buup.upgrade_view(structure)
                            castle_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'smithy'
                            smithy = vill.get_structure_level(from_id, structure)
                            smithy_view = buup.upgrade_view(structure)
                            smithy_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'rally point'
                            rally_point = vill.get_structure_level(from_id, structure)
                            rally_point_view = buup.upgrade_view(structure)
                            structure = 'market'
                            market = vill.get_structure_level(from_id, structure)
                            market_view = buup.upgrade_view(structure)
                            market_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            structure = 'woodcutter'
                            woodcutter = vill.get_structure_level(from_id, structure)
                            woodcutter_view = buup.upgrade_view(structure)
                            structure = 'stone mine'
                            stone_mine = vill.get_structure_level(from_id, structure)
                            stone_mine_view = buup.upgrade_view(structure)
                            structure = 'iron mine'
                            iron_mine = vill.get_structure_level(from_id, structure)
                            iron_mine_view = buup.upgrade_view(structure)
                            structure = 'farm'
                            farm = vill.get_structure_level(from_id, structure)
                            farm_view = buup.upgrade_view(structure)
                            pop_display = vill.population_display(from_id, structure)
                            structure = 'storage'
                            storage = vill.get_structure_level(from_id, structure)
                            storage_view = buup.upgrade_view(structure)
                            cap_display = vill.capacity_display(from_id, structure)
                            structure = 'wall'
                            wall = vill.get_structure_level(from_id, structure)
                            wall_view = buup.upgrade_view(structure)
                            wall_req = villagedao.get_upgrade_requirement_overview(from_id, structure)
                            stock = vill.get_current_stock(from_id)
                            stock_production = vill.production_display(from_id)
                            troops = tro.village_overview_rally_point(village_id)
                            loyalty = vill.get_loyalty(from_id)
                            current_pouches = researchdao.get_player_pouches(from_id)
                            needed_pouches = researchdao.get_needed_pouches(from_id)

                            await bot.send_message(entity=int(event.chat_id), message=str('👤' + str(player) + '\n'
                                '👝 ' + str(int(current_pouches)) + ' next ' + str(int(needed_pouches)) + '\n\n'

                                '🏯 ' + village_name + '\n'
                                '🗺 ' + coordinates + '\n'
                                '🏆 ' + str(village_points) + '\n'
                                '📦 ' + str(cap_display) + '\n' + stock + '\n' + stock_production + '\n'
                                '👥 ' + pop_display + '\n'
                                '\n'
                                '🏛 Level ' + str(headquarters) + headquarters_view + '\n'
                                '⚔ Level ' + str(barracks) + barracks_view + str(barracks_req) + ' \n'
                                '🏹 Level ' + str(archery) + archery_view + str(archery_req) + ' \n'
                                '🐎 Level ' + str(stable) + stable_view + str(stable_req) + ' \n'
                                '💣 Level ' + str(siege_workshop) + siege_workshop_view + str(siege_workshop_req) + ' \n'
                                '🏰 Level ' + str(
                                castle) + castle_view + str(castle_req) + ' \n'
                                '⚒ Level ' + str(smithy) + smithy_view + str(smithy_req) + ' \n'
                                '⛲ Level ' + str(rally_point) + rally_point_view + ' \n'
                                '⚖ Level ' + str(market) + market_view + str(market_req) + ' \n'
                                '🪓 Level ' + str(woodcutter) + woodcutter_view + ' \n'
                                '⛏ Level ' + str(stone_mine) + stone_mine_view + ' \n'
                                '📏 Level ' + str(iron_mine) + iron_mine_view + ' \n'
                                '🌾 Level ' + str(farm) + farm_view + ' \n'
                                '📦 Level ' + str(storage) + storage_view + ' \n'
                                '🧱 Level ' + str(wall) + wall_view + str(wall_req) + ' \n'
                                '\n' \
                                'At ⛲ Rally Point:\n'
                                + str(troops) + '\n'
                                '\n' \
                                '🕯 Loyalty: ' + str(loyalty))
                                                   ,buttons=default_keyboard , parse_mode='html')

                        else:
                            await bot.send_message(entity=int(event.chat_id), message=str(
                                'This village doesn\'t belong to you! select another one in 🏰List'),buttons=default_keyboard ,parse_mode='html')
