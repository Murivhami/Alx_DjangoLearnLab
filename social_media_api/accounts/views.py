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

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user == user_to_follow:
        return JsonResponse({'error': 'You cannot follow yourself.'}, status=400)
    request.user.following.add(user_to_follow)
    return JsonResponse({'success': True, 'message': f'You are now following {user_to_follow.username}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return JsonResponse({'success': True, 'message': f'You have unfollowed {user_to_unfollow.username}'})


class ListFollowersView(generics.ListAPIView):
    """
    API view to list a user's followers.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(CustomUser.objects.all(), id=self.kwargs["user_id"])
        return user.followers.all()

class ListFollowingView(generics.ListAPIView):
    """
    API view to list users that the current user is following.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = get_object_or_404(CustomUser.objects.all(), id=self.kwargs["user_id"])  
        return user.following.all()
