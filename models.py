from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Float, Text)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class MovieDB(DeclarativeBase):
    __tablename__ = "imdb_scraped"

    rank = Column('Rank', Integer, primary_key=True)
    title = Column('Title', String(100))
    release = Column('Release', Integer)
    ratings = Column('Ratings', Float)
    reviews = Column('Reviews', String(100))
    details = Column('Details', Text())