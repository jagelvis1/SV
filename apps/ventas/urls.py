# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.ventas.views import index_ventas

urlpatterns = [
    url(r'^index$', index_ventas),
]
