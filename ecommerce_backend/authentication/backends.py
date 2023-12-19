from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password

CustomUser = get_user_model()

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, custom_username=None, custom_password=None, **kwargs):
        try:
            user = CustomUser.objects.get(Q(custom_username=custom_username))
        except CustomUser.DoesNotExist:
            return None

        if custom_password == user.custom_password:
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
