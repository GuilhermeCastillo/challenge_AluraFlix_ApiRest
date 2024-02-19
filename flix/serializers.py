from rest_framework import serializers
from .models import Video, Categoria


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ("id", "titulo", "descricao", "url", "categoriaId" ,"criacao", "ativo")

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "titulo", "cor")