from django.contrib import admin
from .models import Usuario, Livro, Resenha, Avaliacao

admin.site.register(Usuario)
@admin.register(Livro)
class Livro(admin.ModelAdmin):
  list_display = ("isbn","titulo", "autor", "ano", "genero")
  
admin.site.register(Resenha)
admin.site.register(Avaliacao)
