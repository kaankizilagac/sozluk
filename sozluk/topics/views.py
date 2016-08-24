from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from sozluk.topics.models import Topic, Entry
import json


def today_topic(request):
    query_today = Topic.get_topic_today.all()
    query_today = serializers.serialize('json', query_today)
    return HttpResponse(query_today, content_type="application/json")


def popular_topic(request):
    query_popular = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
    query_popular = serializers.serialize('json', query_popular)
    return HttpResponse(query_popular, content_type="application/json")

# def junior_topic(request):
#     query_junior = Entry.objects.filter(topic__user=)




















