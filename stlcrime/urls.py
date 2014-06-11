from django.conf.urls import patterns, include, url
from django.contrib import admin
from storylist import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stlcrime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^sixhours.html', views.sixHours, name='sixhours'),
    url(r'^twelvehours.html', views.twelveHours, name='twelvehours'),
    #url(r'^day.html', views.day, name='day'),
    #url(r'^week.html', views.week, name='week'),
    #url(r'^month.html', views.month, name='month'),
    #url(r'^all.html', views.all, name='all'),
    #url(r'^postdispatch.html', views.postDispatch, name='pd'),
    #url(r'^sixhours.html', views.sixHours, name='sixhours'),
)