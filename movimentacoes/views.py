from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Movimentacao
from .forms import MovimentacaoForm

class MovimentacaoListView(ListView):
    """
    Exibe a lista de todas as movimentações realizadas no sistema.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_list.html'
    context_object_name = 'movimentacoes'

class MovimentacaoCreateView(CreateView):
    """
    Exibe o formulário para a criação de uma nova movimentação.
    """
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacoes/movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')

class MovimentacaoUpdateView(UpdateView):
    """
    Exibe o formulário para editar uma movimentação existente.
    """
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacoes/movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')

class MovimentacaoDeleteView(DeleteView):
    """
    Exclui uma movimentação do sistema.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_confirm_delete.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
