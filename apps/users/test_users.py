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
    
    def test_login_user(self):
        self.client.post('/api/users/register/',{
            'name': 'Testeloginuser',
            'email': 'testlogin@email.com',
            'phone': '13999999999',
            'password': 'passwordtest'
        })
        
        response = self.client.post('/api/token/', {
            'email': 'testlogin@email.com',
            'password': 'passwordtest'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)