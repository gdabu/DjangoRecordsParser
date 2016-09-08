from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^period/$', views.period),
	url(r'^poll/$', views.poll),
    url(r'^$', views.index, name='index'),
]