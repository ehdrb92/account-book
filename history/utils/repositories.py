from typing import List

from ..serializers import HistorySerializer
from ..models import History
from user.models import User


class HistoryRepo:
    def __init__(self) -> None:
        self.history_serializer = HistorySerializer

    def create(self, user_id: int, data: dict) -> str:
        created = History.objects.create(
            user_id=User.objects.get(id=user_id).id,
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
        )
        return self.history_serializer(created).data

    def get_list(self, user_id: int) -> List[dict]:
        inquiry = History.objects.filter(user_id=user_id, is_delete=False)
        return self.history_serializer(inquiry, many=True).data

    def get_detail(self, history_id: int) -> dict:
        inquiry = History.objects.get(id=history_id)
        return self.history_serializer(inquiry).data

    def update(self, history_id: int, data: dict) -> dict:
        History.objects.filter(id=history_id).update(
            amount=data["amount"],
            sort=data["sort"],
            comment=data["comment"],
        )
        updated = History.objects.get(id=history_id)
        return self.history_serializer(updated).data

    def delete(self, history_id: int) -> None:
        History.objects.filter(id=history_id).update(is_delete=True)
        deleted = History.objects.get(id=history_id)
        return self.history_serializer(deleted).data
