from django.db import models

class Categoria(models.Model):
    """
    Modelo que representa uma categoria para os bens dentro do sistema SIGPAT.
    
    Cada bem pode ser classificado em uma categoria específica, como 'Computadores', 
    'Móveis', 'Equipamentos de Escritório', etc. Esse modelo também pode ser útil 
    para a organização e relatórios de bens.
    
    Attributes:
        nome (str): Nome da categoria, por exemplo, 'Tecnologia', 'Móveis'.
        descricao (str): Descrição adicional sobre a categoria.
    """
    nome = models.CharField(max_length=100, unique=True, help_text="Nome da categoria do bem. Ex: Computadores, Móveis.")
    descricao = models.TextField(blank=True, help_text="Descrição detalhada da categoria.")

    def __str__(self):
        return self.nome
