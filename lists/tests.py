from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):
    """Home page test"""

    def test_uses_home_template(self):
        """test: using Home template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """test: can save post-request"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
