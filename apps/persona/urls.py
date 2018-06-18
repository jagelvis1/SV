# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.persona.views import index
from apps.persona.views import personaView
from apps.persona.views import personaList, personaListid
from apps.persona.views import personaEdit, personaDelete
from apps.persona.views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', PersonaCreate.as_view(), name='personaView'),
    url(r'^listar$', PersonaList.as_view(), name='personaList'),
    url(r'^editar/(?P<pk>[0-9]+)/$', PersonaUpdate.as_view(), name='personaEdit'),
    url(r'^detalle/(?P<id_cliente>[0-9]+)/$', personaListid, name='personaShow'),
    url(r'^eliminar/(?P<pk>[0-9]+)/$', PersonaDelete.as_view(), name='personaDelete'),

]
