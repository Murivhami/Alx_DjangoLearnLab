from django.contrib import admin
from django.urls import path, include
from posts.views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = [
     path('posts/', include('router.urls')),
]
