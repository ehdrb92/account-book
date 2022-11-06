from typing import List

from ..serializers import HistorySerializer
from ..models import History
from user.models import User


class HistoryRepo:
    def __init__(self) -> None:
        self.history_serializer = HistorySerializer

    def create(self, user_id: int, data: dict) -> str:
        History.objects.create(
            user_id=User.objects.get(id=user_id).id,
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
        )
        return "created"

    def get_list(self, user_id: int) -> List[dict]:
        inquiry = History.objects.filter(user_id=user_id, is_delete=False)
        return self.history_serializer(inquiry, many=True).data

    def get_detail(self, history_id: int) -> dict:
        inquiry = History.objects.get(id=history_id)
        return self.history_serializer(inquiry).data

    def update(self, user_id: int, history_id: int, data: dict) -> dict:
        updated = History.objects.filter(id=history_id).update(
            user_id=User.objects.get(id=user_id),
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
            is_delete=data["is_delete"],
        )
        return self.history_serializer(data=updated).data

    def delete(self, history_id: int) -> None:
        History.objects.filter(id=history_id).update(is_delete=True)
        return {"msg": "deleted"}
