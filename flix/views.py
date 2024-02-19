from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer

class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = CategoriaSerializer

class VideosAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer