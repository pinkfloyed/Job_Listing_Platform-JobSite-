from core.models import User, UserProfile
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

    def validate_password(self, value):
        """Validate the password"""
        # Check length of password
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long"
            )
        # Check password match with confirm password
        if value != self.initial_data.get("confirm_password"):
            raise serializers.ValidationError(
                "Password and confirm password don't match"
            )
        return value

    def create(self, validated_data):
        """Create a new user"""
        # Remove confirm_password from validated_data
        validated_data.pop("confirm_password", None)

        return super().create(validated_data)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data