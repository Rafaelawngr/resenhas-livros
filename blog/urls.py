from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='blog/login.html', success_url='blog/biblioteca/'), name='login'),
    path('minha-conta/', views.profile, name='minha-conta'),
    path('biblioteca', views.index, name='biblioteca'),
    path('blog/<int:pk>', views.resenha, name='resenha'),
    path('blog/<int:pk>', views.post_new_review, name='nova-resenha'),
    path('resenhas', views.show_all_reviews, name='resenhas'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]