from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm

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
    if request.method=="POST":
        blog_title=request.POST.get('blog_title')
        
        new_blog=Blog(title=blog_title)
        new_blog.save()
        return redirect('categories')
    
    return render(request,'dashboard/add_post.html')
       
def edit_post(request,id):
    pass

def delete_post(request,id):
    pass
