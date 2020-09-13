from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("editor/", views.editor, name="editor"),
    path("random_page/", views.random_page, name="random_page"),
    path("search/", views.search, name='search'),
]
