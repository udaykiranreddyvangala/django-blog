from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Category,Blog

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
    

