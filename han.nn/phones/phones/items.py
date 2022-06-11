# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    image_url = scrapy.Field()

    ram = scrapy.Field()
    memory = scrapy.Field()
    chip = scrapy.Field()
    screen = scrapy.Field()
    pin = scrapy.Field()
    front_camera = scrapy.Field()
    behind_camera = scrapy.Field()
    sim = scrapy.Field()
    operating_system = scrapy.Field()
