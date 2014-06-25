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
	past24 = datetime.now() - timedelta(days=1)
	stories = Story.objects.filter(added__gt=past24).all()
	context = Context({
		'story_list': reversed(stories)
	})
	return render(request, './templates/index.html', context)


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

<<<<<<< HEAD
=======
def all(request):
    stories = Story.objects.all()
    context = Context({
        'story_list': reversed(stories)
    })
    return render(request, './templates/all.html', context)

>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443
def PD(request):
	stories = Story.objects.filter(source="Post-Dispatch").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD

	return render(request, 'templates/postdispatch.html', context)
=======
	return render(request, './templates/postdispatch.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443


def KSDK(request):
	stories = Story.objects.filter(source="KSDK").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD

	return render(request, 'templates/ksdk.html', context)
=======
	return render(request, './templates/ksdk.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443


def KMOV(request):
	stories = Story.objects.filter(source="KMOV").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD

	return render(request, 'templates/kmov.html', context)
=======
	return render(request, './templates/kmov.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443


def RFT(request):
	stories = Story.objects.filter(source="Riverfront Times").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD

	return render(request, 'templates/rft.html', context)
=======
	return render(request, './templates/rft.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443


def KMOX(request):
	stories = Story.objects.filter(source="KMOX").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD

	return render(request, 'templates/kmox.html', context)
=======
	return render(request, './templates/kmox.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443


def BND(request):
	stories = Story.objects.filter(source="Belleville News-Democrat").all()
	context = Context ({
		'story_list': reversed(stories)
		})
<<<<<<< HEAD
	return render(request, 'templates/bnd.html', context)


=======
	return render(request, './templates/bnd.html', context)
>>>>>>> 00e3bead81afc4389d75c2248683e1356e31e443
