import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Unit(BaseModel, Base):
    unit_name = Column(String(455))
    wood_cost = Column(Integer())
    stone_cost = Column(Integer())
    iron_cost = Column(Integer())
    population_cost = Column(Integer())
    speed = Column(Integer())
    attack = Column(Integer())
    defence = Column(Integer())
    defence_cav = Column(Integer())
    defence_arc = Column(Integer())
    loot_carry = Column(Integer())
    recruit_time = Column(Integer())
