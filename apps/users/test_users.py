from django.test import TestCase
from rest_framework.test import APIClient

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_user_registration(self):
        response = self.client.post('/api/users/register/',{
            'name': 'testeUser',
            'email': 'email@test.com',
            'phone': '51111111111',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'testeUser')
        self.assertNotIn('password', response.data)