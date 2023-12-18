# yourapp/urls.py
from django.urls import path
from .views import home_view
from .views import SignUpView, LoginView, success_signup_view


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home_view, name='home'),
    path('api/success_signup/', success_signup_view, name='success_signup'),
    path('login/', LoginView.as_view(), name='login'),
]

