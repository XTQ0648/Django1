import scrapy


# scrapy startproject VIEW创建项目
# 进入spiders目录
# scrapy genspider tp https://pixabay.com/zh/images/search/?order=ec 创建爬虫文件
# scrapy crawl tp 运行

class TpSpider(scrapy.Spider):

    name = 'tp'
    allowed_domains = ['https://pixabay.com']
    start_urls = ['https://pixabay.com/zh/images/search/?order=ec']

    def parse(self, response):
        print("--------------------------")
        print("--------------------------")
        list_a = response.xpath('//div[@id="content"]/div/div/div/div/div/div/div/div')

        for li in list_a:
            src = li.xpath("https://pixabay.com" + '/a/@href').extract_first()  # 图片
            name = li.xpath('/a/img/@alt').extract_first()[0]  # 名字
            # pipelines 下载数据
            print(src)
