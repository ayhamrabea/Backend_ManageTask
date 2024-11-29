from django.urls import path , include
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserLoginForm
from .views import RegesterView , edit_profile

urlpatterns = [
    path('login/',LoginView.as_view(authentication_form=UserLoginForm) , name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', edit_profile, name='profile'),
    path('singup',RegesterView.as_view(), name='singup'),
    path('',include('django.contrib.auth.urls')),
]