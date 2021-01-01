from sqlalchemy import func

from dao import UserDao as userdao
from dao import WarDao as wardao
from dao import ProfileDao as profiledao
from models.player import Player
from models.reports import Reports
from service import WarService as war

def is_registered(tg_id):
    found_player = userdao.get_player_by_player_id(tg_id)

    if found_player:
        return True
    else:
        return False


def has_unique_player_name(player_name):
    found_player_name = userdao.get_player_name(player_name)

    if found_player_name:
        return True
    else:
        return False


def get_village_owner(village_owner):
    found_village_owner = userdao.get_owner_id(village_owner)

    if found_village_owner:
        return found_village_owner
    else:
        return False


def get_building_current_row(session):
    row = userdao.get_building_current_row(session)

    if row:
        return row


def get_village_current_row(session):
    row = userdao.get_village_current_row(session)

    if row:
        return row


def village_owner_from_selected_village(tg_id):
    owner_check = userdao.owner_check(tg_id)

    if owner_check is True:
        return True
    else:
        return False

def check_report_owner(tg_id, report_id, session):
    owner_check = userdao.report_owner_check(tg_id, report_id)

    if owner_check is True:
        report_title = wardao.fetch_report_title(report_id)
        report_text = wardao.fetch_report(report_id)
        change_view = session.query(Reports).filter(Reports.pk==report_id).first()
        if change_view.read == 0:
            change_view.read = 1
            session.add(change_view)
            session.commit()
        message = '<b>' + report_title + '</b> /delrep_' + str(report_id) + '\n' + report_text
        return message
    else:
        return_message = 'You can\'t access this report.'
        return return_message

def check_report_owner_to_delete(tg_id, report_id, session):
    owner_check = userdao.report_owner_check(tg_id, report_id)

    if owner_check is True:
        report_title = wardao.fetch_report_title(report_id)
        delete_report = session.query(Reports).filter(Reports.pk==report_id).first()
        session.delete(delete_report)
        session.commit()
        message = '<b>' + report_title + '</b> has been deleted.'
        return message
    else:
        return_message = 'You can\'t delete this report.'
        return return_message

def check_reports_delete(tg_id, session):
    player_pk = profiledao.get_player_pk(tg_id)
    counted_reports = session.query(func.count(Reports.read)).filter(Reports.owner==player_pk).scalar()
    counted = counted_reports
    if counted_reports == 0:
        return 'You don\'t have reports to delete!'
    if counted_reports > 0:
        while counted_reports > 0:
            delete_report = session.query(Reports).filter(Reports.owner==player_pk).first()
            session.delete(delete_report)
            session.commit()
            counted_reports = counted_reports - 1
            if counted_reports == 0:
                break
    return 'All ' + str(counted) + ' report(s) are deleted from your account.'

def check_reports_set_to_read(tg_id, session):
    player_pk = profiledao.get_player_pk(tg_id)
    counted_reports = session.query(func.count(Reports.read)).filter(Reports.owner==player_pk).filter(Reports.read==0).scalar()
    counted = counted_reports
    if counted_reports == 0:
        return 'You don\'t have reports to mark as read!'
    if counted_reports > 0:
        while counted_reports > 0:
            read_report = session.query(Reports).filter(Reports.owner==player_pk).filter(Reports.read==0).first()
            read_report.read = 1
            session.add(read_report)
            session.commit()
            counted_reports = counted_reports - 1
            if counted_reports == 0:
                break
    return 'set ' + str(counted) + ' report(s) to read.'

def check_support_owner(tg_id, support_id, session):
    owner_check = userdao.support_owner_check(tg_id, support_id)

    if owner_check is True:
        report_text = war.withdraw_support(support_id, session)
        return report_text
    else:
        return_message = 'You can\'t withdraw troops from others.'
        return return_message