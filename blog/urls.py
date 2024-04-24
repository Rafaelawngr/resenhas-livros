from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('livros', views.livro),
    path('resenha', views.resenha)
]