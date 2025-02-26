from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria
from .forms import CategoriaForm

class CategoriaListView(LoginRequiredMixin, ListView):
    """
    Exibe a lista de categorias no sistema. Apenas usuários autenticados podem visualizar.
    """
    model = Categoria
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 15
    login_url = reverse_lazy('login')  # Redireciona para a página de login se não estiver autenticado

    def get_queryset(self):
        """
        Filtra as categorias para exibir apenas as associadas ao usuário logado.
        """
        return Categoria.objects.filter(usuario=self.request.user)


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário para criação de uma nova categoria.
    O usuário autenticado será automaticamente atribuído à categoria.
    """
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria-list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o usuário logado à categoria
        return super().form_valid(form)


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    """
    Exibe o formulário para edição de uma categoria existente. Apenas usuários autenticados podem editar.
    """
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra as categorias para que o usuário só possa editar as categorias que ele criou.
        """
        return Categoria.objects.filter(usuario=self.request.user)


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    """
    Exibe a confirmação para excluir uma categoria. Apenas usuários autenticados podem excluir.
    """
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categorias:categoria-list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """
        Filtra as categorias para que o usuário só possa apagar as categorias que ele criou.
        """
        return Categoria.objects.filter(usuario=self.request.user)

