from django.shortcuts import render
from storylist.models import Story
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from django.http import HttpResponse
from storylist.models import Story
from django.template import Context

def index(request):
	"""
	Main Index View:
	Displays all stories crawled in the past 24 hours
	"""
	past24 = datetime.now() - timedelta(days=1)
	stories = Story.objects.filter(added__gt=past24).all()
	count = len(stories)
	context = Context({
		'story_list': reversed(stories),
		'story_count': count
	})
	return render(request, './templates/index.html', context)

def filter_view(request):
	"""
	Filter view: NOT IMPLEMENTED YET
	"""
	source_specified = False

	if (request.GET.get('time')):
		hours_filter = request.GET.get('time')
	else:
		hours_filter = 24

	if (request.GET.get('source')):
		source_filter = request.GET.get('source')

		if(source_filter=="all"):
			source_specified = False
		else:
			source_specified = True


	offset = datetime.now() - timedelta(hours=int(hours_filter))

	# Needs conditional in case user selects "all" sources
	if (source_specified):
		stories = Story.objects.filter(added__gt=offset, source=source_filter).all()
	else:
		stories = Story.objects.filter(added__gt=offset).all()

	count = len(stories)
	context = Context({
		'story_list': reversed(stories),
		'story_count': count
		})
	return render(request, './templates/filter.html', context)