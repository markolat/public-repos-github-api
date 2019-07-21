# Python test

Displays github public repositories of a user.

### IDE
Visual studio code, version 1.36.1

## Installation

Clone this repository and install dependencies inside your virtualenv

```bash
pip install -r requirements.txt
```

## Run server
Run developement server
```bash
python manage.py runserver
```
## Usage
Open your browser and go to localhost:8000 (default port if not explicitly changed)

#### Home page
Here you can enter username of a github user. After 'load data' button click, message will apear.
If everything went ok, there will be two more buttons (List repositories and Change repository name) which will take 
you to the corresponding pages.

#### List repositories page
If cached data exists, here will be shown table with data of all public repositories from a user.

#### Change repository name page
Shows form with two inputs (repository id and new repository name). After inserting data into inputs and clicking submit button, message will be displayed. If everything went well, repository with given id will be changed.

#### Reload button
If you press this button cached data will be cleared and you will be redirected to home page where you can insert new username and get new data.