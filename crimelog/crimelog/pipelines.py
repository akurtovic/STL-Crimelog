# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem
import sys
import imp, os
from storylist.models import Story
from time import sleep

sys.path.insert(0, '/Users/amir/Documents/stlcrime/')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'stlcrime.settings'

'''
class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('crimelog.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item
'''


class CrimelogDuplicates(object):
    '''
    Get rid of duplicate entries
    '''
    def __init__(self):
        self.headlines_seen = set()

    def process_item(self, item, spider):
        if item['headline'] in self.headlines_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.headlines_seen.add(item['headline'])
            return item
