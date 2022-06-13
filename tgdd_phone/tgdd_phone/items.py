# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TgddPhoneItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    name = scrapy.Field()
    memory = scrapy.Field()
    color = scrapy.Field()
    originPrice = scrapy.Field()
    discountPrice = scrapy.Field()
    discountRate = scrapy.Field()
    screen = scrapy.Field()
    operatingSystem = scrapy.Field()
    frontCamera = scrapy.Field()
    behindCamera = scrapy.Field()
    chip = scrapy.Field()
    ram = scrapy.Field()
    sim = scrapy.Field()
    pin = scrapy.Field()
    imageUrl = scrapy.Field()
    pass
