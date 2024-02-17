from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Create your models here.
class Video(Base):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.titulo
