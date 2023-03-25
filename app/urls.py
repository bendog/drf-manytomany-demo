from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.ProfileListView.as_view(), name="profile-list"),
    path("skill/", views.SkillListView.as_view(), name="skill-list"),
]
