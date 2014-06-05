from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story
from datetime import datetime

import sys
sys.dont_write_bytecode = True

class KSDKfeatured(Spider):
    name = "ksdk_featured"
    allowed_domains = ["ksdk.com"]
    start_urls = ["http://www.ksdk.com/local/crime-news/"]

    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//div[@class="hero-story"]').extract()
        
        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//div[@class="hero-story"]/h1/a/text()').extract()[story]
            item['url'] = "http://www.ksdk.com" + sel.xpath('//div[@class="hero-story"]/h1/a/@href').extract()[story]
            item['source'] = "KSDK"
            item['added'] = datetime.now()
            item.save()