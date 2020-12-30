from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware

from mainapp.globals import REPOSITORIES
from mainapp.middleware.repolistcheckmiddleware import CheckRepoList

# Create your views here.


def index(request):
    """ Returns home page """

    return render(request, 'index.html')


@decorator_from_middleware(CheckRepoList)
def list_repositories(request):
    """ Returns page with data of all repositories of a user """

    return render(request, 'repository_list.html', {'repositories': REPOSITORIES})


@decorator_from_middleware(CheckRepoList)
def change_repository_name(request):
    """ Returns page with form for updating repository name """

    return render(request, 'repository_change.html')


def reload(request):
    """ Reloads app (Clear repositories global list and redirects to index page) """

    REPOSITORIES.clear()

    return redirect('index')
