from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import SigninSerializer, UserSerializer
from .utils.repositories import UserRepo
from core.provider.auth_provider import AuthProvider

user_repo = UserRepo()
auth_provider = AuthProvider()


@api_view(["POST"])
def signup(request):
    params = request.data
    serializer = UserSerializer(data=params)
    serializer.is_valid()
    user_repo.create(**serializer.data)
    return JsonResponse({"msg": "user_created", "status": status.HTTP_201_CREATED})


@api_view(["GET"])
def signin(request):
    params = request.data
    serializer = SigninSerializer(data=params)
    serializer.is_valid()
    auth_token = user_repo.check_email_and_password(**serializer.data)
    return JsonResponse({"auth_token": auth_token, "status": status.HTTP_200_OK})
