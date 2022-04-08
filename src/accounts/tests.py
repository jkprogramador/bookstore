from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTestCase(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='joe', email='joe@email.com', password='123')
        self.assertEqual(user.username, 'joe')
        self.assertEqual(user.email, 'joe@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username='joe', email='joe@email.com', password='123')
        self.assertEqual(user.username, 'joe')
        self.assertEqual(user.email, 'joe@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
