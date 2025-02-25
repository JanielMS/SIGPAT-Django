from django.urls import path
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.FornecedorListView.as_view(), name='fornecedor-list'),
    path('criar/', views.FornecedorCreateView.as_view(), name='fornecedor-create'),
    path('editar/<int:pk>/', views.FornecedorUpdateView.as_view(), name='fornecedor-update'),
    path('excluir/<int:pk>/', views.FornecedorDeleteView.as_view(), name='fornecedor-delete'),
]
