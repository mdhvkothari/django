# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-05 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_core'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Core',
        ),
    ]
