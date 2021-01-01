from sqlalchemy import Column, text, BigInteger, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import functions as func
from service import ConfigService as conf

db_connection_string = conf.get_string('DBConf', 'db_connection_string')
engine = create_engine(db_connection_string, encoding='utf8')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    pk = Column(BigInteger, primary_key=True)
    create_date = Column(DateTime, server_default=func.now())
    update_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))