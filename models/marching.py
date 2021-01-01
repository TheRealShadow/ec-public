import enum

from sqlalchemy import Column, String, BigInteger, ForeignKey, Enum, Boolean, DateTime, Text, Integer, DECIMAL, Float
from sqlalchemy.orm import relationship

from models.basemodel import BaseModel, Base


class Marching(BaseModel, Base):
    owner_pk = Column('owner_pk', BigInteger, ForeignKey('player.pk'))
    owner = relationship('Player', uselist=False, backref="marching")
    from_village_id = Column(Integer())
    target_owner = Column(Integer())
    to_village_id = Column(Integer())
    arrival_time = Column(DateTime())
    slowest_unit_time = Column(Integer())
    type_march = Column(String(20))
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
    looted_wood = Column(Integer())
    looted_stone = Column(Integer())
    looted_iron = Column(Integer())

    # cheat sheet:  # guild_leader = Column(Boolean, nullable=False, server_default='0')  # teacher = Column(Boolean, nullable=False, server_default='0')  # character_pk = Column('character_pk', BigInteger, ForeignKey('character.pk'))  # character = relationship('Character', uselist=False, backref="user")  # completed_lesson_pk = Column('completed_lesson_pk', BigInteger, ForeignKey('lesson.pk'))  # completed_lesson = relationship('Lesson', uselist=False, backref="user")  # squad_pk = Column('squad_pk', BigInteger, ForeignKey('squad.pk'))  # squad = relationship('Squad', uselist=False, backref="user",  #                      primaryjoin=  #                      squad_pk == Squad.pk)  # squad_request_forbidden_till = Column(DateTime)  # notes = Column(Text)  # ban_reason = Column(Text)  # statistics = Column(Text)  # market_wts_forbidden_till = Column(DateTime)  # market_wtb_forbidden_till = Column(DateTime)  # market_mod = Column(Boolean, nullable=False, server_default='0')
