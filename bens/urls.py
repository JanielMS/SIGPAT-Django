from django.urls import path
from . import views

app_name = 'bens'

urlpatterns = [
    path('', views.BemListView.as_view(), name='bem-list'),
    path('criar/', views.BemCreateView.as_view(), name='bem-create'),
    path('editar/<int:pk>/', views.BemUpdateView.as_view(), name='bem-update'),
    path('excluir/<int:pk>/', views.BemDeleteView.as_view(), name='bem-delete'),
]
