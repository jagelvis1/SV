# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.PersonaCreate import PersonaForm
# Create your views here.
def index(request):
    return render(request,'persona/index.html')

def PersonaView(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('persona:index')
	else:
		form = PersonaForm()

	return render(request, 'persona/CreatePersona.html', {'form':form})			  