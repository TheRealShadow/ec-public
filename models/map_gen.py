import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, Float, DECIMAL
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Map_Gen(BaseModel, Base):
    center_x = Column(Integer())
    center_y = Column(Integer())
    radius = Column(Integer())
    radius_filling = Column(Float(12, 10))
    base_slots = Column(Integer())
    attempts = Column(Integer())