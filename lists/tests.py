from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):
    """Home page test"""

    def test_home_page_returns_correct_html(self):
        """test: Home page returns right html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
