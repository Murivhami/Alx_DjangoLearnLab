from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)  # Create user
        user.set_password(password)  # Hash the password
        user.save()
        
        token, created = Token.objects.get_or_create(user=user)
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
