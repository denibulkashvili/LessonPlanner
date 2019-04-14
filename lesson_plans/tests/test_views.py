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
        self.assertContains(response, '<h1 class="header-title">Lesson Planner</h1>')

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
        self.lesson = Lesson.objects.create(
            title="Countries Lesson",
            book="Get Smart 5",
            lesson_number=1,
            lesson_duration=90,
            lesson_objectives="Learn names of the countries.",
            resources="Books, map, flashcards.",
            content="Learn the vocabulary. Sing the song about countries. Write the names of the ountries on the map.",
            video_link="https://www.youtube.com/watch?v=4gHbPDdGCFs",
        )
        self.tag = Tag.objects.create(name="countries")
        self.lesson.tags.add(self.tag)

    def test_lesson_detail_page_template(self):
        response = self.client.get(f"/lesson/{self.lesson.id}/")
        self.assertEqual(response.status_code, 200)

    def test_lesson_detail_page_displays_tags(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "countries")

    def test_lesson_detail_page_displays_book(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Get Smart 5")

    def test_lesson_detail_page_displays_lesson_number(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Lesson number: 1")

    def test_lesson_detail_page_displays_lesson_duration(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Lesson duration: 90 minutes.")

    def test_lesson_detail_page_displays_lesson_resources(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Resources: Books, map, flashcards.")

    def test_lesson_detail_page_displays_lesson_objectives(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Objectives: Learn names of the countries.")

    def test_lesson_detail_page_displays_lesson_content(self):
        response = self.client.get("/lesson/1/")
        self.assertContains(response, "Content: Learn the vocabulary.")

    def test_lesson_detail_page_displays_video_link(self):
        iframe_scr_tag = 'src="https://www.youtube.com/embed/4gHbPDdGCFs">'
        response = self.client.get("/lesson/1/")
        self.assertContains(response, iframe_scr_tag)


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
