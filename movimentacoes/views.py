from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Movimentacao
from .forms import MovimentacaoForm

class MovimentacaoListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de todas as movimentações realizadas no sistema.
    Apenas usuários autenticados podem visualizar.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_list.html'
    context_object_name = 'movimentacoes'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra as movimentações para exibir apenas as associadas ao usuário logado.
        """
        return Movimentacao.objects.filter(usuario=self.request.user)

class MovimentacaoCreateView(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário para a criação de uma nova movimentação.
    O usuário autenticado será automaticamente atribuído à movimentação.
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
    Apenas usuários autenticados podem editar.
    """
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacoes/movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra as movimentações para que o usuário só possa editar as movimentações que ele criou.
        """
        return Movimentacao.objects.filter(usuario=self.request.user)

class MovimentacaoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exclui uma movimentação do sistema.
    Apenas usuários autenticados podem excluir.
    """
    model = Movimentacao
    template_name = 'movimentacoes/movimentacao_confirm_delete.html'
    success_url = reverse_lazy('movimentacoes:movimentacao-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra as movimentações para que o usuário só possa excluir as movimentações que ele criou.
        """
        return Movimentacao.objects.filter(usuario=self.request.user)
