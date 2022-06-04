from django.contrib import messages
from django.contrib.auth.views import (PasswordResetView, PasswordResetCompleteView, PasswordChangeView,
                                       PasswordResetConfirmView, PasswordChangeDoneView, LoginView, LogoutView,
                                       TemplateView)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegisterForm, UpdateAvatarForm
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
    # form_class = UserProfileEditForm
    success_url = reverse_lazy('user:profile')
    fields = ['username']
    success_message = "Profile updated"
    # template_name_suffix = '_update_form'


def avatar(request):
    if request.method == "POST":
        avatar_form = UpdateAvatarForm(request.POST, request.FILES, instance=request.user.avatar)

        if avatar_form.is_valid():
            avatar_form.save()
            messages.success(request, "Profile image updated successfully")
            return HttpResponseRedirect(reverse('user:profile'))

    else:
        avatar_form = UpdateAvatarForm(instance=request.user.avatar)

    return render(request, 'user/change_avatar.html', context={'avatar_form': avatar_form})


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
