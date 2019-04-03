from django.contrib import admin
from .models import Lesson, Tag

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Tag)