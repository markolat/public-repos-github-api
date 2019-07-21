from django.urls import path

from mainapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reload', views.reload, name='reload'),
    path('repositories', views.list_repositories, name='list-repositories'),
    path('repositories/change-name', views.change_repository_name, name='change-name-form'),
]