from rest_framework import serializers
from .models import CustomUser, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'user_info', 'image', 'country']
        

class CustomUserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'group', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.group = validated_data.get('group', instance.group)
        instance.save()

        # Update profile data if provided
        if profile_data:
            profile = instance.profile
            profile.first_name = profile_data.get('first_name', profile.first_name)
            profile.last_name = profile_data.get('last_name', profile.last_name)
            profile.user_info = profile_data.get('user_info', profile.user_info)
            profile.image = profile_data.get('image', profile.image)
            profile.country = profile_data.get('country', profile.country)
            profile.save()

        return instance



