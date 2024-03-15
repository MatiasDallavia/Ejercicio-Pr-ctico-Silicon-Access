from vehicles.models import Vehicle
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Vehicle
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
