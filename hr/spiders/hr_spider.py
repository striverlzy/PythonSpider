# -*- coding: utf-8 -*-
import scrapy
from hr.items import HrItem
from hr.db import HrInfo


class HrSpiderSpider(scrapy.Spider):
    name = 'hr_spider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0#a']
    hr = HrInfo("hrinfo3")

    def parse(self, response):
            tr1 = response.css("tr[class='even']")
            tr2 = response.css("tr[class='odd']")
            trs = tr1 + tr2
            for tr in trs:
                item = HrItem()
                name = tr.css("td a::text").extract()[0]
                detailLink = tr.css("td a::attr(href)").extract()[0]

                jobtype=tr.css("td::text").extract()[0]
                num = tr.css("td::text").extract()[1]
                city = tr.css("td::text").extract()[2]
                jobtime=tr.css("td::text").extract()[3]
                item["name"] = name
                item["city"] = city
                item["num"] = num
                item["jobtype"]=jobtype
                item["jobtime"]=jobtime
                item["detailLink"] = "https://hr.tencent.com/"+detailLink
                request = scrapy.Request(url=item["detailLink"],callback=self.parse_body)
                request.meta["item"] = item
                yield request
            next_page = response.xpath("//a[@id='next']/@href").extract()[0]
            if next_page:
                yield scrapy.Request(url="https://hr.tencent.com/"+next_page,callback=self.parse)

    def parse_body(self,response):
        item = response.meta["item"]
        jobduty = response.xpath("//tr[@class='c'][1]/td/ul/li/text()").extract()
        jobduty = "\n".join(jobduty)
        workrequire = response.xpath("//tr[@class='c'][2]/td/ul/li/text()").extract()
        workrequire = "\n".join(workrequire)
        item["content"] = "工作职责：\n"+jobduty+"\n工作要求：\n"+workrequire
        yield item


