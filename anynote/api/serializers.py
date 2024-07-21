from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Overridden create method. Ensures that debugApi user creation will work correctly.
        """
        print(validated_data)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
        )
        return user

    class Meta:
        model = User
        fields = "__all__"  # ['id', 'username', 'last_login', 'date_joined', 'password']
