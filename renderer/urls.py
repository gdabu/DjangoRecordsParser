from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^date/$', views.period, name='index'),
	url(r'^poll/$', views.poll, name='index'),
    url(r'^$', views.index, name='index'),
]