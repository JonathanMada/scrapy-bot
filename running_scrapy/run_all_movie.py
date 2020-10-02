from Milestone.spiders.scrapy_imdb import MilestoneScrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Milestone.running_scrapy.DownloadMovie import DownloadM
from sqlalchemy.orm import sessionmaker
from Milestone.models import MovieDB, db_connect

# SCRAPY - We start scraping
settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(MilestoneScrapy)
process.start()

# SQLALCHEMY - Scraping is done, we now access the database with SQLalchemy
engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()
movies = session.query(MovieDB).all()
for movie in movies:
    movieObject = {'title': movie.title,
                   'ratings': movie.ratings
                   }
    if movieObject['ratings'] >= 8.0:

        # SELENIUM - now we start downloading and interacting with the browser
        yts_download = DownloadM(movieObject['title'])
        yts_download.driverstart()