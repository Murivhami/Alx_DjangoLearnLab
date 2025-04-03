from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Post
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def user_feed(request):
    user = request.user
    followed_users = user.following.all()  # Get all users the current user follows
    
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Get posts from followed users, ordered by creation date
    post_data = []
    for post in posts:
        post_data.append({
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at,
        })

    return Response(post_data, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Post
from accounts.models import CustomUser

class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view
    
    def get(self, request):
        # Get the users the current user is following
        following_users = request.user.following.all()  # This gives all users the current user follows
        
        # Fetch posts from those users, ordered by creation date (most recent first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize posts data and return response
        post_data = [{
            "content": post.content,
            "username": post.user.username,
            "created_at": post.created_at,
        } for post in posts]
        
        return Response(post_data, status=status.HTTP_200_OK)


# Create your views here.
