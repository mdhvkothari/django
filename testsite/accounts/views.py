# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from accounts.forms import RegistraionForm
from .models import UserProfile,motivational,tech

def home(request):
    user_data = UserProfile.objects.all().order_by('id')[0:3]
    moti_data = motivational.objects.all().order_by('id')[0:3]
    tech_data = tech.objects.all().order_by('id')[0:3]
    return render(request,'accounts/home.html',{'user_data':user_data,'moti_data':moti_data,'tech_data':tech_data})


def register(request):
    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    
    else:
        form = RegistraionForm()
        args = {'form':form}
        return render(request,'accounts/reg_from.html',args)

def person_detail(request,slug):
    detail_person = UserProfile.objects.get(id=slug)
    return render(request,'accounts/detail.html',{'detail_person':detail_person})


def moti_detail(request,slug):
    moti_person = motivational.objects.get(id=slug)
    return render(request,'accounts/detail_moti.html',{'moti_person':moti_person})


def tech_detail(request,slug):
    tech_person = tech.objects.get(id=slug)
    return render(request,'accounts/detail_tech.html',{'tech_person':tech_person})
