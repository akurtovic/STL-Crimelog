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
    url(r'^index/', views.index, name='index'),
)
