from django.urls import path
from .views import Inicio, CategoriaPostagens, CategoriaCriar, CategoriaListar, CategoriaEditar, CategoriaExcluir


app_name = 'core'
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('<int:pk>/postagens/', CategoriaPostagens.as_view(), name='categoria_postagens'),
    path('categoria/criar/', CategoriaCriar.as_view(), name='categoria_criar'),
    path('categoria/listar/', CategoriaListar.as_view(), name='categoria_listar'),
    path('categoria/editar/<int:pk>/', CategoriaEditar.as_view(), name='categoria_editar'),
    path('categoria/excluir/<int:pk>/', CategoriaExcluir.as_view(), name='categoria_excluir')
]
