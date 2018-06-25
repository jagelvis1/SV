# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from apps.ventas.forms import FacturaForm, Detalle_FacturaForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from apps.ventas.models import factura, detalle_factura



# Create your views here.
def index_ventas(request):
    return HttpResponse("pagina principal de ventas")

class FacturaList(ListView):
    context_object_name = "factura"
    queryset = factura.objects.raw("SELECT * FROM ventas_factura where estatus='ACTIVO' order by nro_factura")
    template_name = "ventas/index.html"

class FacturaCreate(CreateView):
    model = factura
    template_name = 'ventas/ventaForm.html'
    form_class = FacturaForm
    second_form_class = Detalle_FacturaForm
    success_url = reverse_lazy('ventas:ventaList')

    def get_context_data(self,**kwargs):
        context = super(FacturaCreate,self).get_context_data(**kwargs)
        if 'form1' not in context:
            context['form1'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)    
        return context

    def post(self,request,*args,**kwargs): 
        self.object = self.get_object
        form1 = self.form_class(request.POST)  
        form2 = self.second_form_class(request.POST) 
        if form1.is_valid() and form2.is_valid():
            factura = form1.save(commit=False)   
            factura.detalle_factura = form2.save()
            factura.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render_to_response(self.get_context_data(form1 = form1,form2 = form2))    