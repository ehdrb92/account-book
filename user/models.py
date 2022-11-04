from django.db import models

from core.models import TimeStamp
from core.exceptions import NotFoundError
from .serializers import UserSerializer


class User(TimeStamp):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "user"

    def create(self, name: str, email: str, password: str) -> dict:
        created = User.objects.create(
            name=name,
            email=email,
            password=password,
        )
        return UserSerializer(created).data

    def get_by_email(self, email: str) -> dict:
        try:
            return UserSerializer(User.objects.get(email=email)).data
        except User.DoesNotExist:
            return NotFoundError
