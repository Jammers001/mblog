# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
#以上三行，是解决中文不能显示的方案

from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')

admin.site.register(Post,PostAdmin)
