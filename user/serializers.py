from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = "user.User"
        fields = "__all__"


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = "user.User"
        fields = ("email", "password")
