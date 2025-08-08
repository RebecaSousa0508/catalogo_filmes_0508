
from django.urls import path
#from . import views 
from .views import home, login_view, cadastro, adicionar_filme, ver_filmes, editar_filme


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('cadastro/', cadastro, name='cadastro'),
    path('adicionar_filme/', adicionar_filme, name='adicionar_filme' ),
    path('ver_filmes/', ver_filmes, name='ver_filmes'),
    path('editar/<int:id>/', editar_filme, name='editar_filme'),
]
