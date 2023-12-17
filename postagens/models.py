from django.db import models
from core.models import Categoria


class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    desc = models.TextField()
    arquivo = models.FileField(upload_to='arquivos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='postagens')

    def __str__(self):
        return self.titulo
