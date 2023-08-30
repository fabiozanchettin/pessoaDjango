from django.test import TestCase, Client
from django.urls import reverse
from app1.models import Pessoa, Profissao
from app1.forms import PessoaForm, ProfissaoForm


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.profissao1 = Profissao.objects.create(descricao='fisico nuclear')
        self.profissao2 = Profissao.objects.create(descricao='matemático')

        self.pessoa1 = Pessoa.objects.create(
            nome='Fabio',
            cpf='123456789',
            data_nascimento='2000-01-01',
            profissao=self.profissao1
        )
        self.pessoa2 = Pessoa.objects.create(
            nome='Darcio',
            cpf='987654321',
            data_nascimento='1990-01-01',
            profissao=self.profissao2
        )

    def test_index_view(self):
        response = self.client.get(self.url)

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the right data
        self.assertEqual(list(response.context['pessoas']), [self.pessoa1, self.pessoa2])
        self.assertEqual(list(response.context['profissoes']), [self.profissao1, self.profissao2])

        # Check that the HTML contains the expected strings
        self.assertContains(response, 'Fabio')
        self.assertContains(response, 'Darcio')
        self.assertContains(response, 'fisico nuclear')
        self.assertContains(response, 'matemático')


class CadastrarProfissaoViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastrar_profissao')

    def test_cadastrar_profissao_view_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertIsInstance(response.context['form'], ProfissaoForm)

    def test_cadastrar_profissao_view_post_success(self):

        data = {'descricao': 'sacerdote'}

        response = self.client.post(self.url, data)

        self.assertEqual(Profissao.objects.count(), 1)
        self.assertEqual(Profissao.objects.first().descricao, 'sacerdote')

        self.assertRedirects(response, reverse('index'))

    def test_cadastrar_profissao_view_post_fail(self):

        data = {}

        response = self.client.post(self.url, data)

        self.assertEqual(Profissao.objects.count(), 0)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())


class CadastrarPessoaViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastrar_pessoa')  # Replace 'cadastrar_pessoa' with the name you've given this URL pattern in urls.py
        self.profissao = Profissao.objects.create(descricao='programador')

    def test_cadastrar_pessoa_view_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertIsInstance(response.context['form'], PessoaForm)

    def test_cadastrar_pessoa_view_post_success(self):
        # Prepare POST data
        data = {
            'nome': 'Zé',
            'cpf': '123456789',
            'data_nascimento': '2000-01-01',
            'profissao': self.profissao.id
        }

        response = self.client.post(self.url, data)

        self.assertEqual(Pessoa.objects.count(), 1)
        self.assertEqual(Pessoa.objects.first().nome, 'Zé')

        self.assertRedirects(response, reverse('index'))

    def test_cadastrar_pessoa_view_post_fail_invalid_profissao(self):

        data = {
            'nome': 'Maria',
            'cpf': '123456789',
            'data_nascimento': '2000-01-01',
            # 'profissao': None # não vou passar a profissao
        }

        response = self.client.post(self.url, data)

        self.assertEqual(Pessoa.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('erro', str(response.context['form'].errors['profissao']))
