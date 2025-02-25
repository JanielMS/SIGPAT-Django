from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Bem
from .forms import BemForm

class BemListView(ListView):
    """
    Exibe a lista de todos os bens cadastrados no sistema.
    """
    model = Bem
    template_name = 'bens/bem_list.html'
    context_object_name = 'bens'

class BemCreateView(CreateView):
    """
    Exibe o formulário para criar um novo bem.
    """
    model = Bem
    form_class = BemForm
    template_name = 'bens/bem_form.html'
    success_url = reverse_lazy('bens:bem-list')

class BemUpdateView(UpdateView):
    """
    Exibe o formulário para editar um bem existente.
    """
    model = Bem
    form_class = BemForm
    template_name = 'bens/bem_form.html'
    success_url = reverse_lazy('bens:bem-list')

class BemDeleteView(DeleteView):
    """
    Exclui um bem do sistema.
    """
    model = Bem
    template_name = 'bens/bem_confirm_delete.html'
    success_url = reverse_lazy('bens:bem-list')
