from django.db import models

from categorias.models import Categoria
from departamentos.models import Departamento
from fornecedores.models import Fornecedor

class Bem(models.Model):
    """
    Modelo que representa um bem no sistema SIGPAT.
    
    Este modelo pode ser utilizado para registrar bens físicos e incluir informações 
    como nome, categoria, descrição, valor, código RFID, departamento, e o fornecedor 
    de onde o bem foi adquirido.
    
    Attributes:
        nome (str): Nome do bem.
        descricao (str): Descrição detalhada do bem.
        categoria (Categoria): Categoria do bem (relacionado com o modelo Categoria).
        departamento (Departamento): Departamento onde o bem está alocado.
        fornecedor (Fornecedor): Fornecedor de onde o bem foi adquirido.
        rfid_codigo (str): Código RFID do bem para rastreamento.
        data_aquisicao (date): Data em que o bem foi adquirido.
        valor (Decimal): Valor do bem.
        status (str): Status do bem (ativo, inativo, etc.).
    """
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        ('Em manutenção', 'Em manutenção'),
    ]
    
    nome = models.CharField(max_length=255, help_text="Nome do bem.")
    descricao = models.TextField(blank=True, help_text="Descrição do bem.")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='bens', help_text="Categoria do bem.")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='bens', help_text="Departamento onde o bem está alocado.")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='bens', help_text="Fornecedor do bem.")
    rfid_codigo = models.CharField(max_length=100, blank=True, help_text="Código RFID do bem, se aplicável.")
    data_aquisicao = models.DateField(help_text="Data de aquisição do bem.")
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor do bem.")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ativo', help_text="Status do bem.")
    
    def __str__(self):
        return self.nome
