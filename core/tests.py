from rest_framework.test import APITestCase
from rest_framework import status

class ClientAPITestCase(APITestCase):
    
    def test_create_client(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/api/clients/', {'client_name': 'Test Client'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Add more tests as needed.