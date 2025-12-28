from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  blogs.models import Category,Blog


def home(request):
    categories=Category.objects.all()
    featured_blogs=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status="Published").order_by('updated_at')
    context={
        'categories':categories,
        'featured_blogs':featured_blogs,
        'posts':posts,
    }
    
    print(posts)
    return render(request,'home.html',context)