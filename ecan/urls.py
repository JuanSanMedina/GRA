from django.conf.urls import patterns, url
from ecan import views


urlpatterns = patterns('',
	url(r'^upload/', views.upload_item, name='upload'),
	url(r'^upload-ecan/', views.upload_ecan, name='upload-ecan'),
	url(r'^view/', views.view_item, name='view'),
	url(r'^test/', views.home, name='home'),
)