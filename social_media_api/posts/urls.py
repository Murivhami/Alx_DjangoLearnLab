
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
     path('', include(router.urls)),
     path('feed/', views.user_feed, name='user_feed'),
     path('posts/<int:pk>/like', views.follow_user, name='follow_user'),
     path('posts/<int:pk>/unlike', views.follow_user, name='follow_user'),
    
]
