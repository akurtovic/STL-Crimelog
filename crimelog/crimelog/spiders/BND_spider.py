from scrapy.spider import Spider
from scrapy.selector import Selector
from crimelog.items import Story
from datetime import datetime
from crimelog.helpers import dupCheck

import sys

sys.dont_write_bytecode = True

class BND(Spider):
    name = "news-democrat"
    allowed_domains = ["bnd.com"]
    start_urls = ["http://www.bnd.com/crime-news/"]

    def parse(self, response):
        sel = Selector(response)
        stories = sel.xpath('//div[@class="article_text"]').extract()

        for story in range(len(stories)):
            item = Story()
            item['headline'] = sel.xpath('//div[@class="article_text"]/h3/a/text()').extract()[story]
            item['url'] = "http://www.bnd.com/" + sel.xpath('//div[@class="article_text"]/h3/a/@href').extract()[story]
            item['source'] = "Belleville News-Democrat"
            item['added'] = datetime.now()

            if item['headline'] == "CRIME":
                pass
            elif item['headline'] == "TOP STORIES":
                pass
            elif "Neighborhood watch" in item['headline']:
                pass
            else:
                item.save()