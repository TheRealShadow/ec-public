import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Player(BaseModel, Base):
    username = Column(String(455))
    tg_id = Column(String(45), unique=True)
    player_name = Column(String(45), unique=True)
    # Defines where to get the owner ID
    selected_village = Column(Integer())
    selected_march_village = Column(Integer())
    pouches = Column(Integer())
    points = Column(Integer())
    villages = Column(Integer())
    avg_vil_point = Column(Integer())
    ban_status = Column(Integer())
    permission_level = Column(Integer())
    defeated_units_attack = Column(Integer())
    defeated_units_defense = Column(Integer())
    total_defeated_units = Column(Integer())

    # cheat sheet:  # guild_leader = Column(Boolean, nullable=False, server_default='0')  # teacher = Column(Boolean, nullable=False, server_default='0')  # character_pk = Column('character_pk', BigInteger, ForeignKey('character.pk'))  # character = relationship('Character', uselist=False, backref="user")  # completed_lesson_pk = Column('completed_lesson_pk', BigInteger, ForeignKey('lesson.pk'))  # completed_lesson = relationship('Lesson', uselist=False, backref="user")  # squad_pk = Column('squad_pk', BigInteger, ForeignKey('squad.pk'))  # squad = relationship('Squad', uselist=False, backref="user",  #                      primaryjoin=  #                      squad_pk == Squad.pk)  # squad_request_forbidden_till = Column(DateTime)  # notes = Column(Text)  # ban_reason = Column(Text)  # statistics = Column(Text)  # market_wts_forbidden_till = Column(DateTime)  # market_wtb_forbidden_till = Column(DateTime)  # market_mod = Column(Boolean, nullable=False, server_default='0')
