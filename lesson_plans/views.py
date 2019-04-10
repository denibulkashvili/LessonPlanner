from django.views.generic import TemplateView, ListView, DetailView
from lesson_plans.models import Lesson, Tag

# Create your views here.
class IndexView(TemplateView):
    model = Lesson
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_count"] = Lesson.objects.all().count()
        return context


class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"
    template_name = "lesson_list.html"


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson"
    template_name = "lesson_detail.html"

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tag_list.html"


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = "tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context["lessons"] = self.object.lessons.all()
        return context
