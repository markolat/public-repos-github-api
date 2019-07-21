from django.urls import path

from mainapp.api import views


urlpatterns = [
    path('repositories', views.get_repositories, name='get-repositories'),
    path('repositories/change-name', views.change_name, name='change-name'),
]