from django.db import models

from core.models import TimeStamp
from user.models import User


class History(TimeStamp):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField()  # 금액
    sort = models.CharField(max_length=1)  # 수입/지출 구분
    comment = models.TextField()  # 관련 메모
    is_delete = models.BooleanField(default=False)  # 삭제 여부

    class Meta:
        db_table = "history"
