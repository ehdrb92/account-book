import unittest
import json

from django.test import Client

from .models import User


class UserTest(unittest.TestCase):
    def setUp(self) -> None:
        User.objects.create(
            name="테스트",
            email="test@test.com",
            password="test",
        )

    def tearDown(self) -> None:
        User.objects.all().delete()

    def test_user_signup_success(self):
        self.client = Client()
        data = {
            "name": "테스트",
            "email": "test@test.com",
            "password": "test",
        }
        response = self.client.post(
            "/api/signup/",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_user_signin_success(self):
        self.client = Client()
        data = {
            "email": "test@test.com",
            "password": "test",
        }
        response = self.client.get(
            "/api/signin",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
