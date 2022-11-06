import unittest
import json

from django.test import Client

from core.provider.auth_provider import AuthProvider
from .models import History
from user.models import User

auth_provider = AuthProvider()
client = Client()
auth_token = auth_provider.create_token(user_id=1)
headers = {"HTTP_AUTHORIZATION": auth_token}


class UserTest(unittest.TestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            name="테스트",
            email="test@test.com",
            password="test",
        )
        History.objects.create(
            user_id=user.id,
            amount=6000,
            sort="E",
            comment="점심 식사",
        )
        History.objects.create(
            user_id=user.id,
            amount=4000,
            sort="E",
            comment="디저트",
        )

    def tearDown(self) -> None:
        User.objects.all().delete()
        History.objects.all().delete()

    def test_history_create_success(self):
        data = {
            "amount": 1111,
            "sort": "E",
            "comment": "테스트",
        }
        response = client.post(
            "/api/history/",
            json.dumps(data),
            content_type="application/json",
            **headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_history_inquiry_list_success(self):
        response = client.get(
            "/api/history/",
            content_type="application/json",
            **headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_history_inquiry_detail_success(self):
        response = client.get(
            "/api/history/1",
            content_type="application/json",
            **headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_history_update_success(self):
        data = {
            "amount": 8000,
            "sort": "E",
            "comment": "테스트(수정)",
        }
        response = client.put(
            "/api/history/1/update",
            content_type="application/json",
            **headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_history_delete_detail_success(self):
        response = client.delete(
            "/api/history/1/delete",
            content_type="application/json",
            **headers,
        )

        self.assertEqual(response.status_code, 200)
