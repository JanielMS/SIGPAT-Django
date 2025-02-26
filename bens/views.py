from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Bem
from .forms import BemForm

class BemListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de todos os bens cadastrados no sistema.
    Apenas usuários autenticados podem visualizar.
    """
    model = Bem
    template_name = 'bens/bem_list.html'
    context_object_name = 'bens'
    login_url = reverse_lazy('login')

class BemCreateView(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário para criar um novo bem.
    O usuário autenticado será automaticamente atribuído ao bem.
    """
    model = Bem
    form_class = BemForm
    template_name = 'bens/bem_form.html'
    success_url = reverse_lazy('bens:bem-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o bem ao usuário logado
        return super().form_valid(form)

class BemUpdateView(LoginRequiredMixin, UpdateView):
    """
    Exibe o formulário para editar um bem existente.
    Apenas usuários autenticados podem editar.
    """
    model = Bem
    form_class = BemForm
    template_name = 'bens/bem_form.html'
    success_url = reverse_lazy('bens:bem-list')
    login_url = reverse_lazy('login')

class BemDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exclui um bem do sistema.
    Apenas usuários autenticados podem excluir.
    """
    model = Bem
    template_name = 'bens/bem_confirm_delete.html'
    success_url = reverse_lazy('bens:bem-list')
    login_url = reverse_lazy('login')
