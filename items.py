# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MilestoneItem(scrapy.Item):
    # define the fields for your item here like:
    # make always sure that the name of each item corresponds to the ones in spider
    # It acts like a dictionary so call it like a dictionary too
    Rank = scrapy.Field()
    Title = scrapy.Field()
    Release = scrapy.Field()
    Ratings = scrapy.Field()
    Reviews = scrapy.Field()
    Details = scrapy.Field()
