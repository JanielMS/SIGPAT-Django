from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm

class FornecedorListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de fornecedores cadastrados no sistema.
    Apenas usuários autenticados podem visualizar.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_list.html'
    context_object_name = 'fornecedores'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra os fornecedores para exibir apenas os associados ao usuário logado.
        """
        return Fornecedor.objects.filter(usuario=self.request.user)

class FornecedorCreateView(LoginRequiredMixin, CreateView):
    """
    Cria um novo fornecedor.
    O usuário autenticado será automaticamente atribuído ao fornecedor.
    """
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedor_form.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o fornecedor ao usuário logado
        return super().form_valid(form)

class FornecedorUpdateView(LoginRequiredMixin, UpdateView):
    """
    Edita um fornecedor existente.
    Apenas usuários autenticados podem editar.
    """
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedor_form.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra os fornecedores para que o usuário só possa editar os fornecedores que ele criou.
        """
        return Fornecedor.objects.filter(usuario=self.request.user)

class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exclui um fornecedor.
    Apenas usuários autenticados podem excluir.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra os fornecedores para que o usuário só possa excluir os fornecedores que ele criou.
        """
        return Fornecedor.objects.filter(usuario=self.request.user)
