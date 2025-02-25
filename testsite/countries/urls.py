from django.urls import path

from . import views

urlpatterns = [
    path("stats/", views.stats, name="stats"),
    path("countries/", views.get_countries, name="countries"),
]
