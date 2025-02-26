# categorias/tests.py
from django.test import TestCase
from categorias.models import Categoria

class CategoriaModelTest(TestCase):

    def setUp(self):
        """
        Configuração de dados para os testes.
        """
        self.categoria = Categoria.objects.create(nome="Tecnologia", descricao="Categoria de tecnologia")

    def test_categoria_str(self):
        """
        Testa o método __str__ do modelo Categoria.
        """
        self.assertEqual(str(self.categoria), "Tecnologia")

    def test_categoria_creation(self):
        """
        Testa a criação de uma categoria.
        """
        categoria = Categoria.objects.create(nome="Financeiro", descricao="Categoria de finanças")
        self.assertEqual(categoria.nome, "Financeiro")
        self.assertEqual(categoria.descricao, "Categoria de finanças")
        self.assertEqual(Categoria.objects.count(), 2)  # Confirma que a categoria foi salva


from django.urls import reverse

class CategoriaViewTest(TestCase):

    def setUp(self):
        """
        Cria uma categoria para ser usada nos testes.
        """
        self.categoria = Categoria.objects.create(nome="Tecnologia", descricao="Categoria de tecnologia")
        self.url = reverse('categorias:lista')  # URL da view de listagem de categorias

    def test_categoria_list_view(self):
        """
        Testa a view de listagem de categorias.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tecnologia")  # Verifica se o nome da categoria aparece
        self.assertTemplateUsed(response, 'categorias/categoria_list.html')  # Verifica se o template correto é usado

    def test_categoria_list_view_no_categories(self):
        """
        Testa a view de listagem de categorias quando não há categorias.
        """
        Categoria.objects.all().delete()  # Remove todas as categorias
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma categoria encontrada.")  # Verifica a mensagem caso não haja categorias

class CategoriaCreateViewTest(TestCase):

    def setUp(self):
        """
        Configura dados de teste.
        """
        self.url = reverse('categorias:criar')  # URL da view de criação de categorias

    def test_categoria_create_view_get(self):
        """
        Testa a exibição da página de criação de categoria.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categorias/categoria_form.html')  # Verifica se o template correto é usado

    def test_categoria_create_view_post(self):
        """
        Testa a criação de uma nova categoria.
        """
        data = {'nome': 'Saúde', 'descricao': 'Categoria de saúde'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação com sucesso
        self.assertRedirects(response, reverse('categorias:lista'))  # Redireciona para a lista de categorias
        self.assertEqual(Categoria.objects.count(), 1)  # Confirma que a categoria foi criada
        self.assertEqual(Categoria.objects.first().nome, 'Saúde')


from django.contrib.auth.models import User

class CategoriaPermissionsTest(TestCase):

    def setUp(self):
        """
        Cria um usuário admin e uma categoria para os testes.
        """
        self.user_admin = User.objects.create_user(username='admin', password='admin123', is_staff=True)
        self.user_normal = User.objects.create_user(username='user', password='user123', is_staff=False)
        self.url_create = reverse('categorias:criar')

    def test_create_category_admin(self):
        """
        Testa a criação de categoria por um usuário admin.
        """
        self.client.login(username='admin', password='admin123')
        data = {'nome': 'Admin Categoria', 'descricao': 'Categoria para admins'}
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertEqual(Categoria.objects.count(), 1)

    def test_create_category_normal_user(self):
        """
        Testa que um usuário normal não pode criar categorias.
        """
        self.client.login(username='user', password='user123')
        data = {'nome': 'Normal Categoria', 'descricao': 'Categoria para usuários normais'}
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 403)  # Permissão negada
        self.assertEqual(Categoria.objects.count(), 0)
