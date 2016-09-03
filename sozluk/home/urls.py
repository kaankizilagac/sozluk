# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'new/$', views.new_entry, name='new_entry'),
    url(r'(?P<slug>[\w-]+)/$', views.entry_page, name='entry_page'),

    ]
