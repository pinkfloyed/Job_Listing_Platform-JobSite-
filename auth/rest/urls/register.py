# from auth.rest.views.register import (ForgotPasswordView, ResetPasswordView,
#                                     UserRegisterView)
# from django.urls import include, path

# urlpatterns = [
#     path("", UserRegisterView.as_view(), name="user-register"),
#     path("", ForgotPasswordView.as_view(), name="forgot-password"),
#     path("", ResetPasswordView.as_view(), name="reset-password"),
# ]

from auth.rest.views.register import (ForgotPasswordView, ResetPasswordView,
                                    UserRegisterView)
from django.urls import path

urlpatterns = [
    path("", UserRegisterView.as_view(), name="user-register"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]

