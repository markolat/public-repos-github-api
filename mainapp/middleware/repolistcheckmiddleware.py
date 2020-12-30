from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from mainapp.globals import REPOSITORIES

# middleware class that checks if repository list is empty
class CheckRepoList(MiddlewareMixin):

    def process_request(self, request):
        if len(REPOSITORIES) == 0:
            return redirect('index')
        
        return None