from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (SignUpView, AccountPasswordResetView, AccountLogoutView, ProfileView,
                    AccountPasswordResetConfirmView, AccountPasswordResetDoneView, AccountPasswordResetCompleteView,
                    AccountPasswordChangeView, AccountPasswordChangeDoneView, UserUpdateView, AccountLoginView, activate_user)

app_name = "user"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),

    path("login/", AccountLoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', AccountLogoutView.as_view(), name="logout"),

    path("update_user/", UserUpdateView.as_view(), name="update_user"),

    path('profile/', ProfileView.as_view(template_name='user/profile.html'), name="profile"),

    path("password_reset/", AccountPasswordResetView.as_view(template_name='user/password_reset_form.html'),
         name="password_reset"),
    path("password_reset/done/", AccountPasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         AccountPasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("reset/done/", AccountPasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name="password_reset_complete"),

    path('password_change/', AccountPasswordChangeView.as_view(template_name='user/password_change_form.html'),
         name="password_change"),
    path('password_change/done/', AccountPasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),
         name="password_change_done"),
    path('activate_user/<uidb64>/<token>/', activate_user, name='activate_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
