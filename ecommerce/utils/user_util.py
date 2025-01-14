from rest_framework import serializers
from ecommerce.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, min_length=3)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True, allow_null=False)
    phone = serializers.CharField(required=True, allow_null=False)
    address = serializers.CharField(required=True, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'address', 'created_at', 'updated_at']

    # # Custom validation
    # def validate_username(self, value):
    #     if ' ' in value:
    #         raise serializers.ValidationError("Username cannot contain spaces.")
    #     return value