from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm

class FornecedorListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de fornecedores cadastrados no sistema.

    Contexto:
    - fornecedores: Lista de objetos Fornecedor.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_list.html'
    context_object_name = 'fornecedores'
    login_url = reverse_lazy('login')

class FornecedorCreateView(LoginRequiredMixin, CreateView):
    """
    Cria um novo fornecedor.

    Contexto:
    - form: O formulário de criação de fornecedor.
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

    Contexto:
    - form: O formulário de edição do fornecedor.
    """
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedor_form.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
    login_url = reverse_lazy('login')

class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exclui um fornecedor.

    Contexto:
    - object: O objeto Fornecedor a ser excluído.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
    login_url = reverse_lazy('login')
