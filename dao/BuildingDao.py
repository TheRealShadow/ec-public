import datetime

from sqlalchemy import or_

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure

session = None


def init(global_session):
    global session
    session = global_session


def get_structure_id(structure):
    for structure_id in session.query(Structure.pk).filter_by(structure_name=structure).first():
        if structure_id:
            return structure_id


def get_structure_id_by_id(structure_pk):
    for structure_id in session.query(Building.pk).filter_by(pk=structure_pk).first():
        if structure_id:
            return structure_id


def get_structure_wood_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for wood_base in session.query(Structure.structure_base_wood_cost).filter_by(structure_name=structure).first():
            if wood_base:
                return wood_base


def get_structure_wood_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for wood_factor in session.query(Structure.structure_wood_factor).filter_by(structure_name=structure).first():
            if wood_factor:
                return wood_factor


def get_structure_stone_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for stone_base in session.query(Structure.structure_base_stone_cost).filter_by(
                structure_name=structure).first():
            if stone_base:
                return stone_base


def get_structure_stone_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for stone_factor in session.query(Structure.structure_stone_factor).filter_by(structure_name=structure).first():
            if stone_factor:
                return stone_factor


def get_structure_iron_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for iron_base in session.query(Structure.structure_base_iron_cost).filter_by(structure_name=structure).first():
            if iron_base:
                return iron_base


def get_structure_iron_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for iron_factor in session.query(Structure.structure_iron_factor).filter_by(structure_name=structure).first():
            if iron_factor:
                return iron_factor


def get_structure_pop_base(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_base in session.query(Structure.structure_base_population_cost).filter_by(
                structure_name=structure).first():
            if pop_base:
                return pop_base


def get_structure_pop_factor(structure):
    for structure in session.query(Structure.structure_name).filter_by(structure_name=structure).first():
        for pop_factor in session.query(Structure.structure_population_factor).filter_by(
                structure_name=structure).first():
            if pop_factor:
                return pop_factor
