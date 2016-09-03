from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from sozluk.users.models import User
from sozluk.topics.models import Topic, Entry, Category
from sozluk.topics.forms import EntryForm


def home(request):
    # q_main_topic = Entry.objects.filter(user_id=request.user.id).order_by('created_at').select_related('topic')[:1]
    topic = Topic.objects.all().order_by('?').first()
    q_main_topic = Entry.objects.filter(topic=topic)

    Category.objects.all()

    user = User.objects.all()
    form = EntryForm()
    context = {
        "q_main_topic": q_main_topic,
        "topic": topic,
        "form": form
    }

    return render(request, 'base3.html', context)


@login_required
def new_entry(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        user = request.user

        if form.is_valid():
            entry = form.save(commit=False)
            topic_id = request.POST.get('topic_id', None)
            if not topic_id:
                status = 402
                data = {"message": "topic eksik"}
            else:
                entry.topic_id = topic_id
                entry.user = user
                entry.save()
                data = {"message": "ok", "content": entry.content}
                status = 200
        else:
            status = 400
            data = form.errors.as_json()

        return JsonResponse(data=data, status=status)


def entry_page(request, slug):

    entry_category = Category.objects.all()
    qs_category = Entry.objects.filter(category=entry_category)

    context = {
        "qs_category": qs_category
        }

    return render(request, "pages/entrypage.html", context)
