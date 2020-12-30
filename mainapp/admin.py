from django.contrib import admin

from mainapp.models import Repository

# Register your models here.

@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url', 'language', 'watchers_count')
