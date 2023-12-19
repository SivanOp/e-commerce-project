from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CustomUserCreationSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

def home_view(request):
    # Add any additional logic you need for the home page view
    return render(request, 'authentication/home.html')

def success_signup_view(request):
    return render(request, 'authentication/success_signup.html')

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomUserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Add any additional logic here
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        custom_username = request.data.get('custom_username')
        custom_password = request.data.get('custom_password')
        
        if custom_username is not None and custom_password is not None:
            user = authenticate(request, custom_username=custom_username, custom_password=custom_password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

        return Response({'error_message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
