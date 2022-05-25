import scrapy


class PvPhoneSpider(scrapy.Spider):
    name = 'pv_phone'
    allowed_domains = ['phongvu.vn']
    start_urls = ['https://phongvu.vn/search?router=productListing&query=%C4%91i%E1%BB%87n+tho%E1%BA%A1i']

    def parse(self, response):
        pass
