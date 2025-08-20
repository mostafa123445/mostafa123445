from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.http import Http404


def post_list(request):
    posts=Post.objects.all()
    return render( request,'blog/post/list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    try:
        post=Post.objects.get(slug=post,publish__year=year,publish__month=month,publish__day=day)
    except Post.DoesNotExist:
        raise  Http404("No Post Found. ")
    return render(request,'blog/post/detail.html',{'post':post})

# Create your views here.
