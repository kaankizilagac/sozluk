from datetime import timedelta, datetime

from django.http import HttpResponse
from django.shortcuts import render

from sozluk.users.models import User
from sozluk.topics.models import Topic, Entry


def user_profile(request):

    q_top_last_entry = Entry.objects.filter(user_id=request.user.id).order_by('created_at').select_related('topic').last()

    # q_today = Topic.get_topic_today.all()
    # q_popular = Topic.get_topic_popular
    q_last_entry = Entry.objects.filter(user_id=request.user.id).order_by('created_at').select_related('topic')[:10]
    # print(q_last_entry)
    # q_last_entry = Topic.get_last_entry
    # q_last_topic = Topic.get_last_topic.all()

    # like_entry_weekly = Entry.get_like_entry_weekly
    # like_entry_general = Entry.get_like_entry_general
    # last_voting_entry = Entry.get_last_voting_entry

    context = {
        "q_top_last_entry": q_top_last_entry,
        # "q_today": q_today,
        "q_last_entry": q_last_entry,
        # "q_last_topic": q_last_topic,
        # "like_entry_weekly": like_entry_weekly,
        # "like_entry_general": like_entry_general,
        # "last_voting_entry": last_voting_entry
        }

    return render(request, 'pages/profil.html', context)
