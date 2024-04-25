from django.shortcuts import render, get_object_or_404
from .models import Livro, Resenha
from .forms import CreateUser
from django.contrib.auth.decorators import login_required

def login(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'blog/login.html', context)

@login_required
def profile(request):
    return render(request, 'blog/minha-conta.html')

def index(request):
  livros = Livro.objects.all() 

  if request.method == 'GET':
        query = request.GET.get('query', '')
        filtro = request.GET.get('filters', '') 
        if filtro == 'title':
            livros = livros.filter(titulo__icontains=query)
        elif filtro == 'writer':
            livros = livros.filter(autor__icontains=query)
        elif filtro == 'genre':
            livros = livros.filter(genero__icontains=query)

  return render(request, 'blog/index.html', {"livros": livros})

def resenha(request, pk):
  livro = get_object_or_404(Livro, pk=pk)
  resenha = Resenha.objects.all()
  return render(request, 'blog/resenha.html', {"livro": livro, "resenha": resenha})

from django.shortcuts import render
from .models import Livro

