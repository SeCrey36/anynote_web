from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import NoteModel


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Overridden create method. Ensures that debugApi user creation will work correctly.

        """

        user = User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', ""),
            email=validated_data.get('email', ""),
            is_staff=validated_data.get('is_staff', False),
        )
        return user

    class Meta:
        model = User
        fields = "__all__"  # ['id', 'username', 'last_login', 'date_joined', 'password']


class NotesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.JSONField(default=dict)
    hash = serializers.CharField(max_length=200, default="")

    def create(self, validated_data):
        print(validated_data)
        note = NoteModel.objects.create(
            user=validated_data.get("user"),
            content=validated_data.get("content", {}),
            hash=validated_data.get("hash", ""),
        )
        return note

    class Meta:
        model = NoteModel
        fields = ["id", "content", "hash", "user"]  # "__all__"  #
