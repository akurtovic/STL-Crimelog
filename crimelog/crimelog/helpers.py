"""
Helper functions for scrapy project
dupCheck():		Delete duplicate entries.
				Called after each reactor.run() in crimelog.py

"""
import sys
sys.path.insert(0, '/Users/amir/Documents/stlcrime/')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'stlcrime.settings'


from storylist.models import Story
from scrapy.contrib.djangoitem import DjangoItem


def dupCheck():
	'''
	Searches database for duplicate URL entries before saving item.
	item: Story object passed by each spider
	'''

	for url in Story.objects.values_list('url', flat=True).distinct():
		Story.objects.filter(pk__in=Story.objects.filter(url=url).values_list('id', flat=True)[1:]).delete()
