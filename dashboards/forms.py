from blogs.models import Category,Blog
from django import forms
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
                
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','featured_image','short_description','blog_body','status','is_featured')
        
        
        
        