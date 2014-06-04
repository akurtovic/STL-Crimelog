# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import sys
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
from storylist.models import Story

sys.dont_write_bytecode = True

class Story(DjangoItem):
    django_model = Story