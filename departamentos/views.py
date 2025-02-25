from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from .forms import DepartamentoForm

class DepartamentoListView(ListView):
    """
    Exibe uma lista de todos os departamentos cadastrados no sistema.
    """
    model = Departamento
    template_name = 'departamentos/departamento_list.html'
    context_object_name = 'departamentos'
    paginate_by = 15

class DepartamentoCreateView(CreateView):
    """
    Exibe um formulário para criar um novo departamento.
    """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamentos/departamento_form.html'
    success_url = reverse_lazy('departamentos:departamento-list')

class DepartamentoUpdateView(UpdateView):
    """
    Exibe um formulário para editar um departamento existente.
    """
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamentos/departamento_form.html'
    success_url = reverse_lazy('departamentos:departamento-list')

class DepartamentoDeleteView(DeleteView):
    """
    Exibe uma página de confirmação para excluir um departamento.
    """
    model = Departamento
    template_name = 'departamentos/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamentos:departamento-list')
