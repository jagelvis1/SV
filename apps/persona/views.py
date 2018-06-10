# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import personaForm
# Create your views here.
def index(request):
    return render(request,'persona/index.html')

def personaView(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('persona:index') 
    else:
        form = personaForm()
    
    return render(request,'persona/personaForm.html',{'form':form})       