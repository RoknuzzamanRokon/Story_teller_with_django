from django.test import TestCase
from .models import Story

# Create your tests here.
class SimpleTests(TestCase):
    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)


class StoryModelTest(TestCase):
    def setUp(self):
        Story.objects.create(story_name='just a test')

    def test_text_content(self):
        story=Story.objects.get(id=1)
        expected_object_name = f'{story.story_name}'
        self.assertEqual(expected_object_name, 'just a test')