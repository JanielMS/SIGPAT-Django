# ===========================
# 2️⃣ SIGNALS (signals.py)
# ===========================
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    """
    Cria automaticamente os grupos de usuários ao rodar as migrações.
    """
    groups = ["Admin", "Desenvolvedor", "Usuário Comum"]
    for group in groups:
        Group.objects.get_or_create(name=group)

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    """
    Ao criar um novo usuário, ele é automaticamente adicionado ao grupo 'Usuário Comum'.
    """
    if created and not instance.is_superuser:
        user_group = Group.objects.get(name="Usuário Comum")
        instance.groups.add(user_group)

@receiver(post_migrate)
def create_default_admin(sender, **kwargs):
    """
    Cria um usuário admin padrão ao iniciar o sistema, caso ele ainda não exista.
    """
    if not User.objects.filter(username="admin").exists():
        admin_user = User.objects.create_superuser(username="admin", email="admin@sigpat.com", password="admin123")
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        admin_user.groups.add(admin_group)
        print("Usuário admin criado: admin / admin123")