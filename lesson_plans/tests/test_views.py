from django.test import TestCase
from django.urls import reverse

from lesson_plans import views
from lesson_plans.models import Lesson, Tag

# Create your tests here.
class IndexPageTests(TestCase):
    """Tests index page"""
    def setUp(self):
        self.lesson = Lesson.objects.create(title="Classroom Objects")

    def test_index_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_index_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<h1>Lesson Planner</h1>")

    def test_index_page_displays_correct_lesson_count(self):
        response = self.client.get("/")
        lesson_count = response.context["lesson_count"]
        self.assertEqual(lesson_count, 1)

class LessonListPageTests(TestCase):
    """Test LessonList page"""

    def test_lesson_list_template(self):
        response = self.client.get("/lessons/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lesson_list.html")

class LessonDetailPageTests(TestCase):
    """Test LessonDetail page"""

    def setUp(self):
        self.lesson = Lesson.objects.create(title="Countries Lesson")

    def test_lesson_detail_page_template(self):
        response = self.client.get(f"/lesson/{self.lesson.id}/")
        self.assertEqual(response.status_code, 200)

class TagListPageTests(TestCase):
    """Test TagList page"""

    def setUp(self):
        self.tag = Tag.objects.create(name="animals")

    def test_tag_list_template(self):
        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tag_list.html")

class TagDetailPageTests(TestCase):
    """Test TagDetail page"""
    def setUp(self):
        self.tag = Tag.objects.create(name="cat")

    def test_tag_detail_page_status_code(self):
        response = self.client.get("/tag/cat/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tag_detail.html")
