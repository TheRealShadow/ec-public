import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL, Float
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Support(BaseModel, Base):
    owner = Column(Integer())
    from_village_id = Column(Integer())
    in_village_id = Column(Integer())
    slowest_unit_time = Column(Integer())
    spear_man = Column(Integer())
    sword_man = Column(Integer())
    brute = Column(Integer())
    archer = Column(Integer())
    scout = Column(Integer())
    light_cav = Column(Integer())
    heavy_cav = Column(Integer())
    mounted_arch = Column(Integer())
    ram = Column(Integer())
    catapult = Column(Integer())
    noble = Column(Integer())

    # cheat sheet:  # guild_leader = Column(Boolean, nullable=False, server_default='0')  # teacher = Column(Boolean, nullable=False, server_default='0')  # character_pk = Column('character_pk', BigInteger, ForeignKey('character.pk'))  # character = relationship('Character', uselist=False, backref="user")  # completed_lesson_pk = Column('completed_lesson_pk', BigInteger, ForeignKey('lesson.pk'))  # completed_lesson = relationship('Lesson', uselist=False, backref="user")  # squad_pk = Column('squad_pk', BigInteger, ForeignKey('squad.pk'))  # squad = relationship('Squad', uselist=False, backref="user",  #                      primaryjoin=  #                      squad_pk == Squad.pk)  # squad_request_forbidden_till = Column(DateTime)  # notes = Column(Text)  # ban_reason = Column(Text)  # statistics = Column(Text)  # market_wts_forbidden_till = Column(DateTime)  # market_wtb_forbidden_till = Column(DateTime)  # market_mod = Column(Boolean, nullable=False, server_default='0')
