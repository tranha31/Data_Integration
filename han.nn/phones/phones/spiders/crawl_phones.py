import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from phones.items import PhoneItem
from collections import defaultdict
from pymongo import MongoClient

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["cellphones.com.vn"]
    start_urls = [
        "https://cellphones.com.vn/iphone-11.html",
        "https://cellphones.com.vn/iphone-13-pro-max.html",
        "https://cellphones.com.vn/oneplus-nord-n10-5g.html",
        "https://cellphones.com.vn/iphone-12-pro-max.html",
        "https://cellphones.com.vn/samsung-galaxy-s22-ultra-12gb-256gb.html",
        "https://cellphones.com.vn/nokia-105-single-sim-2019.html",
        "https://cellphones.com.vn/xiaomi-redmi-9c-64gb.html",
        "https://cellphones.com.vn/samsung-galaxy-a52s.html",
        "https://cellphones.com.vn/samsung-galaxy-a22.html",
        "https://cellphones.com.vn/iphone-12-128gb.html",
        "https://cellphones.com.vn/iphone-13-mini.html",
        "https://cellphones.com.vn/iphone-8-plus-128gb-chinh-hang-vn-a.html",
    ]


    def __init__(self):
        client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00.mt1kt.mongodb.net:27017,cluster0-shard-00-01.mt1kt.mongodb.net:27017,cluster0-shard-00-02.mt1kt.mongodb.net:27017/?ssl=true&replicaSet=atlas-cl2qgx-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('phones_db')
        self.records = db.phone_items
        dict = self.records.find({})
        # dict =[]
        self.site_map = defaultdict(lambda: False)
        for item in dict:
            self.site_map[str(item['url'].decode('utf-8'))]=True


    def parse(self, response):
        # print(response.xpath('//a[contains(@class, "active")]'))
        # print(Selector(response).xpath("/html/body/div[1]/div/section/div[3]/div[2]/div[2]/div[2]/div").extract())
        item_urls = response.xpath("/html/body/div[1]/div/section/form[1]/div/div[2]/div[2]/div[2]/div/a/@href")
        if item_urls:
            for item_url in item_urls.extract():
                if not self.site_map[item_url]:
                    self.site_map[item_url]=True
                    yield scrapy.Request(response.urljoin(item_url), callback=self.parse_item, meta={'url': item_url})
                 
        next_items = response.xpath("//div[@class='block-products compare-product related-product san-pham-tuong-tu']/div[2]/div/div/div[1]/a/@href")

        if next_items:
            next_urls = next_items.extract()
            for url in next_urls:
                yield scrapy.Request(response.urljoin(url), callback=self.parse)

    def new_item(self, response, phone=None):
        item = PhoneItem()

        item['url']=response.meta.get('url').encode('utf-8')
        name=Selector(response).xpath('//div[@class="box-name__box-product-name"]/h1/text()').extract_first()
        if name:
            item['name']=name.strip(' \t\n\r')
        # ram = scrapy.Field()
        # memory = scrapy.Field()
        # chip = scrapy.Field()
        # screen = scrapy.Field()
        # pin = scrapy.Field()
        # front_camera = scrapy.Field()
        # behind_camera = scrapy.Field()
        # sim = scrapy.Field()
        # operating_system = scrapy.Field()

        tskt = response.xpath('//table[@id="tskt"]/tbody/tr/th/text()').extract()
        for i in range(len(tskt)):
            if 'Kích thước màn hình' in tskt[i]:
                item['screen']=tskt[i+1]+', '+tskt[i+3]
        for i in range(len(tskt)):
            if 'Camera sau' in tskt[i]:
                item['behind_camera']=tskt[i+1]+tskt[i+2]+tskt[i+3]
        for i in range(len(tskt)):
            if 'Camera trước' in tskt[i]:
                item['front_camera']=tskt[i+1]
        for i in range(len(tskt)):
            if 'Chipset' in tskt[i]:
                item['chip']=tskt[i+1]
        for i in range(len(tskt)):
            if 'RAM' in tskt[i]:
                item['ram']=tskt[i+1]
        for i in range(len(tskt)):
            if 'Bộ nhớ trong' in tskt[i]:
                item['memory']=tskt[i+1]
        for i in range(len(tskt)):
            if 'Pin' in tskt[i]:
                item['pin']=tskt[i+1]
        for i in range(len(tskt)):
            if 'Thẻ SIM' in tskt[i]:        
                item['sim']=tskt[i+1]
        for i in range(len(tskt)):
            if 'Hệ điều hành' in tskt[i]:
                item['operating_system']=tskt[i+1]
        if phone is not None:
            print("COLOR")
            color = phone.xpath("a/p/strong/text()").extract_first()
            if color:
                item['color']=color.strip()

            price=phone.xpath("a/p/span/text()").extract_first()
            if price:
                item['price']=price.strip(' \t\n\r')[:-2]

            image_url=phone.xpath("a/img/@data-src").extract_first()
            if image_url:
                item['image_url']=image_url.encode('utf-8')
        else:
            print('NOT COLOR')
            item['color']=''
            price=response.xpath('//a[contains(@class, "active")]/span/text()').extract_first()
            if price:
                item['price']=price.strip(' \t\n\r')[:-2]

            image_url=response.css("div.swiper-slide").xpath("img/@data-src").extract_first()
            # print(image_url)
            if image_url:
                item['image_url']=image_url.encode('utf-8')

        return item


    
    def parse_item(self, response):
        color = False
        for phone in response.xpath("//ul[@class='list-colors']/li"):
            color = True
            item = self.new_item(response, phone=phone)
            self.records.insert_one(dict(item))
        if not color:
            item = self.new_item(response)
            # print(item)
            self.records.insert_one(dict(item))
            


