from core.exceptions import NotFoundError
from core.provider.auth_provider import AuthProvider
from core.exceptions import (
    NotFoundError,
    NotFoundUserError,
)
from ..serializers import UserSerializer, SigninSerializer
from ..models import User


class UserRepo:
    def __init__(self) -> None:
        self.auth_provider = AuthProvider()
        self.user_serializer = UserSerializer
        self.signin_serializer = SigninSerializer

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

    def check_email_and_password(
        self,
        email: str,
        password: str,
    ):
        try:
            serializer = self.user_serializer(User.objects.get(email=email)).data
            if self.auth_provider.checkpw(password=password, hashed=serializer["password"]):
                return self.auth_provider.create_token(serializer["id"])
            else:
                raise NotFoundUserError()
        except User.DoesNotExist:
            return NotFoundError
