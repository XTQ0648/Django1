import scrapy


class HeSpider(scrapy.Spider):
    name = 'he'
    allowed_domains = ['fanyi.youdao.com']
    start_urls = ['http://fanyi.youdao.com/']

    def parse(self, response):
        print("------")
        print("------")
        print("------")
        print("------")
