from scrapy.spider import Spider
from scrapy.selector import Selector

from crimelog.items import Story

import sys
sys.dont_write_bytecode = True

class KMOX(Spider):
    name = "kmox"
    allowed_domains = ["stlouis.cbslocal.com"]
    start_urls = ["http://stlouis.cbslocal.com/category/news/crime/"]

    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//div[@class="feature "]').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//div[@class="feature "]/div/h4/a/text()').extract()[story]
            item['url'] = sel.xpath('//div[@class="feature "]/div/h4/a/@href').extract()[story]
            item.save()