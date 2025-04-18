
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
     path('<int:pk>/like/', views.like_post, name='like_post'),
     path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    
]
