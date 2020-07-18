from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog


def index(request):
    return render(request,'blog/index.html')

def details(request):
    data = Blog.objects.all()
    return render(request,'blog/details.html',context={'data': data})

def read(request,id):
    data = get_object_or_404(Blog, id=id)
    return render(request,'blog/read.html',context={'data':data})