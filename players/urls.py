from django.urls import path

from . import views

urlpatterns = [
    path("", views.teams, name="index"),
    path("<int:team_id>/", views.men, name="men"),
]