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
    ]


    def __init__(self):
        client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00.mt1kt.mongodb.net:27017,cluster0-shard-00-01.mt1kt.mongodb.net:27017,cluster0-shard-00-02.mt1kt.mongodb.net:27017/?ssl=true&replicaSet=atlas-cl2qgx-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('phones_db')
        self.records = db.phone_items
        dict = self.records.find({})
        self.site_map = defaultdict(lambda: False)
        for item in dict:
            self.site_map[str(item['url'].decode('utf-8'))]=True


    def parse(self, response):
        # print(Selector(response).xpath("/html/body/div[1]/div/section/div[3]/div[2]/div[2]/div[2]/div").extract())
        item_urls = response.xpath("/html/body/div[1]/div/section/form[1]/div/div[2]/div[2]/div[2]/div/a/@href")
        if item_urls:
            for item_url in item_urls.extract():
                # print(item_url)
                # print("--------")
                if not self.site_map[item_url]:
                    self.site_map[item_url]=True
                    yield scrapy.Request(response.urljoin(item_url), callback=self.parse_item, meta={'url': item_url})
                 
        next_items = response.xpath("//div[@class='block-products compare-product related-product san-pham-tuong-tu']/div[2]/div/div/div[1]/a/@href")

        if next_items:
            next_urls = next_items.extract()
            for url in next_urls:
                # print(url)
                # print("***********")
                yield scrapy.Request(response.urljoin(url), callback=self.parse)

    
    def parse_item(self, response):
        # print(response.xpath("//ul[@class='list-colors']/li"))
        # print("@@@@@@@@@@@@@@@@@")
        for phone in response.xpath("//ul[@class='list-colors']/li"):
            item = PhoneItem()

            item['url']=response.meta.get('url').encode('utf-8')
            name=Selector(response).xpath('//div[@class="box-name__box-product-name"]/h1/text()').extract_first()
            if name:
                item['name']=name.strip(' \t\n\r')

            price=phone.xpath("a/p/span/text()").extract_first()
            if price:
                item['price']=price.strip(' \t\n\r')[:-2]

            color = phone.xpath("a/p/strong/text()").extract_first()
            if color:
                item['color']=color.strip()

            image_url=phone.xpath("a/img/@data-src").extract_first()
            if image_url:
                item['image_url']=image_url.encode('utf-8')
                # print(item['image_url'])
            # print(item, self.records)
            # print(type(item))
            self.records.insert_one(dict(item))
            # yield item


