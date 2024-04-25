from django import forms
from .models import Usuario, Resenha

class CreateUser(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ("usuario", "email", "senha")

class CreateReview(forms.ModelForm):
  class Meta:
    model = Resenha
    fields = ("titulo", "livro", "texto")