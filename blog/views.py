from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.http import Http404


def post_list(request):
    posts=Post.objects.all()
    return render( request,'blog/post/list.html',{'posts':posts})

def post_detail(request,id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise  Http404("No Post Found. ")
    return render(request,'blog/post/detail.html',{'post':post})

# Create your views here.
