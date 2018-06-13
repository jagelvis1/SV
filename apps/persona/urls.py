# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.persona.views import index
from apps.persona.views import personaView
from apps.persona.views import personaList
from apps.persona.views import personaEdit, personaDelete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', personaView, name='personaView'),
    url(r'^listar$', personaList, name='personaList'),
    url(r'^editar/(?P<id_cliente>[0-9]+)/$', personaEdit, name='personaEdit'),
    url(r'^eliminar/(?P<id_cliente>[0-9]+)/$', personaDelete, name='personaDelete'),

]
