from django.urls import path, re_path

from . import views
    
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("create/", views.create, name="create"),
    path("random_page/", views.random_page, name="random_page"),
    #path("<str:?q=^>", views.search, name="search")
    #re_path(r'^index/$', views.index, name='index'),
    re_path("search/", views.search, name='search'),
    #re_path(r'posts/(?P<post_id>[0-9]+)/$', post_detail_view)

]
