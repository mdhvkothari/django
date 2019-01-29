# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile,motivational,tech
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(motivational)
admin.site.register(tech)
