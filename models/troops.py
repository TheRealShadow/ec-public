import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Troops(BaseModel, Base):
    # Defines where to get the owner ID
    village_pk = Column('village_pk', BigInteger, ForeignKey('village.pk'))
    # Creates the relation from the player database with the village database to set the owner ID == unique player ID for later management and features
    village_id = relationship('Village', uselist=False, backref="troops")
    spear_man = Column(Integer())
    sword_man = Column(Integer())
    brute = Column(Integer())
    archer = Column(Integer())
    scout = Column(Integer())
    light_cav = Column(Integer())
    heavy_cav = Column(Integer())
    mounted_arch = Column(Integer())
    ram = Column(Integer())
    catapult = Column(Integer())
    noble = Column(Integer())