# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^today/$', views.today_topic, name='today_topic'),
    url(r'^popular/$', views.popular_topic, name='popular_topic'),
    url(r'^channels/$', views.channels, name='channels-topic'),
    ]
