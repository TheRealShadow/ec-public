import enum
from math import sqrt, pow

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL, Float
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Village(BaseModel, Base):
    village_name = Column(String(455))
    # Defines where to get the owner ID
    owner_pk = Column('owner_pk', BigInteger, ForeignKey('player.pk'))
    # Creates the relation from the player database with the village database to set the owner ID == unique player ID for later management and features
    owner = relationship('Player', uselist=False, backref="village")
    x_coord = Column(Integer())
    y_coord = Column(Integer())
    wood_stock = Column(Float(12, 10))
    stone_stock = Column(Float(12, 10))
    iron_stock = Column(Float(12, 10))
    loyalty = Column(Float(12, 10))
    # cheat sheet:  # guild_leader = Column(Boolean, nullable=False, server_default='0')  # teacher = Column(Boolean, nullable=False, server_default='0')  # character_pk = Column('character_pk', BigInteger, ForeignKey('character.pk'))  # character = relationship('Character', uselist=False, backref="user")  # completed_lesson_pk = Column('completed_lesson_pk', BigInteger, ForeignKey('lesson.pk'))  # completed_lesson = relationship('Lesson', uselist=False, backref="user")  # squad_pk = Column('squad_pk', BigInteger, ForeignKey('squad.pk'))  # squad = relationship('Squad', uselist=False, backref="user",  #                      primaryjoin=  #                      squad_pk == Squad.pk)  # squad_request_forbidden_till = Column(DateTime)  # notes = Column(Text)  # ban_reason = Column(Text)  # statistics = Column(Text)  # market_wts_forbidden_till = Column(DateTime)  # market_wtb_forbidden_till = Column(DateTime)  # market_mod = Column(Boolean, nullable=False, server_default='0')
