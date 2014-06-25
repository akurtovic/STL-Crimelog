from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from scrapy import log
from crimelog.helpers import dupCheck

class Countdown(object):
    counter = 15

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)

def setup_crawler(spider_name):
    crawler = Crawler(settings)
    crawler.configure()
    spider = crawler.spiders.create(spider_name)
    crawler.crawl(spider)
    crawler.start()

if __name__ == "__main__":

    log.start()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.configure()

    for spider_name in crawler.spiders.list():
        setup_crawler(spider_name)

    # set up Countdown callback to kill reactor after 10 seconds
    reactor.callWhenRunning(Countdown().count)

    # run reactor
    reactor.run()

    # Delete duplticate database entries, from helpers.py
    dupCheck()
