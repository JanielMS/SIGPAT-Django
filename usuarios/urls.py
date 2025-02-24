# ===========================
# 5️⃣ URLS (urls.py)
# ===========================
from django.urls import path
from .views import *
app_name = "usuarios"

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path("cadastro/", UserRegisterView.as_view(), name="registrar"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    path('perfil', UserProfileView.as_view(), name='perfil'),
    path('excluir-conta', UserDeleteView.as_view(), name='deletar-conta'),
    path('listar-usuarios', UserListView.as_view(), name='lista-usuarios'),
    path("alterar-permissoes/<int:pk>", ChangeUserGroupView.as_view(), name="mudar-grupo-usuario"),
]
