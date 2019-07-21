from django.shortcuts import redirect

from mainapp.globals import REPOSITORIES

# middleware class that checks if repository list is empty
class CheckRepoList(object):

    def process_request(self, request):
        if len(REPOSITORIES) == 0:
            return redirect('index')
        
        return None