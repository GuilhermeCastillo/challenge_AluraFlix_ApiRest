from django.urls import path
from .views import VideosAPIView, VideoAPIView, CategoriasAPIView

urlpatterns = [
    path("categorias/", CategoriasAPIView.as_view(), name="categorias"),
    path("categorias/<int:pk>", VideoAPIView.as_view(), name="categoria"),
    path("videos/", VideosAPIView.as_view(), name="videos"),
    path("videos/<int:pk>", VideoAPIView.as_view(), name="video"),
]
