from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from lesson_plans.models import Lesson, Tag

class LessonPlansApp(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        """Instantiates WebDriver and populates the database on every test run"""
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        """Quits Selenium at the end of every test"""
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        """Populates the database"""
        self.animals_lesson = Lesson.objects.create(title='Animals lesson')
        self.animals_tag = Tag.objects.create(name='animals')
        self.kindergarten_tag = Tag.objects.create(name='kindergarten')
        self.animals_lesson.tags.add(self.animals_tag)
        self.animals_lesson.tags.add(self.kindergarten_tag)
        self.clothes_lesson = Lesson.objects.create(title='Clothes lesson')
        self.clothes_lesson.tags.add(self.kindergarten_tag)

    def test_user__when_click_tag_can_see_related_lessons(self):
        # visit the /lessons url
        self.selenium.get(f'{self.live_server_url}/lessons/')
        # find tags on page
        tag = self.selenium.find_element_by_partial_link_text('animals')
        # click the 1st tag
        first_tag_text = tag.text
        tag.click()
        # check that url matches /tag/{tag_name}
        self.assertEqual(f'{self.live_server_url}/tag/{first_tag_text}', self.selenium.current_url)
        # check that page containes related lessons
        titles = self.selenium.find_elements_by_tag_name('h2')
        self.assertEqual(self.animals_lesson.title, titles[0].text)
        self.assertEqual(self.clothes_lesson.title, titles[1].text)
