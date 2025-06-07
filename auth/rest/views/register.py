from auth.rest.serializers.register import (ForgotPasswordSerializer,
                                            ResetPasswordSerializer,
                                            UserRegisterSerializer)
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class UserRegisterView(CreateAPIView):
    """User registration view"""

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    


class ForgotPasswordView(APIView):

    @swagger_auto_schema(
        request_body=ForgotPasswordSerializer,
        operation_description="Send a password reset email",
        responses={200: "Email sent", 400: "Validation error"}
    )
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Reset email sent"}, status=200)
        return Response(serializer.errors, status=400)

class ResetPasswordView(APIView):

    @swagger_auto_schema(
        request_body=ResetPasswordSerializer,
        operation_description="Reset the user's password using token",
        responses={200: "Password updated", 400: "Validation error"}
    )
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Password reset successful"}, status=200)
        return Response(serializer.errors, status=400)