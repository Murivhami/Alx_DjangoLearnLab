from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, TokenSerializer

class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.exceptions import NotFound

class FollowUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        """
        Follow a user by adding them to the following list of the current user.
        """
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")

        # Prevent users from following themselves
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the following list
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        """
        Unfollow a user by removing them from the following list of the current user.
        """
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")

        # Prevent users from unfollowing themselves
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user from the following list
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)


