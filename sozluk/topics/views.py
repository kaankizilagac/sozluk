from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render

from sozluk.topics.models import Topic, Entry
from django.utils.timezone import now


def today_topic(request):
    q_today = Topic.objects.filter(created_at__day=now().day).order_by('title')
    query_today = serializers.serialize('json', q_today)
    return HttpResponse(query_today, content_type="application/json")


def popular_topic(request):
    q_popular = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
    query_popular = serializers.serialize('json', q_popular)
    return HttpResponse(query_popular, content_type="application/json")


def junior_topic(request):
    query_junior = Entry.objects.filter()


def channels(request):
    print('asdasd')
    q_channels = Topic.objects.values_list('title'
                                           )
    query_channels = serializers.serialize('json', q_channels)
    print(query_channels)
    return HttpResponse(query_channels, content_type="application/json")





