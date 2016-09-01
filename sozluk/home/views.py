from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from sozluk.topics.models import Topic, Entry


def home(request):
    # q_main_topic = Entry.objects.filter(user_id=request.user.id).order_by('created_at').select_related('topic')[:1]
    topic = Topic.objects.all().order_by('?').first()

    q_main_topic = Entry.objects.filter(topic=topic)

    q_main_entry = Entry.objects.filter()

    # new_entry = Entry.objects.create(content=content)

    context = {
        "q_main_topic": q_main_topic,
        "topic": topic,
        "slug": topic.slug,
    }

    return render(request, 'base3.html', context)


@login_required
def new_entry(request, new):

    if request.method == 'POST':

        content = request.POST.get('content')
        topic_id = request.POST.get('topic_id')

        new_entries = Entry.objects.create(content=content,
                                           user_id=request.user.id,
                                           topic_id=topic_id,
                                           )

        return HttpResponse({message: "ok"}, content_type="application/json")


