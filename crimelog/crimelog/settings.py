# Scrapy settings for crimelog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import imp, os

sys.path.insert(0, '/home/amirkurtovic/STL-Crimelog')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'crimeline.settings'


sys.dont_write_bytecode = True

BOT_NAME = 'crimelog'

SPIDER_MODULES = ['crimelog.spiders']
NEWSPIDER_MODULE = 'crimelog.spiders'
ITEM_PIPELINES = {
    #'crimelog.pipelines.JsonWriterPipeline':300,
    'crimelog.pipelines.CrimelogDuplicates':100,
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crimelog (+http://www.yourdomain.com)'


