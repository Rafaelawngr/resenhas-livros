from django import forms
from .models import Usuario, Resenha

class CreateUser(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ("usuario", "email", "senha")

class CreateReview(forms.ModelForm):
    NOTA_VALUES = [(i, str(i)) for i in range(1, 6)]
    nota = forms.ChoiceField(choices=NOTA_VALUES, label='Nota')
    class Meta:
        model = Resenha
        fields = ("titulo", "texto", "nota")