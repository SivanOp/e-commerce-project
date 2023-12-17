from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("custom_username", "custom_password")
        exclude = ['']

