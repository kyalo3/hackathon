from rest_framework import serializers
from .models import CustomUser, Profile
from rest_framework_simplejwt.tokens import RefreshToken

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

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'group', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)   
    
    def get_isAdmin(self, obj):
        return obj.is_staff 
    

class UserUpdateSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    profile = ProfileSerializer()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'group' 'password', 'profile']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token) 
        
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile      = instance.profile
        
        instance.username = validated_data.get('username', instance.username)
        instance.email    = validated_data.get('email', instance.email)   
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        
        profile.first_name = profile_data.get('first_name', profile.first_name)
        profile.last_name = profile_data.get('last_name', profile.last_name)
        profile.user_info = profile_data.get('user_info', profile.user_info)
        profile.image = profile_data.get( 'image', profile.image)
        profile.country = profile_data.get( 'country', profile.country)
        profile.save()
        
        return instance


