from django.test import Client, TestCase


class TestView(TestCase):
    def test(self):
        client = Client()
        response = client.get('/admin/')
        self.assertEqual(response.status_code, 302)
