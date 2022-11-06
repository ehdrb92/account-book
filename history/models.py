from typing import List

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


class HistoryRepo:
    def create(self, user_id: int, data: dict) -> dict:
        created = History.objects.create(
            user_id=User.objects.get(id=user_id).id,
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
        )
        return CreateInquirySerializer(data=created).data

    def get_list(self, user_id: int) -> List[dict]:
        inquiry = History.objects.filter(user_id=user_id, is_delete=False)
        return CreateInquirySerializer(data=inquiry).data

    def get_detail(self, history_id: int) -> dict:
        inquiry = History.objects.get(id=history_id)
        return CreateInquirySerializer(data=inquiry).data

    def update(self, user_id: int, history_id: int, data: dict) -> dict:
        updated = History.objects.filter(id=history_id).update(
            user_id=User.objects.get(id=user_id),
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
            is_delete=data["is_delete"],
        )
        return CreateInquirySerializer(data=updated).data

    def delete(self, history_id: int) -> None:
        History.objects.filter(id=history_id).update(is_delete=True)
        return {"msg": "deleted"}
