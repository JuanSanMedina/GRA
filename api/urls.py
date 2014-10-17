from django.conf.urls import patterns, include, url
from django.contrib import admin
from ecan import views


urlpatterns = patterns('',
	# Examples:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ecan/', include('ecan.urls')),
	url(r'^$', views.home, name='home'),
)
