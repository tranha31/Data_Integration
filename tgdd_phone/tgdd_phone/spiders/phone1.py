from pymysql import NULL
import scrapy
import math 
from tgdd_phone.items import TgddPhoneItem
from scrapy_splash import SplashRequest

class Phone1Spider(scrapy.Spider):
    name = 'phone1'
    allowed_domains = ['www.thegioididong.com/dtdd']
    start_urls = ['http://www.thegioididong.com/dtdd#c=42&o=9&pi=5/']

    render_script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(5))

            return {
                html = splash:html(),
                url = splash:url(),
            }
        ends
        """ 

    # Do trang tgdđ nó load bằng javascript. Nên cần delay 1 chút
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse, 
                endpoint='render.html',
                args={
                    'wait': 20,
                    'lua_source': self.render_script,
                }
            )

    def parse(self, response):
        phoneItem = response.css('#categoryPage > div.container-productbox > ul > li > a.main-contain ::attr(href)').extract()
        for phone in phoneItem:
            yield scrapy.Request(response.urljoin(phone), callback=self.parse_info_phone, dont_filter=True)

    # Bat dau boc tach du lieu nhoe!
    def parse_info_phone(self, response):
        phone = TgddPhoneItem()
        phone['company'] = response.css('body > section.detail > ul > li:nth-child(2) > a ::text').extract_first()
        phone['company'] = phone['company'][11:len(phone['company'])]
        phone['color'] = response.css('body > section.detail > div.box_main > div.box_right > div > div.color > a.box03__item ::text').extract()
        phone['name'] = response.css('body > section.detail > h1 ::text').extract_first()
        phone['name'] = phone['name'][11:len(phone['name'])]
        phone['memory'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(7) > div > span ::text').extract_first()
        
        originPrice = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.price-one > div > p.box-price-old').extract()
        if len(originPrice) > 0:
            phone['originPrice'] = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.price-one > div > p.box-price-old ::text').extract_first()
            phone['discountRate'] = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.price-one > div > p.box-price-percent ::text').extract_first()
            phone['discountPrice'] = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.price-one > div > p.box-price-present ::text').extract_first()
        else:
            phone['originPrice'] = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal >div.price-one > div > p.box-price-present ::text').extract_first()
            if phone['originPrice'] == None:
                phone['originPrice'] = response.css('body > section.detail > div.box_main > div.box_right > div.box04.notselling > div.price-one > div > p ::text').extract_first()
            phone['discountRate'] = None
            phone['discountPrice'] = None
            
        
        screenInfo = ''
        for info in response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(1) > div > span ::text').extract():
            screenInfo = screenInfo + info + ', '
        screenInfo = screenInfo[0:len(screenInfo)-2]
        
        phone['screen'] = screenInfo.replace('"','')
        phone['operatingSystem'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(2) > div > span ::text').extract_first()
        phone['frontCamera'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(4) > div > span ::text').extract_first()
        phone['behindCamera'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(3) > div > span ::text').extract_first()
        phone['chip'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(5) > div > span ::text').extract_first()
        phone['ram'] = response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(6) > div > span ::text').extract_first()

        simInfo = ''
        for info in response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(8) > div > span ::text').extract():
            simInfo = simInfo + info + ', '
        simInfo = simInfo[0:len(simInfo)-2]
        phone['sim'] = simInfo

        pinInfo = ''
        for info in response.css('body > section.detail > div.box_main > div.box_right > div.parameter > ul > li:nth-child(9) > div > span ::text').extract():
            pinInfo = pinInfo + info + ', '
        pinInfo = pinInfo[0:len(pinInfo)-2]
        phone['pin'] = pinInfo

        divImage = response.xpath("//div[@data-gallery-id='color-images-gallery']/div/img/@src").extract()
        
        phone['imageUrl'] = divImage
        yield phone