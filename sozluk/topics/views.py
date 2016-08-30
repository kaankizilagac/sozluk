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

# def junior_topic(request):
#     query_junior = Entry.objects.filter(topic__user=)


def channels(request, category):
    q_channels = Topic.objects.filter(category=category).prefetch_related('title')
    query_channels = serializers.serialize('json', q_channels)
    print(query_channels)
    return HttpResponse(query_channels, content_type="application/json")


def mainpage_qs(request, title):

    q_main_topic = Entry.objects.filter(user_id=request.user.id).order_by('created_at').select_related('topic')[:1]
    print(q_main_topic)
    q_main_entry = Entry.objects.filter()

    context = {
        "q_main_topic": q_main_topic,
        "q_main_entry": q_main_entry
    }

    return render(request, 'base3.html', context)














