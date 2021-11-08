from rest_framework import serializers
# from uspl.models import *
from .models import *
from django.contrib.auth import authenticate
# User Serializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
    )
    class Meta:
        model = User
        fields = "__all__"

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8)
    new_password = serializers.CharField(min_length=8)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
