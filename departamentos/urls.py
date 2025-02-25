from django.urls import path
from . import views

app_name = "departamentos"

urlpatterns = [
    path('', views.DepartamentoListView.as_view(), name='departamento-list'),
    path('criar/', views.DepartamentoCreateView.as_view(), name='departamento-create'),
    path('editar/<int:pk>/', views.DepartamentoUpdateView.as_view(), name='departamento-update'),
    path('excluir/<int:pk>/', views.DepartamentoDeleteView.as_view(), name='departamento-delete'),
]
