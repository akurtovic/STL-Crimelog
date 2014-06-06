from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story
from datetime import datetime

import sys
sys.dont_write_bytecode = True

class KMOXfeatured(Spider):
    name = "kmox_featured"
    allowed_domains = ["stlouis.cbslocal.com"]
    start_urls = ["http://stlouis.cbslocal.com/category/news/crime/"]

    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//ul[@class="slides"]/li/a[@class="node"]').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//ul[@class="slides"]/li/a[@class="node"]/div/p[@class="title"]/text()').extract()[story]
            item['url'] = sel.xpath('//ul[@class="slides"]/li/a[@class="node"]/@href').extract()[story]
            item['source'] = "KMOX"
            item['added'] = datetime.now()

            item.save()