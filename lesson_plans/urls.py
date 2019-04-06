from django.urls import path
from lesson_plans.views import LessonDetailView, LessonListView, TagDetailView, TagListView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<tag>/', TagDetailView.as_view(), name='tag_detail'),
]