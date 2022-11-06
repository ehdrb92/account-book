from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from core.provider.auth_provider import AuthProvider
from .serializers import CreateSerializer
from .utils.repositories import HistoryRepo

auth_provider = AuthProvider()
history_repo = HistoryRepo()


class HistoryAPI(APIView):
    def get(self, request):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = auth_provider._decode(token=auth_token)
        user_id = decoded["id"]
        inquiry = history_repo.get_list(user_id=user_id)
        return JsonResponse({"res": inquiry, "status": status.HTTP_200_OK})

    def post(self, request):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = auth_provider._decode(token=auth_token)
        user_id = decoded["id"]
        params = request.data
        serializer = CreateSerializer(data=params)
        if serializer.is_valid():
            created = history_repo.create(user_id=user_id, data=serializer.data)
        return JsonResponse({"msg": created, "status": status.HTTP_201_CREATED})

    def put(request, history_id):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = auth_provider._decode(token=auth_token)
        user_id = decoded["id"]
        params = request.data
        serializer = CreateSerializer(data=params)
        if serializer.is_valid():
            updated = history_repo.update(user_id=user_id, history_id=history_id, data=params)
        return JsonResponse(updated, status.HTTP_200_OK)

    def delete(request, history_id):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = auth_provider._decode(token=auth_token)
        user_id = decoded["id"]
        deleted = history_repo.delete(history_id=history_id)
        return JsonResponse(deleted, status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, history_id):
    auth_token = request.META.get("HTTP_AUTHORIZATION", None)
    decoded = auth_provider._decode(token=auth_token)
    user_id = decoded["id"]
    inquiry = history_repo.get_detail(history_id=history_id)
    return JsonResponse({"res": inquiry, "status": status.HTTP_200_OK})
