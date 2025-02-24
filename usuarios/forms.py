# ===========================
# 3️⃣ FORMULÁRIOS (forms.py)
# ===========================
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário para cadastro de novos usuários.
    """
    # email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """
    Formulário para que os usuários editem suas próprias informações.
    """
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ChangeUserGroupForm(forms.ModelForm):
    """
    Formulário para alterar o grupo de um usuário específico.
    """
    class Meta:
        model = User
        fields = []

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(), 
        label="Novo Grupo"
    )
