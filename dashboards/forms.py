from blogs.models import Category,Blog
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
        
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'