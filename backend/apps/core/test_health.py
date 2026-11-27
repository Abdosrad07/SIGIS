from django.test import TestCase
from django.urls import reverse


class HealthEndpointTests(TestCase):
    def test_health_is_public_and_healthy(self):
        response = self.client.get(reverse('api-health'))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload['success'])
        self.assertEqual(payload['data']['status'], 'healthy')
