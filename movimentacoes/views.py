from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Movimentacao
from .forms import MovimentacaoForm

class MovimentacaoListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de todas as movimentações realizadas no sistema.

    Contexto:
    - movimentacoes: Lista de objetos Movimentacao.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_list.html'
    context_object_name = 'movimentacoes'
    login_url = reverse_lazy('login')

class MovimentacaoCreateView(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário para a criação de uma nova movimentação.

    Contexto:
    - form: O formulário de criação de movimentação.
    """
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacoes/movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa a movimentação ao usuário logado
        return super().form_valid(form)

class MovimentacaoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Exibe o formulário para editar uma movimentação existente.

    Contexto:
    - form: O formulário de edição da movimentação.
    """
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacoes/movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
    login_url = reverse_lazy('login')

class MovimentacaoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exclui uma movimentação do sistema.

    Contexto:
    - object: O objeto Movimentacao a ser excluído.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_confirm_delete.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
    login_url = reverse_lazy('login')
