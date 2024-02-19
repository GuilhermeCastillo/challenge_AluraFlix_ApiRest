from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.titulo

class Video(Base):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1, blank=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.titulo

