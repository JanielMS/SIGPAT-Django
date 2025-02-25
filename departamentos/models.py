from django.db import models

class Departamento(models.Model):
    """
    Modelo que representa um departamento ou setor dentro da organização.
    
    Cada bem será alocado a um departamento específico, como 'TI', 'Financeiro', 'RH', etc.
    Esse modelo facilita a gestão e controle de onde cada bem está localizado dentro da organização.
    
    Attributes:
        nome (str): Nome do departamento, por exemplo, 'TI', 'Financeiro', etc.
        descricao (str): Descrição adicional sobre o departamento.
    """
    nome = models.CharField(max_length=100, unique=True, help_text="Nome do departamento, como TI, RH, etc.")
    descricao = models.TextField(blank=True, help_text="Descrição do departamento.")

    def __str__(self):
        return self.nome
