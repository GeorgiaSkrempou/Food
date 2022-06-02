from django.contrib.auth.views import (PasswordResetView, PasswordResetCompleteView, PasswordChangeView,
                                       PasswordResetConfirmView, PasswordChangeDoneView, LoginView, LogoutView,
                                       TemplateView)
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


# Create your views here.

class AccountLoginView(LoginView):
    pass


class AccountLogoutView(LogoutView):
    next_page = reverse_lazy("recipes:home")


class SignUpView(CreateView):
    form_class = UserRegisterForm

    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'


class AccountPasswordResetView(PasswordResetView):
    email_template_name = "user/password_reset_email.html"
    # subject_template_name = "user/password_reset_subject.txt"
    success_url = reverse_lazy("user:password_reset_done")
    # template_name = "user/password_reset_form.html"


class AccountPasswordResetDoneView(TemplateView):
    pass


class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    pass


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("user:password_reset_complete")


class AccountPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("user:password_change_done")


class AccountPasswordChangeDoneView(PasswordChangeDoneView):
    pass
