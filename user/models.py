from django.db import models

from core.models import TimeStamp


class User(TimeStamp):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "user"
