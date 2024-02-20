from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer


####################################### VERSION 1 API 

class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class VideosAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        if self.kwargs.get("categoria_pk"):
            return self.queryset.filter(categoriaId = self.kwargs.get("categoria_pk"))
        
        categoria = self.request.query_params.get('search')

        print(categoria)
        if categoria:
            queryset = self.queryset.filter(categoriaId_id=categoria)
            if queryset:
                return queryset
                        
        return self.queryset.all()
    
class VideoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    