from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from todolist.models import Modality, Activity, Note

class ActivityAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.modality = Modality.objects.create(name='Corrida')
        self.activity = Activity.objects.create(modality=self.modality, day=1)

        # Obter token JWT
        response = self.client.post('/user_auth/api/token', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_activity(self):
        url = '/api/activities/'
        data = {'modality_id': self.modality.id, 'day': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 2)

    def test_get_activities(self):
        url = '/api/activities/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_activity(self):
        self.client.credentials() # Limpa as credenciais de autenticação
        url = '/api/activities/'
        data = {'modality_id': self.modality.id, 'day': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class NoteAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='testpassword2')
        self.modality = Modality.objects.create(name='Natação')
        self.activity = Activity.objects.create(modality=self.modality, day=1)

        # Obter token JWT
        response = self.client.post('/user_auth/api/token', {'username': 'testuser2', 'password': 'testpassword2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_note_for_activity(self):
        url = f'/api/activities/{self.activity.id}/notes/'
        data = {'text': 'Lembrete para a natação'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().text, 'Lembrete para a natação')

    def test_create_note_for_non_existent_activity(self):
        url = '/api/activities/999/notes/'
        data = {'text': 'Teste'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_notes_for_activity(self):
        Note.objects.create(activity=self.activity, text='Primeira nota')
        url = f'/api/activities/{self.activity.id}/notes/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)