# -*- coding: utf-8 -*-

import json


class blogPipeline(object):
    def open_spider(self, spider):
        self.file = open('blogs.json', 'w', encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)+'\n'
        self.file.writelines(line)
        return item
