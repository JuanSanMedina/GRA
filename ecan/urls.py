from django.conf.urls import patterns, url
from ecan import views


urlpatterns = patterns('',
                       url(r'^upload/', views.upload_item,
                           name='upload'),
                       url(r'^upload-back_ground/', views.upload_bg,
                           name='upload-back_ground'),
                       url(r'^upload-sample/', views.upload_sample,
                           name='upload-sample'),
                       url(r'^upload-ecan/', views.upload_ecan,
                           name='upload-ecan'),
                       url(r'^view/', views.view_item,
                           name='view'),
                       url(r'^view-ip/', views.view_ip,
                           name='view-ip'),
                       url(r'^home/', views.home,
                           name='home'),
                       url(r'^index/', views.index,
                           name='index'),
                       url(r'^sample/', views.show_sample,
                           name='show_sample'),
                       url(r'^insert/', views.insert_attribute,
                           name='insert_attribute'),
                       )
