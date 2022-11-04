from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser  # TODO 해당 기능에 대해 알아볼 것

from .serializers import UserSerializer, SigninSerializer
from .models import User
from utils.auth_provider import AuthProvider


@api_view(["POST"])
def signup(request):
    params = request.data
    serializer = UserSerializer(data=params)

    if serializer.is_valid():
        created = User.create(**params.data)
        return JsonResponse(created, status.HTTP_201_CREATED)

    return JsonResponse(status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def signin(request):
    params = request.data
    serializer = SigninSerializer(data=params)

    if serializer.is_valid():
        auth_token = AuthProvider.login(serializer["email"], serializer["password"])

    return JsonResponse(auth_token, status.HTTP_200_OK)
