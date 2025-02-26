# movimentacoes/tests.py
from django.test import TestCase
from movimentacoes.models import Movimentacao
from bens.models import Bem
from django.contrib.auth.models import User
from datetime import datetime

class MovimentacaoModelTest(TestCase):

    def setUp(self):
        """
        Configuração de dados para os testes.
        """
        self.user = User.objects.create_user(username="usuario_teste", password="senha_teste")
        self.bem = Bem.objects.create(nome="Bem A", valor=100, status="ativo")
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            usuario=self.user,
            tipo="entrada",
            quantidade=10,
            descricao="Entrada de estoque"
        )

    def test_movimentacao_str(self):
        """
        Testa o método __str__ do modelo Movimentacao.
        """
        self.assertEqual(str(self.movimentacao), "entrada - Bem A (10)")

    def test_movimentacao_creation(self):
        """
        Testa a criação de uma movimentação.
        """
        movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            usuario=self.user,
            tipo="saída",
            quantidade=5,
            descricao="Saída de estoque"
        )
        self.assertEqual(movimentacao.bem, self.bem)
        self.assertEqual(movimentacao.usuario, self.user)
        self.assertEqual(movimentacao.tipo, "saída")
        self.assertEqual(movimentacao.quantidade, 5)
        self.assertEqual(movimentacao.descricao, "Saída de estoque")

from django.urls import reverse

class MovimentacaoListViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste para as movimentações.
        """
        self.user = User.objects.create_user(username="usuario_teste", password="senha_teste")
        self.client.login(username="usuario_teste", password="senha_teste")
        self.bem = Bem.objects.create(nome="Bem A", valor=100, status="ativo")
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            usuario=self.user,
            tipo="entrada",
            quantidade=10,
            descricao="Entrada de estoque"
        )
        self.url = reverse('movimentacoes:lista')  # URL da view de listagem de movimentações

    def test_movimentacao_list_view(self):
        """
        Testa a view de listagem de movimentações.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bem A")
        self.assertContains(response, "Entrada de estoque")
        self.assertTemplateUsed(response, 'movimentacoes/movimentacao_list.html')
        
    def test_movimentacao_list_view_no_movimentacoes(self):
        """
        Testa a view de listagem de movimentações quando não há movimentações.
        """
        Movimentacao.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma movimentação encontrada.")

class MovimentacaoCreateViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste para criação de movimentação.
        """
        self.user = User.objects.create_user(username="usuario_teste", password="senha_teste")
        self.client.login(username="usuario_teste", password="senha_teste")
        self.bem = Bem.objects.create(nome="Bem A", valor=100, status="ativo")
        self.url = reverse('movimentacoes:criar')  # URL da view de criação de movimentações

    def test_movimentacao_create_view_get(self):
        """
        Testa a exibição da página de criação de movimentação.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movimentacoes/movimentacao_form.html')

    def test_movimentacao_create_view_post(self):
        """
        Testa a criação de uma nova movimentação.
        """
        data = {
            'bem': self.bem.id,
            'usuario': self.user.id,
            'tipo': 'entrada',
            'quantidade': 5,
            'descricao': 'Entrada de estoque'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação com sucesso
        self.assertRedirects(response, reverse('movimentacoes:lista'))  # Redireciona para a lista de movimentações
        self.assertEqual(Movimentacao.objects.count(), 2)  # Confirma que a movimentação foi criada

class MovimentacaoDetailViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste para visualização dos detalhes de movimentação.
        """
        self.user = User.objects.create_user(username="usuario_teste", password="senha_teste")
        self.client.login(username="usuario_teste", password="senha_teste")
        self.bem = Bem.objects.create(nome="Bem A", valor=100, status="ativo")
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            usuario=self.user,
            tipo="entrada",
            quantidade=10,
            descricao="Entrada de estoque"
        )
        self.url = reverse('movimentacoes:detalhes', args=[self.movimentacao.id])  # URL da view de detalhes

    def test_movimentacao_detail_view(self):
        """
        Testa a exibição da página de detalhes da movimentação.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bem A")
        self.assertContains(response, "Entrada de estoque")
        self.assertContains(response, "10")  # Verifica a quantidade
        self.assertTemplateUsed(response, 'movimentacoes/movimentacao_detail.html')

class MovimentacaoPermissionsTest(TestCase):

    def setUp(self):
        """
        Cria usuários e movimentações para os testes de permissões.
        """
        self.user_admin = User.objects.create_user(username="admin", password="admin123", is_staff=True)
        self.user_normal = User.objects.create_user(username="user", password="user123", is_staff=False)
        self.bem = Bem.objects.create(nome="Bem A", valor=100, status="ativo")
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            usuario=self.user_admin,
            tipo="entrada",
            quantidade=10,
            descricao="Entrada de estoque"
        )
        self.url_create = reverse('movimentacoes:criar')  # URL da view de criação de movimentações
        self.url_edit = reverse('movimentacoes:editar', args=[self.movimentacao.id])  # URL da view de edição

    def test_create_movimentacao_admin(self):
        """
        Testa que um usuário admin pode criar movimentações.
        """
        self.client.login(username="admin", password="admin123")
        data = {
            'bem': self.bem.id,
            'usuario': self.user_admin.id,
            'tipo': 'entrada',
            'quantidade': 5,
            'descricao': 'Entrada de estoque'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertEqual(Movimentacao.objects.count(), 2)

    def test_create_movimentacao_normal_user(self):
        """
        Testa que um usuário normal não pode criar movimentações.
        """
        self.client.login(username="user", password="user123")
        data = {
            'bem': self.bem.id,
            'usuario': self.user_normal.id,
            'tipo': 'entrada',
            'quantidade': 5,
            'descricao': 'Entrada de estoque'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 403)  # Permissão negada
        self.assertEqual(Movimentacao.objects.count(), 1)
