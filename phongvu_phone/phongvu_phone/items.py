# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class PhongvuPhoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    producer = scrapy.Field()
    price = scrapy.Field()
    price_sale = scrapy.Field()
    image = scrapy.Field()
    insurance = scrapy.Field()
    category = scrapy.Field()
    short_name = scrapy.Field()
    color = scrapy.Field()
    screen = scrapy.Field()
    pixels = scrapy.Field()
    ROM = scrapy.Field()
    OS = scrapy.Field()
    RAM = scrapy.Field()
