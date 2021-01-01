import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Building(BaseModel, Base):
    # Defines where to get the owner ID
    village_pk = Column('village_pk', BigInteger, ForeignKey('village.pk'))
    # Creates the relation from the player database with the village database to set the owner ID == unique player ID for later management and features
    village_id = relationship('Village', uselist=False, backref="building")
    headquarter_level = Column(Integer())
    barrack_level = Column(Integer())
    archery_level = Column(Integer())
    stable_level = Column(Integer())
    siege_workshop_level = Column(Integer())
    castle_level = Column(Integer())
    smithy_level = Column(Integer())
    rally_point_level = Column(Integer())
    market_level = Column(Integer())
    woodcutter_level = Column(Integer())
    stone_mine_level = Column(Integer())
    iron_mine_level = Column(Integer())
    farm_level = Column(Integer())
    storage_level = Column(Integer())
    wall_level = Column(Integer())
