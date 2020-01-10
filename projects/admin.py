from django.contrib import admin

from .models import Author, Project, Publication, Tag

admin.site.register(Author)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Tag)
