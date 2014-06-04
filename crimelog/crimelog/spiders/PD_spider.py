from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story

import sys
sys.dont_write_bytecode = True


class PD(Spider):
    name = "pd"
    allowed_domains = ["stltoday.com"]
    start_urls = ["http://www.stltoday.com/news/local/crime-and-courts/"]
    
    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//ul[@class="bull-list"]/li').extract()
 
        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//ul[@class="bull-list"]/li/a/text()').extract()[story]
            item['url'] = "http://www.stltoday.com" + sel.xpath('//ul[@class="bull-list"]/li/a//@href').extract()[story]
            item.save()