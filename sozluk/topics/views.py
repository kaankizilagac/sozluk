from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.shortcuts import render

from sozluk.topics.models import Topic, Entry
from django.utils.timezone import now


def today_topic(request):
    q_today = Topic.objects.filter(created_at__day=now().day).order_by('title').values('title', 'slug')
    topics = []
    for q in q_today:
        data = {
            "title": q["title"],
            "url": reverse('home-general:entry_page', kwargs={"slug": q["slug"]})
        }
        topics.append(data)

    return JsonResponse(data=topics, safe=False)


def popular_topic(request):
    q_popular = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count').values('title', 'slug')
    pop_topics = []
    for qs in q_popular:
        data = {
            "title": qs["title"],
            "url": reverse('home-general:entry_page', kwargs={"slug": qs["slug"]})
        }
        pop_topics.append(data)

    return JsonResponse(data=pop_topics, safe=False)


def junior_topic(request):
    query_junior = Entry.objects.filter()


def channels(request):
    print('asdasd')
    q_channels = Topic.objects.values_list('title')
    query_channels = serializers.serialize('json', q_channels)
    print(query_channels)
    return HttpResponse(query_channels, content_type="application/json")





