from django.test import TestCase
from model_bakery import baker
from pprint import pprint

class ProfissaoTestCase(TestCase):

    def setUp(self):
        self.profissao = baker.make('Profissao')
        pprint(self.profissao.__dict__)

    def test_str(self):
        self.assertEquals(str(self.profissao), self.profissao.descricao)

class PessoaTestCase(TestCase):

    def setUp(self):
        self.pessoa = baker.make('Pessoa')
        pprint(self.pessoa.__dict__)

    def test_str(self):
        self.assertEquals(str(self.pessoa), self.pessoa.nome)
