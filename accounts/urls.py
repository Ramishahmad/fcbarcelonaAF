from django.urls import path
from accounts.views import profile, register


urlpatterns = [
    path('register/', register,name='register_account'),
    path('profile/<int:uid>', profile,name='user_profile'),
]