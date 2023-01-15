from django.urls import path
from accounts.views import login_user, register, logout_user, profile

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
]
