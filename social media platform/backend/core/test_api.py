from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from core.models import Post


class ApiTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('apiuser', password='pass')
        self.client = APIClient()

    def test_token_auth_and_create_post(self):
        # obtain token
        from rest_framework.authtoken.models import Token
        token, _ = Token.objects.get_or_create(user=self.u)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        resp = self.client.post('/api/posts/', {'content': 'hello from api'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
