# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyReadbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_tags = scrapy.Field()
    book_content = scrapy.Field()
    book_src = scrapy.Field()
    book_category = scrapy.Field()
    book_detailedCategory = scrapy.Field()
    book_store = scrapy.Field()
    pass
