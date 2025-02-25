from django.urls import path
from . import views

app_name = 'movimentacoes'

urlpatterns = [
    path('', views.MovimentacaoListView.as_view(), name='movimentacao-list'),
    path('criar/', views.MovimentacaoCreateView.as_view(), name='movimentacao-create'),
    path('editar/<int:pk>/', views.MovimentacaoUpdateView.as_view(), name='movimentacao-update'),
    path('excluir/<int:pk>/', views.MovimentacaoDeleteView.as_view(), name='movimentacao-delete'),
]
