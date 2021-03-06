from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from allauth.account.forms import SignupForm

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

class SignupPageTestCase(TestCase):

    def setUp(self):
        url = reverse('account_signup')
        self.res = self.client.get(url)
    
    def test_signup_status_code(self):
        self.assertEqual(200, self.res.status_code)
    
    def test_signup_template(self):
        self.assertTemplateUsed(self.res, 'account/signup.html')
    
    def test_signuppage_contains_correct_html(self):
        self.assertContains(self.res, 'Sign Up')
    
    def test_signuppage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, 'Hi there! I should not be on the page')
    
    def test_signup_form(self):
        form = self.res.context.get('form')
        self.assertIsInstance(form, SignupForm)
        self.assertContains(self.res, 'csrfmiddlewaretoken')
