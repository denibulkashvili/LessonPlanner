from django.test import TestCase
from django.urls import reverse

from lesson_plans import views

# Create your tests here.
class IndexPageTests(TestCase):
    """Tests index page"""

    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
