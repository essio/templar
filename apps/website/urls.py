# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

from website import views

urlpatterns = patterns('',

      url(r'^',
        views.generic,
        name='generic'),

)
