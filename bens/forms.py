from django import forms
from .models import Bem
from categorias.models import Categoria
from departamentos.models import Departamento
from fornecedores.models import Fornecedor

class BemForm(forms.ModelForm):
    """
    Formulário para criar ou editar um bem no sistema SIGPAT.
    """
    class Meta:
        model = Bem
        fields = ['nome', 'descricao', 'categoria', 'departamento', 'fornecedor', 'rfid_codigo', 'data_aquisicao', 'valor', 'status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Definindo os filtros para exibição das opções de categoria, departamento e fornecedor
        self.fields['categoria'].queryset = Categoria.objects.all()
        self.fields['departamento'].queryset = Departamento.objects.all()
        self.fields['fornecedor'].queryset = Fornecedor.objects.all()
