import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Structure(BaseModel, Base):
    structure_name = Column(String(455))
    structure_base_points = Column(Integer())
    structure_points_factor = Column(DECIMAL(5, 3))
    structure_min_level = Column(Integer())
    structure_max_level = Column(Integer())
    structure_base_wood_cost = Column(Integer())
    structure_base_stone_cost = Column(Integer())
    structure_base_iron_cost = Column(Integer())
    structure_base_population_cost = Column(Integer())
    structure_wood_factor = Column(DECIMAL(5, 3))
    structure_stone_factor = Column(DECIMAL(5, 3))
    structure_iron_factor = Column(DECIMAL(5, 3))
    structure_population_factor = Column(DECIMAL(5, 3))
    structure_base_building_time = Column(Integer())
    structure_building_time_factor = Column(DECIMAL(5, 1))
