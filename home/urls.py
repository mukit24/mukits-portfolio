from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_content, name="home_content"),
]
