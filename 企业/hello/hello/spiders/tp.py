import scrapy


class TpSpider(scrapy.Spider):

    name = 'tp'
    allowed_domains = ['pixabay.com']
    start_urls = ['http://pixabay.com/']

    def parse(self, response):
        print("-------------")
        print("-------------")
        print("-------------")
        print("-------------")
