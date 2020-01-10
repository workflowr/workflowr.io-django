#!/usr/bin/env python

# Not the best long-term way to run scripts for a Django site, but this is just
# a temporary script to help during development.
# https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from projects.models import Author, Project, Publication, Tag

aut1, created = Author.objects.get_or_create(name="author_1", email="email_1@example.com")
aut2, created = Author.objects.get_or_create(name="author_2", email="email_2@example.com")
aut3, created = Author.objects.get_or_create(name="author_3", email="email_3@example.com")

tag1, created = Tag.objects.get_or_create(name="tag_1")
tag2, created = Tag.objects.get_or_create(name="tag_2")
tag3, created = Tag.objects.get_or_create(name="tag_3")

pub1, created = Publication.objects.get_or_create(doi="10.1000/1", title="publication 1")
pub2, created = Publication.objects.get_or_create(doi="10.1000/2", title="publication 2")
pub3, created = Publication.objects.get_or_create(doi="10.1000/3", title="publication 3")

proj1, created = Project.objects.get_or_create(name="project_1", url="https://example.com/1", author=Author.objects.get(id=1))
proj2, created = Project.objects.get_or_create(name="project_2", url="https://example.com/2", author=Author.objects.get(id=2))
proj3, created = Project.objects.get_or_create(name="project_3", url="https://example.com/3", author=Author.objects.get(id=3))

proj1.publications.add(pub1)
proj2.publications.add(pub2)
proj3.publications.add(pub3)

proj1.tags.add(tag1, tag2)
proj2.tags.add(tag3)
