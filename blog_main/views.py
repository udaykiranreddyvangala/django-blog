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

def registerpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if len(password)<3:
            # print('Password must be atleast 3 characters')
            messages.error(request,'Password must be atleast 3 characters')
            return redirect('register-page')
        
        get_all_users_by_username=User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,'username already exits')
            return redirect('register-page')
            
        # print(username)
        
        newuser=User.objects.create_user(username=username,email=email,password=password)
        newuser.save()
        messages.success(request,'Registration Success')
        return redirect('login-page')
    return render(request,'register.html')
    # return HttpResponse('<h3>Hello,World!</h3>')

def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login-page')
    
    
    return render(request,'login.html')
    # return HttpResponse('<h1>Hello,World!</h1>')

def logout_view(request):
    logout(request)
    return redirect('login-page')
