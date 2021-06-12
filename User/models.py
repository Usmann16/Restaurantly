# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.conf import settings
from vendor.models import restuarantInformation

from django.db import models

# Create your models here.

class signup (models.Model):
    Username = models.TextField()
    email = models.TextField()
    password = models.TextField()
    confirmPassword = models.TextField()

    def __str__(self):
        return self.Username

# class review(models.Model):


class review(models.Model):
    u_id = models.AutoField(auto_created=True, primary_key=True, unique=True, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)
    res_name = models.ForeignKey(restuarantInformation, blank=False, on_delete=models.CASCADE)

    title = models.CharField(max_length=500)
    reviews = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class reply(models.Model):
    user_id = models.ForeignKey(review, to_field='u_id', on_delete=models.CASCADE)

    replys = models.TextField()


class contacts(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.email


