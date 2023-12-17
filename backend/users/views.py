from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserProfileSerializer, UserSerializerWithToken, UserUpdateSerializerWithToken
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
        
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        
        for k, v in serializer.items():
            data[k] = v

        return data
    

@api_view(['POST']) 
def register(request):
    data = request.data
    try:
        user = CustomUser.objects.create(
            username = data['username'],
            email = data['email'],
            group = data['group'],
            password = make_password(data['password'])
        )
        
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'user with this email already exists!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    


"""
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user  # Assumes the user is authenticated
    if request.method == 'PUT':
        profile = user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request, username):
    if request.method == 'GET':
        try:
            user = CustomUser.objects.get(username=username)
            user_profile = Profile.objects.get(user=user)
             
            #Serialize the Data
            user_profile_serializer = CustomUserProfileSerializer(user_profile, many=False)
            
            return Response(user_profile_serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({'error': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['PUT'])
@permission_classes([IsAuthenticated])   
def update_user_profile(request):
    if request.method == 'PUT':
        user = request.user
        serializer = UserUpdateSerializerWithToken(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)