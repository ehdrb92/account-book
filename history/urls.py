from django.urls import path

from .views import HistoryAPI, get_detail

urlpatterns = [
    path("history/", HistoryAPI.as_view()),
    path("history/<int:history_id>/", get_detail),
    path("history/<int:history_id>/", HistoryAPI.as_view()),
]
