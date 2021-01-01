import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Protips(BaseModel, Base):
    tip = Column(String(10000))