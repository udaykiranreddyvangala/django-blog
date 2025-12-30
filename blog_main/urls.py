"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blogs_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.registerpage,name='register-page'),
    path('login/',views.loginpage,name='login-page'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home-page'),
    path('category/',include('blogs.urls')),
    path('blog/search/',blogs_views.search,name='search'),
    path('dashboard/',include('dashboards.urls')), 
    path('<slug:slug>/',blogs_views.blog_page,name="blog-page")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
