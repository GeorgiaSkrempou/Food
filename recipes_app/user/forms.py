from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


# class UpdateUserForm(UserChangeForm):
#     class Meta:
#         model = Account
#         fields = '__all__'