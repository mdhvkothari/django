# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivational',
            name='suscriber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='music',
            name='suscriber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='tech',
            name='suscriber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='suscriber',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
