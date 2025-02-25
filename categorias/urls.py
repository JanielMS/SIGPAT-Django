from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
    path('', views.CategoriaListView.as_view(), name='categoria-list'),
    path('criar/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('excluir/<int:pk>/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
]
