# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from os.path import splitext

from IPython.utils.py3compat import annotate
from django.db import models
from django.db.models import signals, QuerySet, Count
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField

from sozluk.users.models import User
from .signals import check_junior


class Category(models.Model):
    title = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return "#{title}".format(title=self.title)


    # def get_topic_popular(self):
    #     return self.annotate(entry_count=Count('entry')).order_by('-entry_count')


class Topic(models.Model):

    objects = models.Manager()

    # get_topic_today = QueryManager(created_at__day=now().day).order_by('title')
    # get_topic_popular = QueryManager(entry_count=Count('entry')).order_by('-entry_count')
    # get_last_entry = QueryManager(filter(id__in=Entry.objects.filter(user_id=request.user_id).values_list()))
    # get_last_topic = QueryManager()

    user = models.ForeignKey(
        User,
        verbose_name=_("User")
    )
    title = models.CharField(
        max_length=140,
        unique=True,
        verbose_name=_("Title")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created at")
    )
    category = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=_("Category")
    )

    slug = AutoSlugField(
        populate_from='title',
        unique=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Baslik")
        verbose_name_plural = _("Basliklar")
        ordering = ('created_at',)


class Entry(models.Model):

    objects = models.Manager()
    #
    # get_like_entry_weekly = QueryManager()
    # get_like_entry_general = QueryManager()
    # get_last_voting_entry = QueryManager()

    user = models.ForeignKey(
        User,
        verbose_name=_("User")
    )
    topic = models.ForeignKey(
        Topic,
        verbose_name=_("Topic")
    )
    content = models.TextField(
        verbose_name=_("Content")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Created at")
    )


signals.post_save.connect(check_junior, sender=Entry)


class Favourite(models.Model):
    entry = models.ForeignKey(
        Entry
    )
    user = models.ForeignKey(
        User,
    )

    class Meta:
        unique_together = (('entry', 'user'),)
