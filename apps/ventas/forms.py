
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django import forms
from apps.ventas.models import factura, detalle_factura
from apps.persona.models import cliente
from django.forms import formset_factory


class FacturaForm(forms.ModelForm):

    #cliente = forms.ModelChoiceField(queryset=cliente.objects.all()

    class Meta:
        model = factura

        fields = [
          'cliente',
          'fecha',
          'sub_total',
          'iva',
          'total',
          'estatus',
        ]

        labels = {
            'cliente':'Cliente',
            'fecha': 'Fecha',
            'sub_total':'Subtotal',
            'iva':'IVA',
            'total':'Total',
            'estatus':'Estatus',
        }

        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control selectpicker','data-live-search':'true','name':'cliente_id','id':'cliente_id'}),
            'sub_total': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Sub Total','id':'sub_total'}),
            'iva': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'IVA','id':'iva'}),
            'total': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Total','id':'total'}),
            'estatus': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Estatus','id':'estatus','value':'ACTIVO','type':'hidden'}),
        }

class Detalle_FacturaForm(forms.ModelForm):

    class Meta:
        model = detalle_factura

        fields = [
          'descripcion',
          'cantidad',
          'precio_unit',
          'precio_total',
        ]

        labels = {
            'descripcion':'Descripcion',
            'cantidad': 'Cantidad',
            'precio_unit':'Precio Unit.',
            'precio_total':'Precio Total',
        }

        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'sub_total': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Sub Total','id':'sub_total'}),
            'iva': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'IVA','id':'iva'}),
            'total': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Total','id':'total'}),
            'estatus': forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Estatus','id':'estatus','value':'ACTIVO','type':'hidden'}),
        }        

Detalle_FacturaFormSet = formset_factory(Detalle_FacturaForm)        