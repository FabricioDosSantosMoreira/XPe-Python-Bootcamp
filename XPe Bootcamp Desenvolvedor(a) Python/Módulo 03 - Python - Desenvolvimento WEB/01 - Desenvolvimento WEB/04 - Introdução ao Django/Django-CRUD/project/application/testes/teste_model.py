from application.models import User
from django.test import TestCase


class StrTest(TestCase):
    def setUp(self) -> None:
        self.user = User(nome = 'Fabrício', telefone = 5551998177655, email = 'FabFab@gmail.com')


    def test_str(self) -> None:
        self.assertEqual(str(self.user), 'Nome: Fabrício, Telefone: 5551998177655, Email: FabFab@gmail.com')
