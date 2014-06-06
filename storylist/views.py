from django.shortcuts import render
from storylist.models import Story
from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from django.http import HttpResponse
from storylist.models import Story
from django.template import Context
 
def index(request):
    six_hours_ago = datetime.utcnow() - timedelta(hours=6)
    stories = Story.objects.filter(added__gt=six_hours_ago).all()
    context = Context({
        'story_list': stories
    })

    return render(request, '../templates/index.html', context)