# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoveldownloadItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    detail = scrapy.Field()
    item_index = scrapy.Field()

