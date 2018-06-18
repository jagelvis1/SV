# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.persona.forms import personaForm
from apps.persona.models import cliente
# Create your views here.
def index(request):
    return render(request,'persona/index.html')

#crear cliente
def personaView(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('persona:personaList') 
    else:
        form = personaForm()
    
    return render(request,'persona/personaForm.html',{'form':form})  

#Mostrar Cliente
def personaList(request):
    persona = cliente.objects.all().order_by('id_cliente')
    contexto = {'persona':persona}
    return render(request, 'persona/index.html',contexto)

def personaListid(request,id_cliente):
    persona = cliente.objects.exclude(id_cliente=id_cliente)
    contexto = {'persona':persona}
    return render(request, 'persona/index.html',contexto)    

def personaEdit(request, id_cliente):
    persona = cliente.objects.get(id_cliente=id_cliente)
    if request.method == 'GET':
        form = personaForm(instance=persona)
    else:
        form = personaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('persona:personaList')   
    return render(request,'persona/personaForm.html',{'form':form})    

def personaDelete(request,id_cliente):
    persona = cliente.objects.get(id_cliente=id_cliente)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona:personaList')   
    return render(request,'persona/personaDelete.html',{'persona':persona})    

#modelos basados en clase

class PersonaList(ListView):
    model = cliente
    template_name = 'persona/index.html'

class PersonaCreate(CreateView):
    model = cliente
    form_class = personaForm
    template_name = 'persona/personaForm.html'
    success_url = reverse_lazy('persona:personaList')

class PersonaUpdate(UpdateView):
    model = cliente
    form_class = personaForm
    template_name = 'persona/personaForm.html'
    success_url = reverse_lazy('persona:personaList')

class PersonaDelete(DeleteView):
    model = cliente
    template_name = 'persona/personaDelete.html'
    success_url = reverse_lazy('persona:personaList')