from django.urls import path

from .views import signin, signup

urlpatterns = [
    path("signup/", signup),
    path("signin/", signin),
]
