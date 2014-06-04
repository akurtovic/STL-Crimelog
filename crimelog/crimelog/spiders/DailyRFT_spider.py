from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story

import sys

sys.dont_write_bytecode = True

class DailyRFT(Spider):
    name = "dailyrft"
    allowed_domains = ["riverfronttimes.com"]
    start_urls = ["http://blogs.riverfronttimes.com/dailyrft/crime/"]

    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//h2[@class="entryHeadline"]').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//h2[@class="entryHeadline"]/a/text()').extract()[story]
            item['url'] = sel.xpath('//h2[@class="entryHeadline"]/a/@href').extract()[story]
            item.save()