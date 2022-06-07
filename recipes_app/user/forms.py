from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']
