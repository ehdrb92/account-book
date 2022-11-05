from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = "user.User"
        fields = "__all__"


class SigninSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=255)
