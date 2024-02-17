from django.urls import path
from .views import VideosAPIView, VideoAPIView

urlpatterns = [
    path("videos/", VideosAPIView.as_view(), name="videos"),
    path("videos/<int:pk>", VideoAPIView.as_view(), name="video"),
]
