from django.db import models
from django.conf import settings
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    senha = models.CharField(max_length=45)

    def __str__(self):
        return self.usuario.username 

class Livro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=45)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=45)
    ano = models.IntegerField()
    genero = models.CharField(max_length=45)
    capa = models.URLField(null=True)

    def __str__(self):
        return self.titulo 

class Resenha(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField(null=True)
    data = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

