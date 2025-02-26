# departamentos/tests.py
from django.test import TestCase
from departamentos.models import Departamento

class DepartamentoModelTest(TestCase):

    def setUp(self):
        """
        Configuração de dados para os testes.
        """
        self.departamento = Departamento.objects.create(
            nome="Departamento A",
            descricao="Descrição do Departamento A"
        )

    def test_departamento_str(self):
        """
        Testa o método __str__ do modelo Departamento.
        """
        self.assertEqual(str(self.departamento), "Departamento A")

    def test_departamento_creation(self):
        """
        Testa a criação de um departamento.
        """
        departamento = Departamento.objects.create(
            nome="Departamento B",
            descricao="Descrição do Departamento B"
        )
        self.assertEqual(departamento.nome, "Departamento B")
        self.assertEqual(departamento.descricao, "Descrição do Departamento B")
        self.assertEqual(Departamento.objects.count(), 2)  # Verifica se o departamento foi salvo

from django.urls import reverse

class DepartamentoViewTest(TestCase):

    def setUp(self):
        """
        Cria um departamento para os testes.
        """
        self.departamento = Departamento.objects.create(
            nome="Departamento A",
            descricao="Descrição do Departamento A"
        )
        self.url = reverse('departamentos:lista')  # URL da view de listagem de departamentos

    def test_departamento_list_view(self):
        """
        Testa a view de listagem de departamentos.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Departamento A")  # Verifica se o nome do departamento aparece
        self.assertTemplateUsed(response, 'departamentos/departamento_list.html')  # Verifica se o template correto é usado

    def test_departamento_list_view_no_departamentos(self):
        """
        Testa a view de listagem de departamentos quando não há departamentos.
        """
        Departamento.objects.all().delete()  # Remove todos os departamentos
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum departamento encontrado.")  # Verifica a mensagem caso não haja departamentos

class DepartamentoCreateViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste.
        """
        self.url = reverse('departamentos:criar')  # URL da view de criação de departamentos

    def test_departamento_create_view_get(self):
        """
        Testa a exibição da página de criação de departamento.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'departamentos/departamento_form.html')  # Verifica se o template correto é usado

    def test_departamento_create_view_post(self):
        """
        Testa a criação de um novo departamento.
        """
        data = {
            'nome': 'Departamento C',
            'descricao': 'Descrição do Departamento C'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação com sucesso
        self.assertRedirects(response, reverse('departamentos:lista'))  # Redireciona para a lista de departamentos
        self.assertEqual(Departamento.objects.count(), 2)  # Confirma que o departamento foi criado
        self.assertEqual(Departamento.objects.first().nome, 'Departamento C')

class DepartamentoUpdateViewTest(TestCase):

    def setUp(self):
        """
        Cria um departamento para os testes.
        """
        self.departamento = Departamento.objects.create(
            nome="Departamento A",
            descricao="Descrição do Departamento A"
        )
        self.url = reverse('departamentos:editar', args=[self.departamento.id])  # URL da view de edição de departamento

    def test_departamento_update_view_get(self):
        """
        Testa a exibição da página de edição de departamento.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'departamentos/departamento_form.html')  # Verifica se o template correto é usado

    def test_departamento_update_view_post(self):
        """
        Testa a atualização de um departamento.
        """
        data = {
            'nome': 'Departamento A Atualizado',
            'descricao': 'Descrição atualizada do Departamento A'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após atualização com sucesso
        self.assertRedirects(response, reverse('departamentos:lista'))  # Redireciona para a lista de departamentos
        departamento = Departamento.objects.get(id=self.departamento.id)
        self.assertEqual(departamento.nome, 'Departamento A Atualizado')
        self.assertEqual(departamento.descricao, 'Descrição atualizada do Departamento A')

from django.contrib.auth.models import User

class DepartamentoPermissionsTest(TestCase):

    def setUp(self):
        """
        Cria um usuário admin e um departamento para os testes.
        """
        self.user_admin = User.objects.create_user(username='admin', password='admin123', is_staff=True)
        self.user_normal = User.objects.create_user(username='user', password='user123', is_staff=False)
        self.url_create = reverse('departamentos:criar')
        self.url_edit = reverse('departamentos:editar', args=[1])  # Assumindo que o departamento ID 1 existe

    def test_create_departamento_admin(self):
        """
        Testa a criação de departamento por um usuário admin.
        """
        self.client.login(username='admin', password='admin123')
        data = {
            'nome': 'Departamento D',
            'descricao': 'Descrição do Departamento D'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertEqual(Departamento.objects.count(), 1)

    def test_create_departamento_normal_user(self):
        """
        Testa que um usuário normal não pode criar departamentos.
        """
        self.client.login(username='user', password='user123')
        data = {
            'nome': 'Departamento E',
            'descricao': 'Descrição do Departamento E'
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 403)  # Permissão negada
        self.assertEqual(Departamento.objects.count(), 0)
