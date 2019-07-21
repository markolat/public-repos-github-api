# Implementation

## Overview
I have implemented this solution using pure Django, without any aditional app (like Django rest framework) mostly because of simplicity of the task.

## Virtual environment
All of dependencies including Django itself were installed in python virtual environment.
I have also used python-dotenv library for storing and securing config data such as database password, name etc. I left app secret key in settings module on purpose, but it should be put in .env file.

## Storing data
The project has mysql database set and ready even though i did not use it for storing repositories. For caching repository data i used one global list called REPOSITORIES.

##  Main App
There is only one app called 'mainapp' and it's content is described in the text ahead.

### Api
I have made two simple function views. One that gets the repositories using requests python library and github api endpoint for fetching list of users public repos and other that changes repository name in cached list of Repository objects. Both of them returns json data with status and message info.

### Middleware
There is simple middleware implementation that hooks at request for displaying list of repositories and the one that changes the name of the repository. It checks if cached repositories list is empty and redirects to home page if so.

### Static files
There is css file that styles the web app a little bit. And there is js file that implements ajax calls, using jQuery. One is for calling api view for fetching repositories and the other is for changing a name of a repository.

### Templates
Templates for index, list repositories and change repository name pages.

### Globals
Global repositories list is stored in globals module.

### Models
Repository model implemented here.

### Views
View functions for rendering and showing pages to the user.

