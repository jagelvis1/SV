# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class tipo_documento(models.Model):
    id_tipodoc = models.AutoField(primary_key=True)
    name_tipodoc = models.CharField(max_length=1)  

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=13)
    nombre_cliente = models.CharField(max_length=100)
    tipo_doc = models.ForeignKey(tipo_documento, null=True, blank=True, on_delete=models.CASCADE)
    num_documento = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=200)
    estatus = models.CharField(max_length=8)