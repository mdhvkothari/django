# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    about = models.TextField(max_length=100000,default='')
    link = models.CharField(max_length=500,default='')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.about[0:60]

class motivational(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    about = models.TextField(max_length=100000,default='')
    link = models.CharField(max_length=500,default='')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.about[0:60]


class tech(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    about = models.TextField(max_length=100000,default='')
    link = models.CharField(max_length=500,default='')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.about[0:60]
