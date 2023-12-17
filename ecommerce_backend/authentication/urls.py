# yourapp/urls.py
from django.urls import path
from .views import SignUpView, LoginView, success_signup_view


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('success-signup/', success_signup_view, name='success_signup'),
    path('login/', LoginView.as_view(), name='login'),
]

