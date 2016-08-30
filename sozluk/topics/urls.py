# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^today/$', views.today_topic, name='today-topic'),
    url(r'^popular/$', views.popular_topic, name='popular-topic'),
    url(r'^channels/(?P<category>[\w-]+)/$', views.channels, name='channels-topic'),
    ]
