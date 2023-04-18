import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://cn.58.com/job/?key=%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8']
    start_urls = ['https://cn.58.com/job/?key=%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8']

    def parse(self, response):
        """
        content = response.text  # 返回字符串
        content = response.body # 返回二进制数据
        """
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print(span.extract())
