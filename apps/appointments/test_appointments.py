from django.test import TestCase
from rest_framework.test import APIClient
from apps.users.models import User
from apps.services.models import Service

class AgendamentosTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email = 'testUserAgendamento@email.com',
            name='TestUserAgendamento',
            password='testagendamentopassword',
        )
        self.user2 = User.objects.create_user(
            email = 'testUser2@email.com',
            name = 'User2Test',
            password = 'testUser2'
        )
        self.service = Service.objects.create(
            name='servicoteste',
            price='100.00',
            description='description teste',
            duration='30'
        )
        response = self.client.post('/api/token/', {
            'email': 'testUserAgendamento@email.com',
            'password': 'testagendamentopassword',
        })
        response2 = self.client.post('/api/token/', {
            'email': 'testUser2@email.com',
            'password': 'testUser2',
        })
        self.token = response.data['access']
        self.token2 = response2.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
    def test_create_agendamento(self):
        response = self.client.post('/api/appointments/', {
            'service': self.service.id,
            'appointment_date': "2026-05-30T10:00:00"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['user'], self.user.id)
        
    def test_isolamento(self):
        response = self.client.post('/api/appointments/', {
            'service': self.service.id,
            'appointment_date': "2026-05-30T10:00:00"
        })
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token2)
        response = self.client.get('/api/appointments/')
        self.assertEqual(len(response.data), 0)