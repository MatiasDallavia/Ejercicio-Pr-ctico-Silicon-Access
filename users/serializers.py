from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import PrivateArea


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("The username is already in use")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("The email is already in use")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class PrivateAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivateArea
        fields = ("id", "user", "allowed_vehicles_type", "city")


    def create(self, validated_data):
        print("*"*30)
        print(validated_data)
        area = PrivateArea.objects.create(**validated_data)
        return area
    
    def validate(self, attrs):
        print("ATRS: ", attrs)
        return attrs    