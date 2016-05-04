from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^searchPage/$', views.searchPage, name='searchPage'),
    url(r'^findTweets/$', views.findTweets, name='findTweets'),
    url(r'^themes/$', views.themes, name='themes'),


]
