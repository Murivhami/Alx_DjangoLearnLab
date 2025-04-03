from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    # Prevent a user from liking the same post multiple times
    if Like.objects.filter(user=user, post=post).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create like
    like = Like.objects.create(user=user, post=post)

    # Create notification
    notification = Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post,
        target_content_type=ContentType.objects.get_for_model(Post),
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    # Ensure the user has liked the post before
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Remove like
    like.delete()

    # Optionally, remove the notification for unliking
    Notification.objects.filter(actor=user, target=post, verb='liked').delete()

    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

# Create your views here.
