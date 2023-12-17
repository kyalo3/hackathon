from rest_framework import serializers
from .models import CustomUser, Profile
from rest_framework_simplejwt.tokens import RefreshToken

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'user_info', 'image', 'country']
        

class CustomUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    group = serializers.CharField(source='user.group')
    password = serializers.CharField(source='user.password', write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    user_info = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    country = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'group', 'password', 'first_name', 'last_name', 'user_info', 'image', 'country']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_data = {
            'username': validated_data.pop('user.username'),
            'email': validated_data.pop('user.email'),
            'group': validated_data.pop('user.group'),
            'password': validated_data.pop('user.password'),
        }

        user = CustomUser.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        instance.user.username = user_data.get('username', instance.user.username)
        instance.user.email = user_data.get('email', instance.user.email)
        instance.user.group = user_data.get('group', instance.user.group)
        instance.user.save()

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.user_info = validated_data.get('user_info', instance.user_info)
        instance.image = validated_data.get('image', instance.image)
        instance.country = validated_data.get('country', instance.country)
        instance.save()

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
        fields = ['username', 'email', 'group', 'password', 'profile', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.group = validated_data.get('group', instance.group)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        profile.first_name = profile_data.get('first_name', profile.first_name)
        profile.last_name = profile_data.get('last_name', profile.last_name)
        profile.user_info = profile_data.get('user_info', profile.user_info)
        profile.image = profile_data.get('image', profile.image)
        profile.country = profile_data.get('country', profile.country)
        profile.save()

        return instance
