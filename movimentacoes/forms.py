from django import forms
from .models import Movimentacao
from departamentos.models import Departamento
from bens.models import Bem

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['bem', 'data_movimentacao', 'tipo_movimentacao', 'descricao', 'departamento_origem', 'departamento_destino', 'status_anterior', 'status_atual']
        widgets = {
            'data_movimentacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtro de departamentos para exibir apenas departamentos ativos (ou conforme a lógica do sistema)
        self.fields['departamento_origem'].queryset = Departamento.objects.all()
        self.fields['departamento_destino'].queryset = Departamento.objects.all()
        self.fields['bem'].queryset = Bem.objects.all()
