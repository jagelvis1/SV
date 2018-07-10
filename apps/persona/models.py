# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=13)
    nombre_cliente = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=1)  
    num_documento = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=200)
    estatus = models.CharField(max_length=8)

    def __unicode__(self):
        return self.nombre_cliente