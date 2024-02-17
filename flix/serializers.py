from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {"email": {"write_only": True}}
        model = Video
        fields = ("id", "titulo", "descricao", "url", "criacao", "ativo")
