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

def sixHours(request):
    past_six = datetime.now() - timedelta(hours=6)
    stories = Story.objects.filter(added__gt=past_six).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/sixhours.html', context)

def twelveHours(request):
    past_twelve = datetime.now() - timedelta(hours=12)
    stories = Story.objects.filter(added__gt=past_twelve).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/twelvehours.html', context)


def day(request):
    past_day = datetime.now() - timedelta(days=1)
    stories = Story.objects.filter(added__gt=past_day).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/day.html', context)


def week(request):
    past_week = datetime.now() - timedelta(days=7)
    stories = Story.objects.filter(added__gt=past_week).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/week.html', context)


def month(request):
    past_month = datetime.now() - timedelta(days=30)
    stories = Story.objects.filter(added__gt=past_month).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/month.html', context)

def PD(request):
	stories = Story.objects.filter(source="Post-Dispatch").all()
	context = Context ({
		'story_list': reversed(stories)
		})

	return render(request, './templates/postdispatch.html', context)


def KSDK(request):
	stories = Story.objects.filter(source="KSDK").all()
	context = Context ({
		'story_list': reversed(stories)
		})
	return render(request, './templates/ksdk.html', context)



def KMOV(request):
	stories = Story.objects.filter(source="KMOV").all()
	context = Context ({
		'story_list': reversed(stories)
		})
	return render(request, './templates/kmov.html', context)



def RFT(request):
	stories = Story.objects.filter(source="Riverfront Times").all()
	context = Context ({
		'story_list': reversed(stories)
		})
	return render(request, './templates/rft.html', context)

def KMOX(request):
	stories = Story.objects.filter(source="KMOX").all()
	context = Context ({
		'story_list': reversed(stories)
		})
	return render(request, './templates/kmox.html', context)



def BND(request):
	stories = Story.objects.filter(source="Belleville News-Democrat").all()
	context = Context ({
		'story_list': reversed(stories)
		})
	return render(request, './templates/bnd.html', context)