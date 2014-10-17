from django.conf.urls import patterns, url
from ecan import views


urlpatterns = patterns('',
	url(r'^upload/', views.upload_item, name='upload'),
	url(r'^test/', views.home, name='home'),
)