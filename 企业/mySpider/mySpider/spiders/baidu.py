import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名字，用于运行爬虫使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址，第一次要访问的域名
    # start_urls是在allowed_domains的前面,添加一个http:// 在allowed_domains的后边添加一个/
    start_urls = ['http://www.baidu.com/']

    # 这是执行起始start_urls后执行的方法,方法中的response就是返回的那个对象
    # 相当于,response = urllib.request.urlopen()
    # 还相当于response = requests.get(),也就是不需要再执行这个了
    def parse(self, response):
        print('阿里')
