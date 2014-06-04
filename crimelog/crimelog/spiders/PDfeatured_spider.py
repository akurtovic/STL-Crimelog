from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story

import sys
sys.dont_write_bytecode = True


class PDfeatured(Spider):
    name = "pd_featured"
    allowed_domains = ["stltoday.com"]
    start_urls = ["http://www.stltoday.com/news/local/crime-and-courts/"]
    
    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//div[@class="index-list-item"]/h1').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//div[@class="index-list-item"]/h1/a/text()').extract()[story]
            item['url'] = "http://www.stltoday.com" + sel.xpath('//div[@class="index-list-item"]/h1/a//@href').extract()[story]
            item.save()