# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile,motivational,tech,music
# Create your views here.

@login_required(login_url='accounts:login')
def detail(request):
    user_data = UserProfile.objects.all().order_by('id')
    return render(request,'allchannel/entertainment.html',{'user_data':user_data})

@login_required(login_url='accounts:login')
def moti(request):
    moti_data = motivational.objects.all().order_by('id')
    return render(request,'allchannel/motivational.html',{'moti_data':moti_data})

@login_required(login_url='accounts:login')
def tech_person(request):
    tech_data = tech.objects.all().order_by('id')
    return render(request,'allchannel/tech.html',{'tech_data':tech_data})

@login_required(login_url='accounts:login')
def music_person(request):
    music_data = music.objects.all().order_by('id')
    return render(request,'allchannel/music.html',{'music_data':music_data})
