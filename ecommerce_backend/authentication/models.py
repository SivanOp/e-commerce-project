# authentication/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields
    custom_username = models.CharField(max_length=30, unique=True)
    custom_password = models.CharField(max_length=128)
    custom_user_groups = models.ManyToManyField(Group, related_name='custom_users', through='CustomUserGroup')
    custom_user_permissions = models.ManyToManyField(Permission, related_name='custom_users', through='CustomUserPermission')

    class Meta:
        permissions = [
            # Add custom permissions if needed
        ]

class CustomUserGroup(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class CustomUserPermission(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
