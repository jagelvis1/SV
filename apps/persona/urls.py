# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.persona.views import index

urlpatterns = [
    url(r'^$', index),
]
