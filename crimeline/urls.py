from django.conf.urls import patterns, include, url
from django.contrib import admin
from storylist import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^filter.html', views.filter_view, name='filter_view'),
    url(r'^filter.html(?P<time>[0-9])(?P<source>\w+)/$', views.filter_view, name='filter_view'),
)