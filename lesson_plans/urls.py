from django.urls import path
from lesson_plans.views import (
    LessonDetailView,
    LessonListView,
    TagDetailView,
    TagListView,
    IndexView,
    AboutView,
    OnlineGamesView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("lessons/", LessonListView.as_view(), name="lesson_list"),
    path("lesson/<pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tag/<slug:slug>/", TagDetailView.as_view(), name="tag_detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("online-games/", OnlineGamesView.as_view(), name="online_games"),
]
