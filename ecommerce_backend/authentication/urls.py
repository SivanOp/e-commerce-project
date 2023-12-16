# yourapp/urls.py
from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    # Add other URL patterns as needed
]
