from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Livro, Resenha
from .forms import CreateUser, CreateReview
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    resenhas = Resenha.objects.filter(livro=livro)
    
    if request.method == 'POST':

        form = CreateReview(request.POST)
        if form.is_valid():
            resenha = form.save(commit=False)
            resenha.livro = livro
            usuario, _ = Usuario.objects.get_or_create(email=request.user.email)
            resenha.usuario = usuario
            resenha.save()
            return redirect('resenha', pk=pk)
    else:
        form = CreateReview()
    
    return render(request, 'blog/resenha.html', {'livro': livro, 'resenhas': resenhas, 'form': form})

def post_new_review(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if request.method == 'POST':
        form = CreateReview(request.POST)
        if form.is_valid():
            resenha = form.save(commit=False)
            usuario, _ = Usuario.objects.get_or_create(usuario=request.user)
            resenha.usuario = usuario
            resenha.data = timezone.now()
            resenha.livro = livro 
            resenha.save()
            return redirect('resenha', pk=pk)  
    else:
        form = CreateReview()
    
    resenha = Resenha.objects.filter(livro=livro) 
    return render(request, 'blog/resenha.html', {'form': form, 'livro': livro, 'resenha': resenha})

def show_all_reviews(request):
    all_resenhas = Resenha.objects.all().order_by('-data')
    return render(request, 'blog/resenhas.html', {'resenhas': all_resenhas})

