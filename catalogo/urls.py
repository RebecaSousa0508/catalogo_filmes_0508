
from django.urls import path
#from . import views 
from .views import home, login_view, cadastro, adicionar_filme, ver_filmes


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('cadastro/', cadastro, name='cadastro'),
    path('adicionar_filme/', adicionar_filme, name='adicionar_filme' ),
    path('ver_filmes/', ver_filmes, name='ver_filmes')
     
]
