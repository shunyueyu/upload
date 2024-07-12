# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class NoveldownloadPipeline:
    def __init__(self):
        self.data_list = []
        self.base_path =  "aaa/"
        self.filename_path = self.base_path + "aa.txt"

    def process_item(self, item, spider):
        self.data_list.append(item)
        return item

    def close_spider(self,spider):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        with open(self.filename_path, 'a+', encoding='utf-8') as f:
            for data in sorted(self.data_list, key=lambda x: x['item_index']):
                f.write(data['title'] + "\n")
                f.write(data['detail'] + "\n")

