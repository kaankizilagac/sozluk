# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = (
            "content",
        )
