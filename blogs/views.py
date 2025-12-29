from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Category,Blog
from django.db.models import Q

# Create your views here.
def posts_by_category(request,category_id):
    category_blogs=Blog.objects.filter(category_id=category_id)
    
    # return HttpResponse(category_blogs)
    # try:
        # category=Category.objects.get(id=category_id)
    # except:
    #     return redirect('home-page')
    # Use get_object_or_404() if 404 error page is to be showed when category does not exist
    category=get_object_or_404(Category,id=category_id)
    context={
        'posts':category_blogs,
        'category_name':category.category_name
    }
    return render(request,'posts_by_category.html',context)
    
def blog_page(request,slug):
    req_blog=get_object_or_404(Blog,slug=slug)
    context={
        'post':req_blog,
    }
    return render(request,'blog_page.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body=keyword),status='Published')
    context={
        'posts':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)
    # return HttpResponse('{{}}')