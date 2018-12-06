# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account is created')
            return redirect('home')
        return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    
def index(request):
    return render(request, 'users/home.html')
    
