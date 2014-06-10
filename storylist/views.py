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
	Displays all stories crawled in the past week
	"""
	past_week = datetime.now() - timedelta(days=7)
	stories = Story.objects.filter(added__gt=past_week).all()
	context = Context({
		'story_list': reversed(stories)
	})
	return render(request, '../templates/index.html', context)

def sixHours(request):
    past_six = datetime.now() - timedelta(hours=6)
    stories = Story.objects.filter(added__gt=past_six).all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, '../templates/sixhours.html', context)