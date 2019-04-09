from django.test import TestCase
from lesson_plans.models import Lesson, Tag

# Create your tests here.
class LessonTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Lesson.objects.create(title='Food lesson')
    
    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_title_label(self):
        lesson = Lesson.objects.get(id=1)
        field_label = lesson._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'lesson title')

    def test_title_max_length(self):
        lesson = Lesson.objects.get(id=1)
        max_length = lesson._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_title(self):
        lesson = Lesson.objects.get(id=1)
        expected_object_name = lesson.title
        self.assertEquals(expected_object_name, str(lesson))

    def test_get_absolute_url(self):
        lesson = Lesson.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(lesson.get_absolute_url(), '/lesson/1/')

class TagTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Tag.objects.create(name='food')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'tag name')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_object_name_is_name(self):
        tag = Tag.objects.get(id=1)
        expected_name = tag.name
        self.assertEquals(expected_name, str(tag))