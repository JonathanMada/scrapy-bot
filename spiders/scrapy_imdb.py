import scrapy
from Milestone.items import MilestoneItem

class MilestoneScrapy(scrapy.Spider):
    name = "Imdb"

    start_urls = {
        "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    }

    def parse(self, response):
        # Here we are assigning the dict under item with another variable
        movie_item = MilestoneItem()
        for movie in response.xpath(".//tr"):
            rank = movie.xpath("./td[@class='titleColumn']/div/text()").get()
            title = movie.xpath("./td[@class='titleColumn']/a/text()").get()
            release = movie.xpath("./td[@class='titleColumn']/span/text()").get()
            rating = movie.xpath("./td[@class='ratingColumn imdbRating']/strong/text()").get()
            reviews = movie.xpath("./td[@class='ratingColumn imdbRating']/strong/@title").get()
            link = response.urljoin(movie.xpath("./td[@class='titleColumn']/a/@href").get())

            yield scrapy.Request(link, callback=self.parse_more, cb_kwargs={'movie_item': movie_item,
                                                                            'rank': rank,
                                                                            'title': title,
                                                                            'release': release,
                                                                            'rating': rating,
                                                                            'reviews': reviews
                                                                            })

    @staticmethod
    def parse_more(response, movie_item, rank, title, release, rating, reviews):
        description = response.css('div.plot_summary')
        # Here we are assigning the scraped objects as values to the dictionary item
        movie_item['Rank'] = int((rank[0:2]).strip())
        movie_item['Title'] = title
        movie_item['Release'] = (int(release.strip('()')) if release is not None else 0)
        movie_item['Ratings'] = (float(rating) if rating is not None else 0)
        movie_item['Reviews'] = (reviews.split(' ')[-3] if reviews is not None else 0)
        movie_item['Details'] = (description.xpath("./div[@class='summary_text']/text()").get()).strip()
        yield movie_item
