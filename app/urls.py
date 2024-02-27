from django.urls import path
from app import views

urlpatterns = [
    path("", view.IndexView.as_view(), name="index"),
]
