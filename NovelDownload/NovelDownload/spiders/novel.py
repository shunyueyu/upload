import scrapy
from ..items import NoveldownloadItem

class NovelSpider(scrapy.Spider):
    name = "novel"
    # allowed_domains = ["wap.bqbwx.cc"]
    # start_urls = ["https://wap.bqbwx.cc/53/53190/488294265.html"]
    allowed_domains = ["www.26ks.cc"]
    start_urls = ["http://www.26ks.cc/book/24023/"]


    def parse(self, response):
        chapters = response.xpath('//*[@id="list"]/dl/dd/a/@href').getall()
        #print("http://www.26ks.cc" +chapters[192])
        start_index = 192
        end_index = 200
        for item_index,chapter_url in enumerate(chapters[start_index:end_index]):
            yield response.follow("http://www.26ks.cc" + chapter_url, self.parse_chapter,meta={'item_index': item_index})
            #request = scrapy.Request("http://www.26ks.cc" + chapter_url, callback=self.parse_detail,meta={'index': index})

    def parse_chapter(self, response):
        novel_item = NoveldownloadItem()
        novel_item['title'] = response.xpath('/html/head/title/text()').get().replace('超神宠兽店_',"").replace('_玄幻小说_爱豆看书网',"").replace(' ','').replace("\r\n",'')
        novel_item['content'] = response.xpath('//*[@id="content"]/p/text()').getall()
        novel_item['detail'] = " ".join(novel_item['content'][1:]).replace(' ','').replace("\r",'')
        novel_item['item_index'] = response.meta.get('item_index')

        yield {
               "title":novel_item['title'],
               "detail":novel_item['detail'],
               "item_index":novel_item['item_index']
               }
