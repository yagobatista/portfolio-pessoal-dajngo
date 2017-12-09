from django.db import models


# Create your models here.
class Portfolio(models.Model):
    titulo = models.CharField(max_length = 100)
    imagem = models.ImageField(upload_to='portfolio')
    link = models.URLField()
    conteudo = models.TextField()
    def __str__(self):
        return self.titulo

class Habilidade (models.Model):
    titulo = models.CharField(max_length = 100)
    nivel = models.IntegerField()
    def __str__(self):
        return self.titulo

class Caracteristica (models.Model):
    titulo = models.CharField(max_length = 100)
    nivel = models.IntegerField()
    def __str__(self):
        return self.titulo

class Gosto (models.Model):
    titulo = models.CharField(max_length = 100)
    def __str__(self):
        return self.titulo

class Recomendacao(models.Model):
    titulo = models.CharField(max_length = 100)
    conteudo = models.TextField()
    def __str__(self):
        return self.titulo
class Perfil(models.Model):
    nome = models.CharField(max_length = 100)
    cargo = models.CharField(max_length = 100)
    email = models.CharField(max_length = 300)
    telefone = models.CharField(max_length = 15)
    foto_perfil = models.ImageField(upload_to='perfil')
    mensagem = models.TextField()
    servicos = models.TextField()
    def __str__(self):
        return self.nome
