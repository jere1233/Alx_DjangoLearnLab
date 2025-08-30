from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "bio", "profile_picture"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "profile_picture"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            profile_picture=validated_data.get("profile_picture"),
        )
        return user
