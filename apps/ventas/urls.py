# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.ventas.views import index_ventas, FacturaList, FacturaCreate

urlpatterns = [
    url(r'^index$', index_ventas),
    url(r'^nuevo$', FacturaCreate.as_view(), name='FacturaView'),
    url(r'^listar$', FacturaList.as_view(), name='ventaList'),

]
