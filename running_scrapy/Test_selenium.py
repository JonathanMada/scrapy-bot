from Milestone.running_scrapy.DownloadMovie import DownloadM
from sqlalchemy.orm import sessionmaker
from Milestone.models import MovieDB, db_connect
import re

# mymovies = ['Onward', 'The Wolf of Wall Street']
#
# for movie in mymovies:
#     test = DownloadM(movie)
#     test.driverstart

engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()
# my_title = session.query(MovieDB.title).all()
# my_detail = session.query(MovieDB.details).all()
movies = session.query(MovieDB).all()
for movie in movies:
    movieObject = {'title': movie.title,
                   'ratings': movie.ratings
                   }
    if movieObject['ratings'] >= 8.0:

        print(movieObject['title'], ' - ', movieObject['ratings'])


# my_movie = [i[0] for i in movies]
# my_rating = [i[0] for i in ratings]
# titles = [i[0] for i in my_title]
# for i in titles:
#     if i == 'Joker':
#         yts_download = DownloadM(i)
#         yts_download.driverstart()
