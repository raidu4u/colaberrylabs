# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        return render(request, 'users/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    
def index(request):
    return render(request, 'users/home.html')
    
