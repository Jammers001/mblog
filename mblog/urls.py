# -*- coding: utf-8 -*-

from django.conf.urls import url,include
from django.contrib import admin
from mainsite.views import homepage
urlpatterns = [
    url(r'^$',homepage),
    url(r'^admin/', include(admin.site.urls)),
]
