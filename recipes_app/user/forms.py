from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account, Avatar


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


class UpdateAvatarForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Avatar
        fields = ['avatar']
