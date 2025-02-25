from django.db import models

class Fornecedor(models.Model):
    """
    Modelo que representa um fornecedor de bens dentro do sistema SIGPAT.
    
    Cada fornecedor pode fornecer diversos tipos de bens, e este modelo armazena 
    informações como o nome do fornecedor, dados de contato, endereço e outros detalhes 
    relevantes sobre o fornecedor.
    
    Attributes:
        nome (str): Nome do fornecedor.
        email (str): Endereço de e-mail do fornecedor.
        telefone (str): Número de telefone do fornecedor.
        endereco (str): Endereço do fornecedor.
        descricao (str): Descrição adicional sobre o fornecedor.
        cnpj (str): O CNPJ do fornecedor.
        ativo (boolean): Status do fornecedor
    """
    nome = models.CharField(max_length=255, unique=True, help_text="Nome do fornecedor.")
    email = models.EmailField(unique=True, help_text="E-mail do fornecedor.")
    telefone = models.CharField(max_length=15, blank=True, help_text="Número de telefone do fornecedor.")
    endereco = models.CharField(max_length=255, blank=True, help_text="Endereço do fornecedor.")
    cnpj = models.CharField(max_length=18, unique=True)
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(blank=True, help_text="Descrição adicional sobre o fornecedor.")

    def __str__(self):
        return self.nome
