# ===========================
# 4️⃣ VIEWS (views.py)
# ===========================
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import FormView, CreateView, RedirectView, UpdateView, DeleteView, ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from .forms import ChangeUserGroupForm, CustomUserCreationForm, UserUpdateForm

class IsAdminMixin(UserPassesTestMixin):
    """
    Permite acesso apenas para usuários do grupo 'Admin' ou superusuários.
    """
    def test_func(self):
        return self.request.user.groups.filter(name="Admin").exists() or self.request.user.is_superuser

class ChangeUserGroupView(LoginRequiredMixin, IsAdminMixin, FormView):
    """
    View para que o Admin altere o grupo de um usuário específico.
    """
    template_name = "usuarios/mudar_grupo_usuario.html"
    form_class = ChangeUserGroupForm

    def get_form(self):
        """
        Preenche o formulário com os dados do usuário selecionado.
        """
        form = super().get_form()
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        print(user.username)
        form.fields["group"].initial = user.groups.first()
        return form

    def get_context_data(self, **kwargs):
        """
        Passa o usuário correto para o template.
        """
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        """
        Atualiza o grupo do usuário.
        """
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        group = form.cleaned_data["group"]
        user.groups.clear()
        user.groups.add(group)
        return redirect("usuarios:lista-usuarios")

class UserProfileView(LoginRequiredMixin, UpdateView):
    """
    View para que os usuários editem seus próprios dados.
    """
    model = User
    form_class = UserUpdateForm
    template_name = "usuarios/perfil.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("usuarios:perfil")

class UserDeleteView(LoginRequiredMixin, DeleteView):
    """
    View para que os usuários possam excluir suas próprias contas.
    """
    model = User
    template_name = "usuarios/deletar_conta.html"
    success_url = reverse_lazy("usuarios:login")

    def get_object(self, queryset=None):
        return self.request.user

class UserListView(LoginRequiredMixin, IsAdminMixin, ListView):
    """
    Lista de usuários acessível apenas para Admins.
    Suporta paginação e filtragem por grupo.
    """
    model = User
    template_name = "usuarios/lista_usuarios.html"
    context_object_name = "users"
    paginate_by = 15

    def get_queryset(self):
        queryset = User.objects.exclude(is_superuser=True)
        group_filter = self.request.GET.get("group", None)

        if group_filter:
            queryset = queryset.filter(groups__name=group_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = Group.objects.all()
        return context


class UserRegisterView(CreateView):
    """
    View para cadastro de novos usuários.
    """
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("usuarios:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class UserLoginView(LoginView):
    """
    View para login de usuários.
    """
    template_name = "registration/login.html"

class UserLogoutView(RedirectView):
    """
    View para logout de usuários.
    """
    pattern_name = "usuarios:login"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)