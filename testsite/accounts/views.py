# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import UserProfile,motivational,tech,music
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import(
    authenticate,
    get_user_model,
)
from .forms import UserLoginForm,UserRegisterForm


@login_required(login_url='accounts:login')
def home(request):
    user_data = UserProfile.objects.all().order_by('id')[0:3]
    moti_data = motivational.objects.all().order_by('id')[0:3]
    tech_data = tech.objects.all().order_by('id')[0:3]
    music_data = music.objects.all().order_by('id')[0:3]
    # music_data = music.objects.all().order_by('id')[0:3]
    return render(request,'accounts/home.html',{'user_data':user_data,'moti_data':moti_data,'tech_data':tech_data,'music_data':music_data})

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


def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        auth_login(request,user)
        return redirect("/account")
    return render(request,'accounts/login.html',{"form":form})




def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=username,password=password)
        auth_login(request,new_user)
        return redirect("/account")

    return render(request,'accounts/reg_from.html',{"form":form})


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

@login_required(login_url='accounts:login')
def music_detail(request,slug):
    music_person = music.objects.get(id=slug)
    return render(request,'accounts/music_detail.html',{'music_person':music_person})

def about(request):
    return render(request,'accounts/about.html')


# @login_required(login_url='accounts:login')
# def music_detail(request,slug):
#     music_person = tech.objects.get(id=slug)
#     return render(request,'accounts/music_detail.html',{'music_person':music_person})
