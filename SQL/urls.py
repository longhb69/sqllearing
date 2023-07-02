from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sql/<str:title>", views.entry, name="entry"),
    path('tryit/<str:statement>', views.tryit, name="tryit"),
    path("query/<str:query>", views.query, name="query"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("answer/<str:title>", views.answer, name="answer")
]