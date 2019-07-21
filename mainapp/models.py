from django.db import models

# Create your models here.

class Repository(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Repository name")
    description = models.TextField(help_text="Repository description text")
    url =  models.CharField(max_length=200, help_text="Repository git url") # corresponds to git_url field
    language = models.CharField(max_length=50, help_text="Programming language name")
    watchers_count =  models.IntegerField()

