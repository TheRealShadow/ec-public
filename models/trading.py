import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL, Float
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Trading(BaseModel, Base):
    owner = Column(Integer())
    from_village_id = Column(Integer())
    to_village_id = Column(Integer())
    arrival_time = Column(DateTime())
    wood = Column(Integer())
    stone = Column(Integer())
    iron = Column(Integer())
    traders = Column(Integer())
    type_trade = Column(String(20))