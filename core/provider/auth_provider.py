from datetime import datetime

import bcrypt
import jwt
from django.conf import settings

from core.exceptions import TokenExpiredError


class AuthProvider:
    def __init__(self):
        self.key = settings.SECRET_KEY
        self.expire_sec = settings.JWT_EXPIRE_TIME

    # 현재시간 가져오기
    def _get_curr_sec(self):
        return datetime.now().timestamp()

    # 비밀번호 암호화
    def hashpw(self, password: str):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt()).decode("utf8")

    # 로그인 비밀번호 체크
    def checkpw(self, password: str, hashed: str):
        return bcrypt.checkpw(password.encode("utf8"), hashed.encode("utf8"))

    # JWT 디코딩
    def _decode(self, token: str):
        decoded = jwt.decode(token, self.key, algorithms=["HS256"])
        if decoded["exp"] <= self._get_curr_sec():
            raise TokenExpiredError
        else:
            return decoded

    # 요청으로 부터 토큰정보 가져오기
    def get_token_from_request(self, request):
        return request.META.get("HTTP_AUTHORIZATION", None)

    # 유저 아이디 정보 및 만료 시간 정보를 포함한 JWT 생성
    def create_token(self, user_id: str, is_expired: bool = False):
        exp = 0 if is_expired else self._get_curr_sec() + self.expire_sec
        encoded_jwt = jwt.encode(
            {"id": user_id, "exp": exp},
            self.key,
            algorithm="HS256",
        )
        return encoded_jwt
