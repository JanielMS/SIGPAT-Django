from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .forms import CategoriaForm

class CategoriaListView(ListView):
    """
    Exibe a lista de categorias no sistema.
    """
    model = Categoria
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 15  # Para paginação de 15 categorias por página

class CategoriaCreateView(CreateView):
    """
    Exibe o formulário para criação de uma nova categoria.
    """
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria-list')  # Redireciona para a lista de categorias após salvar

class CategoriaUpdateView(UpdateView):
    """
    Exibe o formulário para edição de uma categoria existente.
    """
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria-list')  # Redireciona para a lista de categorias após editar

class CategoriaDeleteView(DeleteView):
    """
    Exibe a confirmação para excluir uma categoria.
    """
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categorias:categoria-list')  # Redireciona para a lista de categorias após excluir
