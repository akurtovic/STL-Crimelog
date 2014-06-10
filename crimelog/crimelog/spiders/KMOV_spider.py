from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story
from datetime import datetime

import sys
sys.dont_write_bytecode = True


class KMOV(Spider):
    name = "kmov"
    allowed_domains = ["kmov.com"]
    start_urls = ["http://www.kmov.com/news/crime/"]
    
    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//h3[@class="entry-title"]').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//h3[@class="entry-title"]/a/text()').extract()[story]
            item['url'] = sel.xpath('//h3/a[@class="storyLink"]/@href').extract()[story]
            if "http" not in item['url']:
                pass
            else:
                item['source'] = "KMOV"
                item['added'] = datetime.now()
                item.save()