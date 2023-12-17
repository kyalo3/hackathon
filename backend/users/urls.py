from django.urls import path
from .views import register, get_user_profile, update_user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('update-user-and-profile/', update_user_profile, name='update_user_and_profile'),
    path('profile/<str:username>', get_user_profile, name='user_profile'),
    
]