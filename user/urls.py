from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginUser.as_view() ,name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/', profile, name='profile'),
    # path('lo/', SendEmail, name='lo'),
    path('register/', RegisterUser.as_view(), name='register'),
]


