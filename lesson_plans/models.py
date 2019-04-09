from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Lesson(models.Model):
    """Creates a Lesson model"""
    title = models.CharField(
        max_length=200,
        verbose_name='lesson title',
    )
    tags = models.ManyToManyField(
        'Tag', 
        related_name="lessons",
        related_query_name='lesson',
    )

    class Meta: 
        indexes = [models.Index(fields=['title'])]
        ordering = ['-title']
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', args=[str(self.id)]) # or kwargs={"pk": self.pk}

    # example url
    # from news import views
    # path('archive/', views.archive, name='news-archive')

class Tag(models.Model):
    """Creates a Tag model"""
    name = models.CharField(
        max_length=20,
        verbose_name='tag name',
    )
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', args=[str(self.id)])
