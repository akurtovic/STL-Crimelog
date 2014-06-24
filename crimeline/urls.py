from django.conf.urls import patterns, include, url
from django.contrib import admin
from storylist import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^sixhours.html', views.sixHours, name='sixhours'),
    url(r'^twelvehours.html', views.twelveHours, name='twelvehours'),
    url(r'^day.html', views.day, name='day'),
    url(r'^week.html', views.week, name='week'),
    url(r'^month.html', views.month, name='month'),
    url(r'^postdispatch.html', views.PD, name='pd'),
    url(r'^ksdk.html', views.KSDK, name='ksdk'),
    url(r'^kmov.html', views.KMOV, name='kmov'),
    url(r'^rft.html', views.RFT, name='rft'),
    url(r'^kmox.html', views.KMOX, name='kmox'),
    url(r'^bnd.html', views.BND, name='bnd'),
)