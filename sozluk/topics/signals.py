# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


def check_junior(sender, instance, created, **kwargs):
    # from .models import Entry  # avoid circled import

    if created and instance.user.junior:
        total_entry = sender.objects.filter(user=instance.user).count()
        if total_entry >= 2:
            instance.user.junior = False
            instance.user.save()

