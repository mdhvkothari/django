# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motivational',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('about', models.TextField(default='', max_length=100000)),
                ('link', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('suscriber', models.TextField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('about', models.TextField(default='', max_length=100000)),
                ('link', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('suscriber', models.TextField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tech',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('about', models.TextField(default='', max_length=100000)),
                ('link', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('suscriber', models.TextField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('about', models.TextField(default='', max_length=100000)),
                ('link', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('suscriber', models.TextField(default='', max_length=10)),
            ],
        ),
    ]
