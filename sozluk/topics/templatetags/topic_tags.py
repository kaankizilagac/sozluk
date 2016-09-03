# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import template
from django.utils.timezone import now

from sozluk.topics.models import Topic

register = template.Library()


@register.assignment_tag(name="today_topics")
def today_topics():
    return Topic.objects.filter(created_at__day=now().day).order_by('title')
