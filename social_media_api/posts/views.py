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
    permission_classes = [permissions.IsAuthenticated]  # Ensure that only authenticated users can access this view
    
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

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id):
        # Fetch the post object by post_id, if not found it raises a 404 error
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Use get_or_create to avoid duplicate likes by the same user on the same post
        like, created = Like.objects.get_or_create(post=post, user=user)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post's author
        notification = Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
            target=post
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id):
        # Fetch the post object by post_id, if not found it raises a 404 error
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the like
        like.delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
