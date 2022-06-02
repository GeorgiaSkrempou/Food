from django.contrib import messages
from django.contrib.auth.views import (PasswordResetView, PasswordResetCompleteView, PasswordChangeView,
                                       PasswordResetConfirmView, PasswordChangeDoneView, LoginView, LogoutView,
                                       TemplateView)
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegisterForm
from .models import Account


# Create your views here.

class AccountLoginView(LoginView):
    pass


class AccountLogoutView(LogoutView):
    next_page = reverse_lazy("recipes:home")


class SignUpView(CreateView):
    form_class = UserRegisterForm

    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Account
    success_url = reverse_lazy('user:profile')
    fields = ['username', 'profile_image', 'hide_email']
    success_message = "Profile updated."


class ProfileView(LoginRequiredMixin, TemplateView):
    pass


class AccountPasswordResetView(PasswordResetView):
    email_template_name = "user/password_reset_email.html"
    success_url = reverse_lazy("user:password_reset_done")


class AccountPasswordResetDoneView(TemplateView):
    pass


class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    pass


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("user:password_reset_complete")


class AccountPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("user:password_change_done")


class AccountPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    pass



