from django.shortcuts import render
from .models import Livro

def index(request):
  livros = Livro.objects.all() 
  return render(request, 'blog/index.html', {"livros": livros})

# def livro(request):
#   livros = Livro.objects.all() 
#   return render(request, 'blog/index.html', {"livros": livros})

def resenha(request):
  return render(request, 'blog/resenha.html', {})

