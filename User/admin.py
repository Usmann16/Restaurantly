# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import signup, review,reply, contacts

# Register your models here.
admin.site.register(signup)
admin.site.register(review)
admin.site.register(reply)
admin.site.register(contacts)

