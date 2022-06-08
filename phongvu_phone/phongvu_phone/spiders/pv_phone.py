import re
import scrapy
from phongvu_phone.items import PhongvuPhoneItem


class PvPhoneSpider(scrapy.Spider):
    name = 'pv_phone'
    allowed_domains = ['phongvu.vn']
    start_urls = [
        'https://phongvu.vn/search?router=productListing&query=%C4%91i%E1%BB%87n+tho%E1%BA%A1i+di+%C4%91%E1%BB%99ng&masterCategoryIds=2388',
        'https://phongvu.vn/search?router=productListing&query=%C4%91i%E1%BB%87n+tho%E1%BA%A1i+di+%C4%91%E1%BB%99ng&masterCategoryIds=2388&page=2'
    ]

    def parse(self, response):
        for item_url in response.css("div.css-13w7uog > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_phone)

        next_page = response.css(
            "div.css-1jfq9xh > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_phone(self, response):
        item = PhongvuPhoneItem()
        item['name'] = response.css(
            'div.css-6b3ezu > div > h1.css-4kh4rf ::text').extract()[-1]

        all_prices = response.css(
            'div.css-12htb1n > div ::text').extract()
        item['price'] = all_prices[0]
        if len(all_prices) > 1:
            item['price_sale'] = all_prices[-1]
        else:
            item['price_sale'] = None

        item['image'] = response.css(
            'div.css-1idxzwd > picture > source ::attr(srcset)').extract_first()

        details = response.css(
            'div.css-1i3ajxp > div ::text').extract()
        item['producer'] = details[1]
        item['insurance'] = details[3]
        item['category'] = details[5]
        item['short_name'] = details[7]
        item['color'] = details[9]
        item['screen'] = details[11]
        item['pixels'] = details[13]
        item['ROM'] = details[15]
        item['OS'] = details[17]
        item['RAM'] = details[19]

        yield item
