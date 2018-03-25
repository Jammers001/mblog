# -*- coding: utf-8 -*-

from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    post_lists=list()
    for count,post in enumerate(posts):
        post_lists.append('No.{}:'.format(str(count))+str(post)+'<br>')
        post_lists.append('<font size="3" color="blue">'+str(post.body)+
                          '</font><br><br>')
    return HttpResponse(post_lists)