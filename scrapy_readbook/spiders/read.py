# 1.创建项目 scrapy startproject 项目名称
# 2.跳转到spiders文件夹的目录下
#     cd 项目名字/项目名字/spiders
# 3.创建爬虫文件
#     scrapy genspider -t crawl 爬虫文件名字  爬取的域名
import urllib
import random
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_readbook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    def __init__(self, *args, **kwargs):
        super(ReadSpider, self).__init__(*args, **kwargs)
        if not os.path.exists('image'):
            os.makedirs('image')
    name = "read"
    allowed_domains = ["yuedu.163.com"]
    # cate_arr = [2000, 2300, 2800, 2500, 2600, 2400, 2100, 2200, 2900, 2700, 3000, 3100]
    def start_requests(self):
    # 这个只能爬取一个详细分类的图书，如果要爬多个分类，需要修改start_url和allow的路径，和详细类别的参数
        base_url = 'https://yuedu.163.com/book/category/category/{}/0_0_1/p{}/s20'
        cate_arr = [2000, 2300, 2800, 2500, 2600, 2400, 2100, 2200, 2900, 2700, 3000, 3100, ]
        pages = range(0, 34)  # 你要爬取的不同页数范围
        for cate in cate_arr:
            for page in pages:
                url = base_url.format(cate, page)
                yield scrapy.Request(url=url, callback=self.parse)

    # 这里是网页中，分页的href的规律
    # /book/category/category/2000/2004/0_0_1/p2+/s20
    # /book/category/category/2000/2004/0_0_1/p3+/s20
    #allow=r'/book/category/category/2000/0_0_1/p\d+/s20'


    # rules = (Rule(LinkExtractor(allow=r'/book/category/category/2000/0_0_1/p\d+/s20'),
    #               callback="parse",
    #               follow=True),)

    # def start_requests(self):
    #     headers = {
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    #         'Cookie':'YUEDUDYAMIC=73b63802c56bb10183fabdbf5f94b10d5c3f562e; YUEDU_V_DID=1690109116802471; NTESYUEDUSI=B0B8476BA2F373C227A4420F29EF789E.hzabj-yaolu54.server.163.org-8010'
    #     }
    #
    #     yield scrapy.Request(url=self.start_urls[0],  callback=self.parse)

    def parse(self, response):
        # 获取图书列表
        book_list = response.xpath('//div[contains(@class,"yd-book-item-pull-left")]/a/@href').getall()
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Cookie':'YUEDUDYAMIC=73b63802c56bb10183fabdbf5f94b10d5c3f562e; YUEDU_V_DID=1690109116802471; NTESYUEDUSI=B0B8476BA2F373C227A4420F29EF789E.hzabj-yaolu54.server.163.org-8010'
        }
        for book in book_list:
            book_url = "https://yuedu.163.com" + book;
            #循环进入图书详情页
            yield scrapy.Request(url=book_url,headers = headers, callback=self.parse_book)

    def parse_book(self, response):
        # 书名
        book_title = response.xpath('//div[@class="f-fl"]/h3/em/text()').get()
        # 作者
        book_author = response.xpath('//div[@class="f-fl"]/h3/span/a/text()').get()
        # 内容简介
        book_content_nodes = response.xpath('//div[contains(@class,"description")]/text()').extract()
        book_content = ''.join(book_content_nodes).strip()
        # 图书标签
        book_tags = response.xpath('//div[@class="m-tags"]/a/text()').get()

        # 图片
        book_src = response.xpath('//div[@class="m-bookdetail"]/a[@class="cover"]/img/@src').get()
        parts = book_src.split('/')
        # 获取最后一个部分，即斜杠后的内容,作为图片的名字以及地址
        last_part = parts[-1]
        #下载图片
        urllib.request.urlretrieve(url=book_src, filename='./image/' + last_part + '.jpg')

        # 类别
        book_category = response.xpath('//div[@class="m-breadcrumbs"]/a/text()')[1].get()

        # 详细类别
        book_detailedCategory = response.xpath('//div[@class="m-breadcrumbs"]/a/text()')[2].get()

        #库存，初始化为5
        book_store = 5

        book = ScrapyReadbookItem(book_title=book_title, book_author=book_author,book_tags=book_tags,
                                  book_content=book_content, book_src=last_part+".jpg",book_category=book_category,
                                  book_detailedCategory=book_detailedCategory,book_store = book_store)
        yield book
