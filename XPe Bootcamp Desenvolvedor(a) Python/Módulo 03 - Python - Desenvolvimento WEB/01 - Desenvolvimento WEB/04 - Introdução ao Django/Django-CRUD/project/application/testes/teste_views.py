from django.test import Client, TestCase
from django.urls import reverse_lazy


class ViewTest(TestCase):

    def setUp(self) -> None:
        self.dados = {
            'nome': 'teste',
            'telefone': 5551990,
            'email': 'teste@gmail.com'
        } 

        self.client = Client()
    

    def test_index(self) -> None:
        request = self.client.get(reverse_lazy('index'))

        self.assertEqual(request.status_code, 200)


    def test_criar(self) -> None:
        request = self.client.post(reverse_lazy('criar'), data=self.dados)

        self.assertEqual(request.status_code, 302)
