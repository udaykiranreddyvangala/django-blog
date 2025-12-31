from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  blogs.models import Category,Blog
from .forms import RegistrationForm

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

def registerpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home-page')
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')

    #     if len(password)<3:
    #         messages.error(request,'Password must be atleast 3 characters')
    #         return redirect('register-page')
        
    #     get_all_users_by_username=User.objects.filter(username=username)
    #     if get_all_users_by_username:
    #         messages.error(request,'username already exits')
    #         return redirect('register-page')
        
    #     newuser=User.objects.create_user(username=username,email=email,password=password)
    #     newuser.save()
    #     messages.success(request,'Registration Success')
    #     return redirect('login-page')
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('login-page')
    else:   
        form=RegistrationForm()        
    context={
        'form':form,
    }
    return render(request,'register2.html',context)

def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home-page')
    # if request.method=='POST':
    #     username=request.POST.get('uname')
    #     password=request.POST.get('pass')
        
    #     validate_user=authenticate(username=username,password=password)
    #     if validate_user is not None:
    #         login(request,validate_user)
    #         return redirect('home-page')
    #     else:
    #         messages.error(request,'Invalid login credentials')
    #         return redirect('login-page')
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            validate_user=authenticate(username=username,password=password)
            if validate_user is not None:
                login(request,validate_user)
                return redirect('home-page')
            else:
                messages.error(request,'Invalid login credentials')
                return redirect('login-page')
    else:
        form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login2.html',context)

def logout_view(request):
    logout(request)
    return redirect('login-page')
