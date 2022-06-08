from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordChangeDoneView,
    LoginView,
    LogoutView,
    TemplateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView

from .forms import UserRegisterForm
from .models import Account
from .utils import generate_token


# Create your views here.


class AccountLoginView(LoginView):
    pass


class AccountLogoutView(LogoutView):
    next_page = reverse_lazy("recipes:home")


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # deactivate account until it is confirmed
            user.save()

            current_domain = get_current_site(request)
            email_subject = 'Activate your Foodie Account'
            email_body = render_to_string('user/registration_email_confirmation.html', {
                'user': user,
                'domain': current_domain.domain,
                'uid': urlsafe_base64_encode(str(user.pk).encode('utf-8')),
                'token': generate_token.make_token(user)
            })

            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email]
            )
            email.send()
            messages.success(request, "We sent you an activation email. Please check your inbox")

            return redirect(reverse('user:login'))

        # print(form.errors)
        return redirect(reverse('user:signup'))


def activate_user(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = Account.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Email verified, you can now log in")
        return redirect(reverse('user:login'))

    messages.warning(request, "Email verification failed")
    return redirect(reverse('user:login'))


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Account
    success_url = reverse_lazy('user:profile')
    fields = ['username', 'avatar']
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        return Account.objects.get(pk=self.request.user.pk)


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
