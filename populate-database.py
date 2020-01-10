#!/usr/bin/env python

# Not the best long-term way to run scripts for a Django site, but this is just
# a temporary script to help during development.
# https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from projects.models import Author, Tag

Author.objects.create(name="author_1", email="email_1@example.com")
Author.objects.create(name="author_2", email="email_2@example.com")
Author.objects.create(name="author_3", email="email_3@example.com")

Tag.objects.create(name="tag_1")
Tag.objects.create(name="tag_2")
Tag.objects.create(name="tag_3")
