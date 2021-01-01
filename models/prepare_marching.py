import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, Float, DECIMAL
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Prepare_marching(BaseModel, Base):
    sending_village = Column(Integer())
    unit = Column(Integer())
    amount = Column(Integer())