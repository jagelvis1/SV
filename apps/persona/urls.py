# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.persona.views import index, personaView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', personaView, name='personaView'),
]
