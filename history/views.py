from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from core.provider.auth_provider import AuthProvider
from .serializers import HistorySerializer
from .models import History


class HistoryAPI(APIView):
    def get(request):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = AuthProvider._decode(token=auth_token)
        user_id = decoded["id"]
        inquiry = History.get_list(user_id=user_id)
        return JsonResponse(inquiry, status.HTTP_200_OK)

    def post(request):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = AuthProvider._decode(token=auth_token)
        user_id = decoded["id"]
        params = request.data
        serializer = HistorySerializer(data=params)
        if serializer.is_valid():
            created = History.create(user_id=user_id, data=params.data)
        return JsonResponse(created, status.HTTP_201_CREATED)

    def put(request, history_id):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = AuthProvider._decode(token=auth_token)
        user_id = decoded["id"]
        params = request.data
        serializer = HistorySerializer(data=params)
        if serializer.is_valid():
            updated = History.update(user_id=user_id, history_id=history_id, data=params)
        return JsonResponse(updated, status.HTTP_200_OK)

    def delete(request, history_id):
        auth_token = request.META.get("HTTP_AUTHORIZATION", None)
        decoded = AuthProvider._decode(token=auth_token)
        user_id = decoded["id"]
        deleted = History.delete(history_id=history_id)
        return JsonResponse(deleted, status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, history_id):
    auth_token = request.META.get("HTTP_AUTHORIZATION", None)
    decoded = AuthProvider._decode(token=auth_token)
    user_id = decoded["id"]
    inquiry = History.get_detail(history_id=history_id)
    return JsonResponse(inquiry, status.HTTP_200_OK)
