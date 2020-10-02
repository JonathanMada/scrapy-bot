# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from Milestone.models import MovieDB, db_connect, create_table
from scrapy.exceptions import DropItem
import logging


class MilestonePipeline:

    def __init__(self):
        """
        Initializes database connection and session maker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        moviedb = MovieDB()
        # Since Item in items.py is treated as a dictionary, we can fetch our data by calling its elements
        moviedb.rank = item["Rank"]
        moviedb.title = item["Title"]
        moviedb.release = item["Release"]
        moviedb.ratings = item["Ratings"]
        moviedb.reviews = item["Reviews"]
        moviedb.details = item["Details"]

        try:
            session.add(moviedb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

            return item


# We have to verify
class DuplicatesPipeline:

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****DuplicatesPipeline: database connected****")

    def process_item(self, item, spider):
        session = self.Session()
        exist_movie = session.query(MovieDB).filter_by(title=item["Title"]).first()
        if exist_movie is not None:  # the movie quote exists
            raise DropItem(f'Duplicate item found: {item["Title"]}')
            session.close()
        else:
            return item
            session.close()
