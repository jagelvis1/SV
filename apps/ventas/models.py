# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib.auth.models import User
from django.db import models
from apps.persona.models import tipo_documento, cliente

# Create your models here.
#class factura
class factura(models.Model):
    nro_factura = models.AutoField(primary_key=True)    
    cliente = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    sub_total =  models.DecimalField(decimal_places=2,max_digits=11)
    iva =  models.DecimalField(decimal_places=2,max_digits=11)
    total = models.DecimalField(decimal_places=2,max_digits=11)
    estatus = models.CharField(max_length=8)

#class detalle_factura
class detalle_factura(models.Model):
    id_detalle_factura = models.AutoField(primary_key=True)    
    factura = models.ForeignKey(factura, null=True, blagit add README.mdnk=True, on_delete=models.CASCADE)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio_unit = models.DecimalField(decimal_places=2,max_digits=11)
    precio_total = models.DecimalField(decimal_places=2,max_digits=11)
