from django.shortcuts import render
from storylist.models import Story
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from django.http import HttpResponse
from storylist.models import Story
from django.template import Context
 
def index(request):
    past_week = datetime.now() - timedelta(days=7)
    stories = Story.objects.filter(added__gt=past_week).all()
    context = Context({
        'story_list': reversed(stories)
    })

    return render(request, '../templates/index.html', context)