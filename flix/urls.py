from django.urls import path
from .views import VideoAPIView

urlpatterns = [
    path("videos/", VideoAPIView.as_view(), name="videos"),
]
