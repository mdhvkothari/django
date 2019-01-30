# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserProfile,motivational,tech
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import UserInfoForm


@login_required(login_url='accounts:login')
def home(request):
    user_data = UserProfile.objects.all().order_by('id')[0:3]
    moti_data = motivational.objects.all().order_by('id')[0:3]
    tech_data = tech.objects.all().order_by('id')[0:3]
    return render(request,'accounts/home.html',{'user_data':user_data,'moti_data':moti_data,'tech_data':tech_data})

# def register(request):
#     if request.method == 'POST':
#         form = RegistraionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             login(request, user)
#             return redirect('/account')
#
#         else:
#             print(form.errors)
#     else:
#         form = RegistraionForm()
#         args = {'form':form}
#         return render(request,'accounts/reg_from.html',args)

def register(request):

    if request.method=='POST':

        user_info = UserInfoForm(request.POST)

        if user_info.is_valid() :

            user = user_info.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()
            return render(request,'accounts/home.html')
        else:
            print(user_info.errors)
    else:

        user_info = UserInfoForm()

    return render(request,'accounts/reg_from.html',{'form':user_info})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/account')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/reg_from.html', {'form': form})


@login_required(login_url='accounts:login')
def person_detail(request,slug):
    detail_person = UserProfile.objects.get(id=slug)
    return render(request,'accounts/detail.html',{'detail_person':detail_person})

@login_required(login_url='accounts:login')
def moti_detail(request,slug):
    moti_person = motivational.objects.get(id=slug)
    return render(request,'accounts/detail_moti.html',{'moti_person':moti_person})

@login_required(login_url='accounts:login')
def tech_detail(request,slug):
    tech_person = tech.objects.get(id=slug)
    return render(request,'accounts/detail_tech.html',{'tech_person':tech_person})
