from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm

class FornecedorListView(ListView):
    """
    Exibe a lista de fornecedores cadastrados no sistema.
    
    Contexto:
    - fornecedores: Lista de objetos Fornecedor.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    """
    Cria um novo fornecedor.
    
    Contexto:
    - form: O formulário de criação de fornecedor.
    """
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedor_form.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')

class FornecedorUpdateView(UpdateView):
    """
    Edita um fornecedor existente.
    
    Contexto:
    - form: O formulário de edição do fornecedor.
    """
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedores/fornecedor_form.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')

class FornecedorDeleteView(DeleteView):
    """
    Exclui um fornecedor.
    
    Contexto:
    - object: O objeto Fornecedor a ser excluído.
    """
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_confirm_delete.html'
    success_url = reverse_lazy('fornecedores:fornecedor-list')
