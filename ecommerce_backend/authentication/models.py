from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import UserManager


class CustomUser(AbstractBaseUser):
    # Add custom fields
    custom_username = models.CharField(max_length=100, unique=True)
    custom_password = models.CharField(max_length=128)
    is_active = models.BooleanField()
    USERNAME_FIELD = "custom_username"
    objects = UserManager()

    class Meta:
        constraints = [UniqueConstraint(fields=["custom_username"], name="user_username_unq")]

# class CustomUserGroup(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
