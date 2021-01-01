import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Research(BaseModel, Base):
    # Defines where to get the owner ID
    village_pk = Column('village_pk', BigInteger, ForeignKey('village.pk'))
    # Creates the relation from the player database with the village database to set the owner ID == unique player ID for later management and features
    village_id = relationship('Village', uselist=False, backref="research")
    spear_man = Column(String(3))
    sword_man = Column(String(3))
    brute = Column(String(3))
    archer = Column(String(3))
    scout = Column(String(3))
    light_cav = Column(String(3))
    heavy_cav = Column(String(3))
    mounted_arch = Column(String(3))
    ram = Column(String(3))
    catapult = Column(String(3))
