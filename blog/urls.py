from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/<int:pk>', views.resenha, name='resenha')
]