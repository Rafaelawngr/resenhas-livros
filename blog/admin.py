from django.contrib import admin
from .models import Usuario, Livro, Resenha
admin.site.register(Usuario)
@admin.register(Livro)
class Livro(admin.ModelAdmin):
  list_display = ("isbn","titulo", "autor", "ano", "genero")
  
@admin.register(Resenha)
class Resenha(admin.ModelAdmin):
  list_display = ("livro","titulo")

