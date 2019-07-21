import requests
import json

from django.http import HttpResponse

from mainapp.models import Repository
from mainapp.globals import REPOSITORIES


def get_repositories(request):
    """ Gets the list of public repositories of a user """

    if request.method == 'GET':
    
        REPOSITORIES.clear()

        github_username = request.GET.get('username', False)
        response = requests.get(f"https://api.github.com/users/{github_username}/repos")

        data = {
            'status':'fail',
            'message': 'Error while collecting data.'
        }

        if github_username and response.status_code == 200:
        
            data['status'] = 'success'
            repo_list = json.loads(response.content)
            if len(repo_list) == 0:
                data['message'] = 'User valid but does not have any public repository'
            else:
                for repo in repo_list:
                    REPOSITORIES.append(
                        Repository(
                            id=repo['id'],
                            name = repo['name'],
                            description = repo['description'] if repo['description'] != None else 'No description',
                            url = repo['git_url'],
                            language = repo['language'],
                            watchers_count = repo['watchers_count']
                        )
                    )
                data['message'] = 'Repository list fetched.'

        return HttpResponse(json.dumps(data), content_type="application/json", status=response.status_code)


def change_name(request):
    """ Finds the repository with given id and changes it's name to a new value """

    if request.method == 'POST':

        data = {
            'status':'fail',
            'message': 'Bad data'
        }
        status_code = 400
        changed = False

        repo_id = int(request.POST.get('id', False))
        new_name = request.POST.get('new-name', False)

        if repo_id and new_name:
            
            for repo in REPOSITORIES:
                if repo.id == repo_id:
                    repo.name = new_name
                    changed = True
                    break

            if changed:
                data['status'] = 'success'
                data['message'] = 'You have successfuly changed name of repository'
                status_code = 200
            else:
                data['message'] = 'Repository not found. Wrong id.'
                status_code = 404

        return HttpResponse(json.dumps(data), content_type="application/json", status=status_code)