
from django.urls import path
#from . import views 
from .views import home, meus_filmes

urlpatterns = [
    path('', home, name='home'),
    path('meus_filmes', meus_filmes, name='meus_filmes'), 
    
]
