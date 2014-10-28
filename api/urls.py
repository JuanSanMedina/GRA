from django.conf.urls import patterns, include, url
from django.contrib import admin
from ecan import views
from api import settings

urlpatterns = patterns('',
	# Examples:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ecan/', include('ecan.urls', namespace="ecan")),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),
)