from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required,permission_required
from .forms import CategoryForm,BlogForm,AddUserForm,EditUserForm
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your views here.
@login_required(login_url='login-page')
def dashboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',context)

# Category CRUD
def categories(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,'dashboard/categories.html',context)

def add_category(request):
    # if request.method=="POST":
    #     category_name=request.POST.get('category_name')
        
    #     new_category=Category(category_name=category_name)
    #     new_category.save()
    #     return redirect('categories')
    if request.method=='POST':
        form=CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:    
        form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_category2.html',context)
    
def edit_category(request,id):
    # if request.method=="POST":
    #     req_category=get_object_or_404(Category,id=id)
        
    #     new_category_name=request.POST.get('category_name')
    #     req_category.category_name=new_category_name
    #     req_category.save()
    #     return redirect('categories')
    
    req_category=get_object_or_404(Category,id=id)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=req_category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:    
        form=CategoryForm(instance=req_category)
    context={
        'req_category':req_category,
        'form':form,
    }
    return render(request,'dashboard/edit_category2.html',context)
    
def delete_category(request,id):
    req_category=get_object_or_404(Category,id=id)
    req_category.delete()
    return redirect('categories')
    
# Blog CRUD    
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        
        if form.is_valid():
            post=form.save(commit=False)#commit=false do not update database yet,but gives an object with updated data
            
            post.author=request.user
            post.save()
            post.slug=slugify(post.title)+'-'+str(post.id)
            post.save()
            
            return redirect('posts')
    else:
        form=BlogForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_post.html',context)
       
def edit_post(request,id):
    req_post=get_object_or_404(Blog,id=id)
    if request.method=='POST':
        form=BlogForm(request.POST,instance=req_post)
        
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form=BlogForm(instance=req_post)
    context={
        'form':form,
        'req_post':req_post,
    }
    return render(request,'dashboard/edit_post.html',context)

def delete_post(request,id):
    req_post=get_object_or_404(Blog,id=id)
    req_post.delete()
    return redirect('posts')

def users(request):
    users=User.objects.all()
    context={
        'users':users,
    }
    return render(request,'dashboard/users.html',context)

def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=AddUserForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_user.html',context)
       
def edit_user(request,id):
    req_user=get_object_or_404(User,id=id)
    if request.method=='POST':
        form=EditUserForm(request.POST,instance=req_user)
        
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=EditUserForm(instance=req_user)
    context={
        'form':form,
        'req_user':req_user,
    }
    return render(request,'dashboard/edit_user.html',context)

@permission_required('auth.delete_user',raise_exception=True)
def delete_user(request,id):
    req_user=get_object_or_404(User,id=id)
    req_user.delete()
    return redirect('users')
