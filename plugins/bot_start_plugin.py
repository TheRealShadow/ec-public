import re
import logging
import itertools

from telethon import events
from telethon.tl.custom import Button

from models.player import Player
from models.village import Village
from models.building import Building
from models.research import Research
from models.troops import Troops
from models.settings import Settings
from dao import MapGenDao as mapgendao
from service import AuthenticationService as auth, ButtonService as buttons

logger = logging.getLogger(__name__)


async def init(bot, session):
    @bot.on(events.NewMessage(incoming=True, pattern=r"(/start)"))
    async def handler(event):
        if event.is_private:
            message = event.message
            if message:
                sender = message.sender
                if sender:
                    from_id = sender.id
                    first_name = sender.first_name
                    welcome_text = 'Welcome ' + first_name + ' to Empire Conquest.\n \n' \
                                                             'Do you have what it takes to rule an empire? Fight off enemies, create alliances and create a legend for yourself as the Emperor?\n \n' \
                                                             'Then give us your Emperor name.'
                    if auth.is_registered(from_id) is False:
                        # username check on length + special characters (symbols)
                        async with bot.conversation(event.chat_id) as conv:
                            # Asks for question, awaits the reply for this
                            ruler_name_question = await bot.send_message(entity=event.chat_id, message=welcome_text)
                            # Here waits for the response of variable ruler_name_question
                            ruler_name_message = await conv.get_response(message=ruler_name_question, timeout=300)
                            # Set the verification to false, so we can do the check later
                            ruler_name_verification = False
                            # As long ruler_name_verification is not true, keep looping until true
                            while ruler_name_verification is False:
                                if len(ruler_name_message.raw_text) > 25 or len(ruler_name_message.raw_text) < 1:
                                    ruler_name_verification = False
                                    ruler_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                       message='Your Emperor name was either too long or too short, please keep it less than 25 characters, but more than one single character.')
                                    ruler_name_message = await conv.get_response(message=ruler_name_question_retry,
                                                                                 timeout=300)
                                # Does here a check on the characters A-Za (alphabet) and z0-9 (numbers).
                                # Still will keep in a loop until the verification has been set to True once again
                                elif re.match("^[A-Za-z0-9]*$", ruler_name_message.raw_text):
                                    ruler_name_verification = False
                                    if auth.has_unique_player_name(ruler_name_message.raw_text) is True:
                                        ruler_name_verification = False
                                        ruler_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                           message='Emperor name is already taken! get another one.')
                                        ruler_name_message = await conv.get_response(message=ruler_name_question_retry,
                                                                                     timeout=300)
                                    elif auth.has_unique_player_name(ruler_name_message.raw_text) is False:
                                        break
                                else:
                                    ruler_name_verification = False
                                    ruler_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                       message='Your Emperor name can\'t have special characters! You\'re already \'special\' enough.')
                                    ruler_name_message = await conv.get_response(message=ruler_name_question_retry,
                                                                                 timeout=300)
                                    continue
                                    if auth.has_unique_player_name(ruler_name_message.raw_text) is True:
                                        ruler_name_verification = False
                                        ruler_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                           message='Emperor name is already taken! get another one.')
                                        ruler_name_message = await conv.get_response(message=ruler_name_question_retry,
                                                                                     timeout=300)
                                    elif auth.has_unique_player_name(ruler_name_message.raw_text) is False:
                                        break

                            village_name_question = await bot.send_message(entity=event.chat_id,
                                                                           message='Your Emperor name \"' + ruler_name_message.raw_text + '\" has been accepted! But now you need to also chose a name for your village!\nNo worries, you can change this later on if you want.\n\nSo tell us the name for your starting village.')
                            village_name_message = await conv.get_response(message=village_name_question, timeout=300)
                            village_name_verification = False
                            while village_name_verification is False:
                                if len(village_name_message.raw_text) > 30 or len(village_name_message.raw_text) < 1:
                                    village_name_verification = False
                                    village_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                         message='Your village name was either too long or too short, please keep it less than 30 characters, but more than one single character.')
                                    village_name_message = await conv.get_response(message=village_name_question_retry,
                                                                                   timeout=300)
                                    continue
                                elif re.match("^[A-Za-z0-9|\s]*$", ruler_name_message.raw_text):
                                    village_name_verification = False
                                    if auth.has_unique_player_name(ruler_name_message.raw_text) is True:
                                        village_name_verification = False
                                        village_name_question_retry = await bot.send_message(entity=event.chat_id,
                                                                                             message='Emperor name is already taken! get another one.')
                                        village_name_message = await conv.get_response(
                                            message=village_name_question_retry, timeout=300)
                                    elif auth.has_unique_player_name(ruler_name_message.raw_text) is False:
                                        break
                                else:
                                    break

                            # generating coordinates
                            generated_coordinates = mapgendao.generate_coordinates()
                            generated_coordinates = re.split('[(,)]', str(generated_coordinates))
                            x_coord = generated_coordinates[0]
                            y_coord = generated_coordinates[1]
                            x_coord = str(x_coord)
                            x_coord = float(x_coord)
                            x_coord = round(x_coord)
                            x_coord = int(x_coord)
                            y_coord = str(y_coord)
                            y_coord = float(y_coord)
                            y_coord = round(y_coord)
                            y_coord = int(y_coord)
                            # Inserting the following statements to the Database:
                            # Player, village and buildings creation
                            new_player = Player()
                            new_player.username = sender.username
                            new_player.tg_id = sender.id
                            new_player.player_name = ruler_name_message.raw_text
                            new_player.pouches = '0'
                            new_player.points = '47'
                            new_player.villages = '1'
                            new_player.avg_vil_point = '47'
                            new_player.ban_status = '0'
                            new_player.permission_level = '1'
                            new_player.defeated_units_attack = '0'
                            new_player.defeated_units_defense = '0'
                            new_player.total_defeated_units = '0'
                            new_village = Village()
                            new_village.village_name = village_name_message.raw_text
                            new_village.owner = new_player
                            new_village.x_coord = x_coord
                            new_village.y_coord = y_coord
                            new_village.wood_stock = '2000'
                            new_village.stone_stock = '2000'
                            new_village.iron_stock = '2000'
                            new_village.loyalty = '100'
                            new_building = Building()
                            new_building.village_id = new_village
                            new_building.headquarter_level = '1'
                            new_building.barrack_level = '0'
                            new_building.archery_level = '0'
                            new_building.stable_level = '0'
                            new_building.siege_workshop_level = '0'
                            new_building.castle_level = '0'
                            new_building.smithy_level = '0'
                            new_building.rally_point_level = '1'
                            new_building.market_level = '0'
                            new_building.woodcutter_level = '6'
                            new_building.stone_mine_level = '6'
                            new_building.iron_mine_level = '6'
                            new_building.farm_level = '5'
                            new_building.storage_level = '5'
                            new_building.wall_level = '0'
                            new_research = Research()
                            new_research.village_id = new_village
                            new_research.spear_man = 'YES'
                            new_research.sword_man = 'YES'
                            new_research.brute = 'NO'
                            new_research.archer = 'NO'
                            new_research.scout = 'YES'
                            new_research.light_cav = 'NO'
                            new_research.heavy_cav = 'NO'
                            new_research.mounted_arch = 'NO'
                            new_research.ram = 'NO'
                            new_research.catapult = 'NO'
                            new_troops = Troops()
                            new_troops.village_id = new_village
                            new_troops.spear_man = '75'
                            new_troops.sword_man =  '75'
                            new_troops.brute = '0'
                            new_troops.archer = '0'
                            new_troops.scout = '0'
                            new_troops.light_cav = '0'
                            new_troops.heavy_cav = '0'
                            new_troops.mounted_arch = '0'
                            new_troops.ram = '0'
                            new_troops.catapult = '0'
                            new_troops.noble = '0'
                            new_settings = Settings()
                            new_settings.player = new_player
                            new_settings.show_username = '0'
                            new_settings.vacation_stop = '0'
                            new_settings.merged_account = '0'
                            new_settings.show_downgrade = '0'
                            session.add(new_player)
                            session.add(new_village)
                            session.add(new_building)
                            session.add(new_research)
                            session.add(new_troops)
                            session.add(new_settings)
                            session.commit()
                            owner = session.query(Player.pk).filter_by(tg_id=from_id).first()
                            select_village = session.query(Village.pk).filter_by(owner_pk=owner).first()
                            set_village = session.query(Player).filter_by(tg_id=from_id).first()
                            set_village.selected_village = select_village
                            session.add(set_village)
                            session.commit()
                            for _ in itertools.repeat(None, 2):
                                # generating coordinates
                                generated_coordinates = mapgendao.generate_coordinates()
                                generated_coordinates = re.split('[(,)]', str(generated_coordinates))
                                x_coord = generated_coordinates[0]
                                y_coord = generated_coordinates[1]
                                x_coord = str(x_coord)
                                x_coord = float(x_coord)
                                x_coord = round(x_coord)
                                x_coord = int(x_coord)
                                y_coord = str(y_coord)
                                y_coord = float(y_coord)
                                y_coord = round(y_coord)
                                y_coord = int(y_coord)
                                # Inserting the following statements to the Database:
                                # Player, village and buildings creation
                                new_village = Village()
                                new_village.village_name = 'Barbarian'
                                new_village.owner = None
                                new_village.x_coord = x_coord
                                new_village.y_coord = y_coord
                                new_village.wood_stock = '1000'
                                new_village.stone_stock = '1000'
                                new_village.iron_stock = '1000'
                                new_village.loyalty = '100'
                                new_building = Building()
                                new_building.village_id = new_village
                                new_building.headquarter_level = '5'
                                new_building.barrack_level = '0'
                                new_building.archery_level = '0'
                                new_building.stable_level = '0'
                                new_building.siege_workshop_level = '0'
                                new_building.castle_level = '0'
                                new_building.smithy_level = '0'
                                new_building.rally_point_level = '1'
                                new_building.market_level = '0'
                                new_building.woodcutter_level = '25'
                                new_building.stone_mine_level = '25'
                                new_building.iron_mine_level = '25'
                                new_building.farm_level = '1'
                                new_building.storage_level = '25'
                                new_building.wall_level = '0'
                                new_research = Research()
                                new_research.village_id = new_village
                                new_research.spear_man = 'YES'
                                new_research.sword_man = 'NO'
                                new_research.brute = 'NO'
                                new_research.archer = 'NO'
                                new_research.scout = 'YES'
                                new_research.light_cav = 'NO'
                                new_research.heavy_cav = 'NO'
                                new_research.mounted_arch = 'NO'
                                new_research.ram = 'NO'
                                new_research.catapult = 'NO'
                                new_troops = Troops()
                                new_troops.village_id = new_village
                                new_troops.spear_man = '0'
                                new_troops.sword_man =  '0'
                                new_troops.brute = '0'
                                new_troops.archer = '0'
                                new_troops.scout = '0'
                                new_troops.light_cav = '0'
                                new_troops.heavy_cav = '0'
                                new_troops.mounted_arch = '0'
                                new_troops.ram = '0'
                                new_troops.catapult = '0'
                                new_troops.noble = '0'
                                session.add(new_player)
                                session.add(new_village)
                                session.add(new_building)
                                session.add(new_research)
                                session.add(new_troops)
                                session.add(new_village)
                                session.add(new_building)
                                session.commit()

                            default_buttons = buttons.get_default_keyboard(from_id)
                            await bot.send_message(entity=event.chat_id,
                                                   message='Welcome ' + ruler_name_message.raw_text + ' to your empire!\nThe village name you\'ve chosen is ' + village_name_message.raw_text + ' and will be the start of a large <a href=https://telegra.ph/Empire-Conquest-Quick-tips-08-24>Empire</a>.',
                                                   buttons=default_buttons, parse_mode='html', link_preview=False)

                    else:
                        default_buttons = buttons.get_default_keyboard(from_id)
                        await bot.send_message(entity=event.chat_id, message='Resetting keyboard',
                                               buttons=default_buttons)
