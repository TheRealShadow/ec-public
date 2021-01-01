import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Structure_Resource_Production(BaseModel, Base):
    name = Column(String(455))
    base_production_production = Column(Integer())
    base_population_production = Column(Integer())
    base_capacity = Column(Integer())
    production_factor = Column(DECIMAL(12, 10))
    population_factor = Column(DECIMAL(12, 10))
    capacity_factor = Column(DECIMAL(12, 10))
