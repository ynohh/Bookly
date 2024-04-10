from django.db import models
from django.utils import timezone


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField(null=True, blank=True)
    ISBN = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Resenhas(models.Model):
    id_resenha = models.AutoField(primary_key=True)
    ref_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    ref_livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    texto_resenha = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    avaliacao = models.IntegerField()

    def __str__(self):
        return f"Resenha de {self.ref_livro.titulo} por {self.ref_usuario.nome}"
