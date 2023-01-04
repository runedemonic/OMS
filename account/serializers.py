from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            company=validated_data['company'],
            name=validated_data['name'],
            nickname=validated_data['nickname'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['company', 'nickname', 'name', 'password']
