# fornecedores/tests.py
from django.test import TestCase
from fornecedores.models import Fornecedor

class FornecedorModelTest(TestCase):

    def setUp(self):
        """
        Configuração de dados para os testes.
        """
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            email="fornecedorA@example.com",
            telefone="1234567890",
            endereco="Rua Exemplo, 123"
        )

    def test_fornecedor_str(self):
        """
        Testa o método __str__ do modelo Fornecedor.
        """
        self.assertEqual(str(self.fornecedor), "Fornecedor A")

    def test_fornecedor_creation(self):
        """
        Testa a criação de um fornecedor.
        """
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor B",
            email="fornecedorB@example.com",
            telefone="0987654321",
            endereco="Avenida Teste, 456"
        )
        self.assertEqual(fornecedor.nome, "Fornecedor B")
        self.assertEqual(fornecedor.email, "fornecedorB@example.com")
        self.assertEqual(fornecedor.telefone, "0987654321")
        self.assertEqual(fornecedor.endereco, "Avenida Teste, 456")
        self.assertEqual(Fornecedor.objects.count(), 2)  # Verifica se o fornecedor foi salvo

from django.urls import reverse

class FornecedorViewTest(TestCase):

    def setUp(self):
        """
        Cria um fornecedor para os testes.
        """
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            email="fornecedorA@example.com",
            telefone="1234567890",
            endereco="Rua Exemplo, 123"
        )
        self.url = reverse('fornecedores:lista')  # URL da view de listagem de fornecedores

    def test_fornecedor_list_view(self):
        """
        Testa a view de listagem de fornecedores.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fornecedor A")  # Verifica se o nome do fornecedor aparece
        self.assertTemplateUsed(response, 'fornecedores/fornecedor_list.html')  # Verifica se o template correto é usado

    def test_fornecedor_list_view_no_fornecedores(self):
        """
        Testa a view de listagem de fornecedores quando não há fornecedores.
        """
        Fornecedor.objects.all().delete()  # Remove todos os fornecedores
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum fornecedor encontrado.")  # Verifica a mensagem caso não haja fornecedores

class FornecedorCreateViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste.
        """
        self.url = reverse('fornecedores:criar')  # URL da view de criação de fornecedores

    def test_fornecedor_create_view_get(self):
        """
        Testa a exibição da página de criação de fornecedor.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedores/fornecedor_form.html')  # Verifica se o template correto é usado

    def test_fornecedor_create_view_post(self):
        """
        Testa a criação de um novo fornecedor.
        """
        data = {
            'nome': 'Fornecedor C',
            'email': 'fornecedorC@example.com',
            'telefone': '1122334455',
            'endereco': 'Rua Teste, 789'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação com sucesso
        self.assertRedirects(response, reverse('fornecedores:lista'))  # Redireciona para a lista de fornecedores
        self.assertEqual(Fornecedor.objects.count(), 2)  # Confirma que o fornecedor foi criado
        self.assertEqual(Fornecedor.objects.first().nome, 'Fornecedor C')

class FornecedorUpdateViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste.
        """
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            email="fornecedorA@example.com",
            telefone="1234567890",
            endereco="Rua Exemplo, 123"
        )
        self.url = reverse('fornecedores:editar', args=[self.fornecedor.id])  # URL da view de edição de fornecedor

    def test_fornecedor_update_view_get(self):
        """
        Testa a exibição da página de edição de fornecedor.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedores/fornecedor_form.html')  # Verifica se o template correto é usado

    def test_fornecedor_update_view_post(self):
        """
        Testa a atualização de um fornecedor.
        """
        data = {
            'nome': 'Fornecedor A Atualizado',
            'email': 'fornecedorA_updated@example.com',
            'telefone': '9876543210',
            'endereco': 'Rua Atualizada, 456'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após atualização com sucesso
        self.assertRedirects(response, reverse('fornecedores:lista'))  # Redireciona para a lista de fornecedores
        fornecedor = Fornecedor.objects.get(id=self.fornecedor.id)
        self.assertEqual(fornecedor.nome, 'Fornecedor A Atualizado')
        self.assertEqual(fornecedor.email, 'fornecedorA_updated@example.com')

from django.contrib.auth.models import User

class FornecedorPermissionsTest(TestCase):

    def setUp(self):
        """
        Cria um usuário admin e um fornecedor para os testes.
        """
        self.user_admin = User.objects.create_user(username='admin', password='admin123', is_staff=True)
        self.user_normal = User.objects.create_user(username='user', password='user123', is_staff=False)
        self.url_create = reverse('fornecedores:criar')
        self.url_edit = reverse('fornecedores:editar', args=[1])  # Assumindo que o fornecedor ID 1 existe

    def test_create_fornecedor_admin(self):
        """
        Testa a criação de fornecedor por um usuário admin.
        """
        self.client.login(username='admin', password='admin123')
        data = {
            'nome': 'Fornecedor D',
            'email': 'fornecedorD@example.com',
            'telefone': '1122334455',
            'endereco': 'Avenida Admin, 100'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertEqual(Fornecedor.objects.count(), 1)

    def test_create_fornecedor_normal_user(self):
        """
        Testa que um usuário normal não pode criar fornecedores.
        """
        self.client.login(username='user', password='user123')
        data = {
            'nome': 'Fornecedor E',
            'email': 'fornecedorE@example.com',
            'telefone': '2233445566',
            'endereco': 'Avenida Normal, 200'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 403)  # Permissão negada
        self.assertEqual(Fornecedor.objects.count(), 0)
