# ===========================
# 1️⃣ MODELOS (models.py)
# ===========================
from django.contrib.auth.models import User, Group
from django.db import models

class UserProfile(models.Model):
    """
    Modelo para armazenar o grupo associado a um usuário.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.grupo.name if self.grupo else 'Sem grupo'}"