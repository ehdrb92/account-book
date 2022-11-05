from django.db import models

from core.models import TimeStamp
from core.exceptions import NotFoundError
from core.provider.auth_provider import AuthProvider
from core.exceptions import (
    NotFoundError,
    NotFoundUserError,
)
from .serializers import UserSerializer, SigninSerializer


class User(TimeStamp):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "user"


class UserRepo:
    def __init__(self) -> None:
        self.auth_provider = AuthProvider()
        self.user_serializer = UserSerializer()
        self.signin_serializer = SigninSerializer()

    def create(
        self,
        name: str,
        email: str,
        password: str,
    ) -> dict:
        password = self.auth_provider.hashpw(password=password)
        created = User.objects.create(
            name=name,
            email=email,
            password=password,
        )
        return self.user_serializer(created).data

    # TODO 오류 발생 코드 (검토 필요)
    # def check_email_and_password(
    #     self,
    #     email: str,
    #     password: str,
    # ):
    #     try:
    #         a = UserSerializer(User.objects.get(email=email))
    #         serializer = UserSerializer(User.objects.get(email=email)).data
    #         if self.auth_provider.checkpw(password=password, hashed=serializer["password"]):
    #             return self.auth_provider.create_token(serializer["id"])
    #         else:
    #             raise NotFoundUserError()
    #     except User.DoesNotExist:
    #         return NotFoundError

    def check_email_and_password(
        self,
        email: str,
        password: str,
    ):
        try:
            user = User.objects.get(email=email)
            if self.auth_provider.checkpw(password=password, hashed=user.password):
                return self.auth_provider.create_token(user.id)
            else:
                raise NotFoundUserError()
        except User.DoesNotExist:
            return NotFoundError
