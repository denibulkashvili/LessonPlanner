from django.test import TestCase
from lesson_plans.models import Lesson, Tag

# Create your tests here.
class LessonTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print(
            "setUpTestData: Run once to set up non-modified data for all class methods."
        )
        Lesson.objects.create(title="Food lesson")

    def setUp(self):
        self.lesson = Lesson.objects.get(id=1)

    def test_title_label(self):
        field_label = self.lesson._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "lesson title")

    def test_title_max_length(self):
        max_length = self.lesson._meta.get_field("title").max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_title(self):
        expected_object_name = self.lesson.title
        self.assertEquals(expected_object_name, str(self.lesson))

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        self.assertEquals(self.lesson.get_absolute_url(), "/lesson/1/")

    def test_book_field(self):
        book_field_label = self.lesson._meta.get_field("book").verbose_name
        max_length = self.lesson._meta.get_field("book").max_length
        self.assertEquals(book_field_label, "book")
        self.assertEquals(max_length, 200)

    def test_lesson_number_field(self):
        field_label = self.lesson._meta.get_field("lesson_number").verbose_name
        self.assertEquals(field_label, "lesson number")

    def test_lesson_duration_field(self):
        field_label = self.lesson._meta.get_field("lesson_duration").verbose_name
        self.assertEquals(field_label, "lesson duration (in minutes)")

    def test_lesson_objectives_field(self):
        field_label = self.lesson._meta.get_field("lesson_objectives").verbose_name
        max_length = self.lesson._meta.get_field("lesson_objectives").max_length
        self.assertEquals(field_label, "lesson objectives")
        self.assertEquals(max_length, 500)

    def test_resources_field(self):
        field_label = self.lesson._meta.get_field("resources").verbose_name
        max_length = self.lesson._meta.get_field("resources").max_length
        self.assertEquals(field_label, "resources")
        self.assertEquals(max_length, 500)

    def test_content_filed(self):
        field_label = self.lesson._meta.get_field("content").verbose_name
        self.assertEquals(field_label, "content")

    def test_video_link_field(self):
        field_label = self.lesson._meta.get_field("video_link").verbose_name
        max_length = self.lesson._meta.get_field("video_link").max_length
        self.assertEquals(field_label, "video link")
        self.assertEquals(max_length, 200)


class TagTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print(
            "setUpTestData: Run once to set up non-modified data for all class methods."
        )
        Tag.objects.create(name="food")

    def setUp(self):
        self.tag = Tag.objects.get(id=1)

    def test_name_label(self):
        field_label = self.tag._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "tag name")

    def test_name_max_length(self):
        max_length = self.tag._meta.get_field("name").max_length
        self.assertEquals(max_length, 20)

    def test_object_name_is_name(self):
        expected_name = self.tag.name
        self.assertEquals(expected_name, str(self.tag))
