from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hr.spiders.hr_spider import HrSpiderSpider
from hr.db import HrInfo

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl("hr_spider")
    number = str(input("请输入1或2选择功能：\n1.数据爬取:\n2.数据查询:\n"))
    if number == '1':
        hr = HrInfo("hrinfo3")
        hr.create_table()
        process.start()
    elif number == '2':
        begin = int(input("请输入开始ID："))
        total = int(input("查询多少个元素："))
        keyword = str(input("请输入关键字："))
        city = str(input("请输入城市："))
        jobtype = str(input("请输入工作类型："))
        hr = HrInfo("hrinfo3")
        items = hr.outinfo(begin,total,keyword,city,jobtype)
   
        for item in items:
            print('title:  '+item['title']+ "\n")
            print('content:  '+item['content']+ "\n")
            print('jobtime:  '+item['jobtime']+ "\n")
            print('city:  '+item['city']+ "\n")
            print('num:  '+item['num']+ "\n")
            print('jobtype:  '+item['jobtype']+ "\n")
            print("--------------next------------------------")
           # print("title: %s\n,detail_url: %s\n,content: %s\n,date: %s\n,location: %s\n,num: %s\n,jobType: %s\n")%(item["title"],item["detail_url"],item["content"],item["date"],item["location"],item["num"],item["jobType"])
    else:
        print("error")


