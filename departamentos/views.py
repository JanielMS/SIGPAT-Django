from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from .forms import DepartamentoForm

class DepartamentoListView(LoginRequiredMixin, ListView):
    """
    Exibe uma lista de todos os departamentos cadastrados no sistema.
    Apenas usuários autenticados podem visualizar.
    """
    model = Departamento
    template_name = 'departamentos/departamento_list.html'
    context_object_name = 'departamentos'
    paginate_by = 15
    login_url = reverse_lazy('login')

class DepartamentoCreateView(LoginRequiredMixin, CreateView):
    """
    Exibe um formulário para criar um novo departamento.
    O usuário autenticado será automaticamente associado ao departamento.
    """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamentos/departamento_form.html'
    success_url = reverse_lazy('departamentos:departamento-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o departamento ao usuário logado
        return super().form_valid(form)

class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Exibe um formulário para editar um departamento existente.
    Apenas usuários autenticados podem editar.
    """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamentos/departamento_form.html'
    success_url = reverse_lazy('departamentos:departamento-list')
    login_url = reverse_lazy('login')

class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exibe uma página de confirmação para excluir um departamento.
    Apenas usuários autenticados podem excluir.
    """
    model = Departamento
    template_name = 'departamentos/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamentos:departamento-list')
    login_url = reverse_lazy('login')
