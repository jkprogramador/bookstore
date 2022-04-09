from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomePageViewTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.res = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(200, self.res.status_code)
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(HomePageView.as_view().__name__, view.func.__name__)
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.res, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, 'Homepage')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, 'Hi there! I should not be on the page')

class AboutPageViewTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.res = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(200, self.res.status_code)
    
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.res, 'about.html')
    
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(AboutPageView.as_view().__name__, view.func.__name__)
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.res, 'About Page')
    
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, 'Hi there! I should not be on the page')