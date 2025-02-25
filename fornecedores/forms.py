from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    """
    Formulário para criação e edição de fornecedores.
    """
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco', 'descricao']
        widgets = {
            'cnpj': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
