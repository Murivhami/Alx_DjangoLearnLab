"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', PostListView.as_view(), name = 'post_list'),
    path('posts/new/', PostCreateView.as_view(), name = 'post_create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete'),
    #path('blog/', include('blog.urls')),
]
