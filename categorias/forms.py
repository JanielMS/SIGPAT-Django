from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    """
    Formulário para a criação e edição de categorias.
    """
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição da categoria'}),
        }
