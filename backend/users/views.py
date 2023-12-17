from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserProfileSerializer, ProfileSerializer
from .models import *

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = CustomUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_and_profile(request):
    user = request.user  # Assumes the user is authenticated
    if request.method == 'PUT':
        serializer = CustomUserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" # You can also create a separate view for updating only the profile
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
#@permission_classes([IsAuthenticated])
def get_user_profile(request, username):
    if request.method == 'GET':
        try:
            user = CustomUser.objects.get(username=username)  # Replace with your custom user model if applicable
            profile = Profile.objects.get(user=user)
            profile_serializer = ProfileSerializer(profile, many=False)
            return Response(profile_serializer.data, status=status.HTTP_200_OK)
        except (CustomUser.DoesNotExist, Profile.DoesNotExist):
            return Response({'error': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)