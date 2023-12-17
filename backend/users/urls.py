from django.urls import path
from .views import register, update_user_and_profile, get_user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('update-user-and-profile/', update_user_and_profile, name='update_user_and_profile'),
    path('profile/<str:username>', get_user_profile, name='user_profile'),
    
]