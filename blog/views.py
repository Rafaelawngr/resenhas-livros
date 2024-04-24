from django.shortcuts import render, get_object_or_404
from .models import Livro

def index(request):
  livros = Livro.objects.all() 
  return render(request, 'blog/index.html', {"livros": livros})

def resenha(request, pk):
  livro = get_object_or_404(Livro, pk=pk)
  return render(request, 'blog/resenha.html', {"livro": livro})

