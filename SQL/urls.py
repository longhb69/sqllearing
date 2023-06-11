from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sql/<str:title>", views.entry, name="entry"),
    path('tryit/', views.tryit, name="tryit"),
    path("query/<str:query>", views.query, name="query")
]