import datetime
from math import pi, cos, sin, sqrt
from random import random
from decimal import *
import re

from sqlalchemy import or_

from models.player import Player
from models.village import Village
from models.building import Building
from models.structure import Structure
from models.map_gen import Map_Gen
from dao import ProfileDao as profiledao
from dao import VillageDao as villagedao
from dao import MapGenDao as mapgendao
from models.structure_resource_production import Structure_Resource_Production

session = None


def init(global_session):
    global session
    session = global_session


def centre_x():
    center = session.query(Map_Gen.center_x).first()
    if center:
        return center


def centre_y():
    center = session.query(Map_Gen.center_y).first()
    if center:
        return center


def radius():
    for circle_radius in session.query(Map_Gen.radius).first():
        if circle_radius:
            return circle_radius


def radius_fill():
    for filling in session.query(Map_Gen.radius_filling).first():
        if filling:
            return filling


def base():
    base_slots = session.query(Map_Gen.base_slots).first()
    if base_slots:
        return base_slots


def counter():
    for attempts in session.query(Map_Gen.attempts).first():
        if attempts:
            return attempts


def point(x, y, r):
    theta = random() * 2 * pi
    return y + cos(theta) * r, x + sin(theta) * r


def get_x_coordinates():
    x_coords = []
    for fetch_village_x in session.query(Village.x_coord).all():
        if fetch_village_x is None:
            fetch_village_x = 0
        x_coords.append(fetch_village_x)
        return x_coords


def get_y_coordinates():
    y_coords = []
    for fetch_village_y in session.query(Village.y_coord).all():
        if fetch_village_y is None:
            fetch_village_y = 0
        y_coords.append(fetch_village_y)
        return y_coords


def generate_coordinates():
    new_coords_verification = False
    while new_coords_verification is False:
        fetch_village_x = get_x_coordinates()
        fetch_village_y = get_y_coordinates()
        x_size = 500
        y_size = 500
        r_size = radius()
        base_slot = 6
        fill = radius_fill()
        attempt = counter()
        radius_increase = Decimal('{0:.8g}'.format(0.0004))
        maximum_attempts = int((r_size * base_slot) * fill)
        generated_coordinates = [point(x_size, y_size, r_size) for _ in range(1)]
        generated_coordinates = re.split('[(,)]', str(generated_coordinates))
        x_coord = generated_coordinates[1]
        y_coord = generated_coordinates[2]
        x_coord = str(x_coord)
        x_coord = float(x_coord)
        x_coord = round(x_coord)
        x_coord = int(x_coord)
        y_coord = str(y_coord)
        y_coord = float(y_coord)
        y_coord = round(y_coord)
        y_coord = int(y_coord)
        gen_x = str(x_coord)
        gen_y = str(y_coord)
        generated_coordinates = gen_x + ', ' + gen_y
        possible_village = session.query(Village.x_coord).filter(Village.x_coord == x_coord).filter(
            Village.y_coord == y_coord).first()
        if possible_village:
            new_coords_verification = False
        else:
            if attempt is None:
                attempt = 0
                if attempt >= maximum_attempts:
                    new_coords_verification = False
                    inject_map_gen = session.query(Map_Gen).filter_by(center_x=500).first()
                    inject_map_gen.radius = inject_map_gen.radius + 1
                    inject_map_gen.attempts = 0
                    session.add(inject_map_gen)
                    session.commit()
                elif attempt <= maximum_attempts:
                    new_coords_verification = True
                    inject_map_gen = session.query(Map_Gen).filter_by(center_x=500).first()
                    inject_map_gen.attempts = inject_map_gen.attempts + 1
                    inject_map_gen.radius_filling = inject_map_gen.radius_filling + radius_increase
                    session.add(inject_map_gen)
                    session.commit()
                    return generated_coordinates
            elif attempt > 0:
                if attempt >= maximum_attempts:
                    new_coords_verification = False
                    inject_map_gen = session.query(Map_Gen).filter_by(center_x=500).first()
                    inject_map_gen.radius = inject_map_gen.radius + 1
                    inject_map_gen.attempts = 0
                    session.add(inject_map_gen)
                    session.commit()
                elif attempt <= maximum_attempts:
                    new_coords_verification = True
                    inject_map_gen = session.query(Map_Gen).filter_by(center_x=500).first()
                    inject_map_gen.attempts = inject_map_gen.attempts + 1
                    session.add(inject_map_gen)
                    session.commit()
                    return generated_coordinates

def get_village_x_coordinates(village_pk):
    for fetch_village_x in session.query(Village.x_coord).filter_by(pk=village_pk).first():
        if fetch_village_x:
            return fetch_village_x


def get_village_y_coordinates(village_pk):
    for fetch_village_y in session.query(Village.y_coord).filter_by(pk=village_pk).first():
        if fetch_village_y:
            return fetch_village_y

def calculate_village_distance(tg_id, village_pk):
    current_village = profiledao.get_cur_village_id(tg_id)
    current_village_x = get_village_x_coordinates(current_village)
    current_village_y = get_village_y_coordinates(current_village)
    viewing_village_x = get_village_x_coordinates(village_pk)
    viewing_village_y = get_village_y_coordinates(village_pk)
    x_distance = max(current_village_x - viewing_village_x, viewing_village_x - current_village_x)
    y_distance = max(current_village_y - viewing_village_y, viewing_village_y - current_village_y)
    distance = sqrt(x_distance**2+y_distance**2)
    if distance == None or distance == 0:
        distance = 0
        return distance
    elif distance:
        distance = round(distance, 1)
        return distance

def calculate_village_distance_by_2_pk(village_pk1, village_pk2):
    current_village_x = get_village_x_coordinates(village_pk1)
    current_village_y = get_village_y_coordinates(village_pk1)
    viewing_village_x = get_village_x_coordinates(village_pk2)
    viewing_village_y = get_village_y_coordinates(village_pk2)
    x_distance = max(current_village_x - viewing_village_x, viewing_village_x - current_village_x)
    y_distance = max(current_village_y - viewing_village_y, viewing_village_y - current_village_y)
    distance = sqrt(x_distance**2+y_distance**2)
    if distance == None or distance == 0:
        distance = 0
        return distance
    elif distance:
        distance = round(distance, 1)
        return distance

def calculate_all_distances(tg_id):
    current_village = profiledao.get_cur_village_id(tg_id)
    current_village_x = get_village_x_coordinates(current_village)
    current_village_y = get_village_y_coordinates(current_village)
    max_y = current_village_y + 10
    max_x = current_village_x + 10
    low_y = current_village_y - 10
    low_x = current_village_x - 10
    maps = session.query(Village).order_by(Village.village_name.asc()).filter(Village.x_coord >= low_x).filter(Village.x_coord <= max_x).filter(Village.y_coord >= low_y).filter(Village.y_coord <= max_y).all()
    maps_sorted = sorted(maps, key=lambda m: mapgendao.calculate_village_distance(tg_id, m.pk))
    return maps_sorted