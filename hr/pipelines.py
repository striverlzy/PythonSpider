# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from hr.db import HrInfo
import json
class HrPipeline(object):
    def __init__(self):
        #self.file = open("hr.json","w",encoding="utf-8")
        pass
    def process_item(self, item, spider):
        if item["name"]:
             #line = json.dumps(dict(item))+"\n"
            #self.file.write(line.encode("utf-8").decode("unicode_escape"))
            hr = HrInfo("hrinfo3")
            hr.add_hr(item["name"],item["detailLink"],item["content"],item["city"],item["num"],item["jobtype"],item["jobtime"])
            return item
        else:
            raise DropItem("没有标题 %s"%item)
