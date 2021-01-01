from telethon.tl.custom import Button

from dao import UserDao as userdao
from dao import WarDao as wardao

def get_default_keyboard(tg_id):
    reports_text = wardao.unread_reports_counter_button(tg_id)
    pm_start_row_1_buttons = []
    pm_start_row_1_buttons.append(Button.text('🏛Overview', resize=True))
    pm_start_row_1_buttons.append(Button.text('🎪Units', resize=True))
    pm_start_row_1_buttons.append(Button.text('🏰List', resize=True))

    pm_start_row_2_buttons = []
    pm_start_row_2_buttons.append(Button.text('🚩Orders', resize=True))
    pm_start_row_2_buttons.append(Button.text('⚙Settings', resize=True))
    pm_start_row_2_buttons.append(Button.text('🥇Tops', resize=True))

    pm_start_row_3_buttons = []
    pm_start_row_3_buttons.append(Button.text('🗺Map', resize=True))
    pm_start_row_3_buttons.append(Button.text(reports_text, resize=True))

    pm_start_buttons = []
    pm_start_buttons.append(pm_start_row_1_buttons)
    pm_start_buttons.append(pm_start_row_2_buttons)
    pm_start_buttons.append(pm_start_row_3_buttons)
    return pm_start_buttons

def get_toplist_keyboard():
    pm_start_row_1_buttons = []
    pm_start_row_1_buttons.append(Button.text('🏆Top', resize=True))
    pm_start_row_1_buttons.append(Button.text('🏰Top', resize=True))
    pm_start_row_1_buttons.append(Button.text('🏰Avg', resize=True))

    pm_start_row_2_buttons = []
    pm_start_row_2_buttons.append(Button.text('💀Top', resize=True))
    pm_start_row_2_buttons.append(Button.text('💀⚔️Top', resize=True))
    pm_start_row_2_buttons.append(Button.text('💀🛡Top', resize=True))

    pm_start_row_3_buttons = []
    pm_start_row_3_buttons.append(Button.text('⬅Back', resize=True))

    pm_start_buttons = []
    pm_start_buttons.append(pm_start_row_1_buttons)
    pm_start_buttons.append(pm_start_row_2_buttons)
    pm_start_buttons.append(pm_start_row_3_buttons)
    return pm_start_buttons

def get_recruitment_keyboard():
    pm_start_row_1_buttons = []
    pm_start_row_1_buttons.append(Button.text('🔬Research', resize=True))
    pm_start_row_1_buttons.append(Button.text('🎓Recruitment', resize=True))
    pm_start_row_1_buttons.append(Button.text('🏰Nobles', resize=True))

    #    pm_start_row_2_buttons = []
    #    pm_start_row_2_buttons.append(Button.text('☠Top', resize=True))
    #    pm_start_row_2_buttons.append(Button.text('☠⚔Top', resize=True))
    #    pm_start_row_2_buttons.append(Button.text('☠🛡Top', resize=True))

    pm_start_row_3_buttons = []
    pm_start_row_3_buttons.append(Button.text('⬅Back', resize=True))

    pm_start_buttons = []
    pm_start_buttons.append(pm_start_row_1_buttons)
    #    pm_start_buttons.append(pm_start_row_2_buttons)
    pm_start_buttons.append(pm_start_row_3_buttons)
    return pm_start_buttons

def get_noble_keyboard():
    pm_start_row_1_buttons = []
    pm_start_row_1_buttons.append(Button.text('🔬Research', resize=True))
    pm_start_row_1_buttons.append(Button.text('🎓Recruitment', resize=True))
    pm_start_row_1_buttons.append(Button.text('🏰Nobles', resize=True))

    #    pm_start_row_2_buttons = []
    #    pm_start_row_2_buttons.append(Button.text('☠Top', resize=True))
    #    pm_start_row_2_buttons.append(Button.text('☠⚔Top', resize=True))
    #    pm_start_row_2_buttons.append(Button.text('☠🛡Top', resize=True))

    pm_start_row_3_buttons = []
    pm_start_row_3_buttons.append(Button.text('👝Create pouch', resize=True))
    pm_start_row_3_buttons.append(Button.text('⬅Back', resize=True))

    pm_start_buttons = []
    pm_start_buttons.append(pm_start_row_1_buttons)
    #    pm_start_buttons.append(pm_start_row_2_buttons)
    pm_start_buttons.append(pm_start_row_3_buttons)
    return pm_start_buttons

def get_orders_keyboard():
    pm_start_row_1_buttons = []
    pm_start_row_1_buttons.append(Button.text('🚩All Orders', resize=True))
    pm_start_row_1_buttons.append(Button.text('🔥Inc att', resize=True))
    pm_start_row_1_buttons.append(Button.text('💧Inc sup', resize=True))
    pm_start_row_1_buttons.append(Button.text('', resize=True))

    pm_start_row_2_buttons = []
    pm_start_row_2_buttons.append(Button.text('🚩Vill Orders', resize=True))
    pm_start_row_2_buttons.append(Button.text('🔥Inc vill att', resize=True))
    pm_start_row_2_buttons.append(Button.text('💧Inc vill sup', resize=True))

    pm_start_row_3_buttons = []
    pm_start_row_3_buttons.append(Button.text('⬅Back', resize=True))

    pm_start_buttons = []
    pm_start_buttons.append(pm_start_row_1_buttons)
    pm_start_buttons.append(pm_start_row_2_buttons)
    pm_start_buttons.append(pm_start_row_3_buttons)
    return pm_start_buttons