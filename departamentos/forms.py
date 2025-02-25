from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    """
    Formulário para a criação e edição de um Departamento.
    """
    class Meta:
        model = Departamento
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
