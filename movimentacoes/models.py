from django.db import models
from django.utils import timezone

class Movimentacao(models.Model):
    """
    Modelo que representa uma movimentação de um bem dentro do sistema SIGPAT.
    
    Este modelo é usado para registrar todas as mudanças relacionadas aos bens, como 
    movimentações entre departamentos, alteração de status, ou transferências para manutenção.
    
    Attributes:
        bem (Bem): O bem que está sendo movimentado.
        data_movimentacao (datetime): Data e hora da movimentação.
        tipo_movimentacao (str): Tipo de movimentação (ex: Transferência, Status Alterado, etc.).
        descricao (str): Descrição adicional sobre a movimentação.
        departamento_origem (Departamento): Departamento de origem, caso a movimentação envolva transferência entre departamentos.
        departamento_destino (Departamento): Departamento de destino, no caso de transferência.
        status_anterior (str): Status anterior do bem, antes da alteração.
        status_atual (str): Status atual do bem, após a movimentação.
    """
    TIPOS_MOVIMENTACAO = [
        ('Transferência', 'Transferência'),
        ('Alteração de Status', 'Alteração de Status'),
        ('Manutenção', 'Manutenção'),
        ('Desativação', 'Desativação'),
    ]
    
    bem = models.ForeignKey('bens.Bem', on_delete=models.CASCADE, related_name='movimentacoes', help_text="Bem que está sendo movimentado.")
    data_movimentacao = models.DateTimeField(default=timezone.now, help_text="Data e hora da movimentação.")
    tipo_movimentacao = models.CharField(max_length=50, choices=TIPOS_MOVIMENTACAO, help_text="Tipo de movimentação realizada.")
    descricao = models.TextField(blank=True, help_text="Descrição adicional sobre a movimentação.")
    departamento_origem = models.ForeignKey('departamentos.Departamento', on_delete=models.SET_NULL, null=True, blank=True, related_name='movimentacoes_origem', help_text="Departamento de origem da movimentação.")
    departamento_destino = models.ForeignKey('departamentos.Departamento', on_delete=models.SET_NULL, null=True, blank=True, related_name='movimentacoes_destino', help_text="Departamento de destino da movimentação.")
    status_anterior = models.CharField(max_length=50, blank=True, help_text="Status anterior do bem antes da movimentação.")
    status_atual = models.CharField(max_length=50, blank=True, help_text="Status atual do bem após a movimentação.")
    
    def __str__(self):
        return f"Movimentação do bem: {self.bem.nome} - {self.tipo_movimentacao} em {self.data_movimentacao.strftime('%d/%m/%Y %H:%M')}"
