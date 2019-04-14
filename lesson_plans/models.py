from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from urllib import parse

# Create your models here.
class Lesson(models.Model):
    """Creates a Lesson model"""

    title = models.CharField(max_length=200, verbose_name="lesson title")
    tags = models.ManyToManyField(
        "Tag", related_name="lessons", related_query_name="lesson"
    )
    book = models.CharField(max_length=200, verbose_name="book", default="")
    lesson_number = models.IntegerField(verbose_name="lesson number", default=0)
    lesson_duration = models.IntegerField(verbose_name="lesson duration (in minutes)", default=0)
    lesson_objectives = models.TextField(max_length=500, verbose_name="lesson objectives", default="")
    resources = models.TextField(max_length=500, verbose_name="resources", default="")
    content = models.TextField(max_length=500, verbose_name="content", default="")
    video_link = models.CharField(max_length=200, verbose_name="video link", default="")

    def get_embed_video_url(self):
        video_link_parsed = parse.urlparse(self.video_link)
        qsl = parse.parse_qs(video_link_parsed.query)
        video_id = qsl['v'][0]
        self.video_link = f'https://www.youtube.com/embed/{video_id}'

    def save(self, *args, **kwargs):
        if self.video_link:
            self.get_embed_video_url()
        super(Lesson, self).save(*args, **kwargs)

    class Meta:
        indexes = [models.Index(fields=["title"])]
        ordering = ["title"]
        verbose_name = "lesson"
        verbose_name_plural = "lessons"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "lesson_detail", args=[str(self.id)]
        )  # or kwargs={"pk": self.pk}

    # example url
    # from news import views
    # path('archive/', views.archive, name='news-archive')


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", args=[str(self.id)])
