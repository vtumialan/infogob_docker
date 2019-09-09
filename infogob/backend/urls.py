from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    url(r'^publisher/$', views.PublisherList.as_view()),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
    url(r'^scraping', views.scrapeSite),
    url(r'^regidor/$', views.scrapeRegion, name='request'),
]

urlpatterns = format_suffix_patterns(urlpatterns)