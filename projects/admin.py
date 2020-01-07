from django.contrib import admin

from .models import Project, Publication, Tag

admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Tag)
