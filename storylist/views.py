from django.shortcuts import render
from storylist.models import Story
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)

    return render_to_response('../templates/index.html', context)
