from django.shortcuts import render
from django.views import generic

from .models import Author, Project, Tag


def index(request):
    return render(request, 'index.html')


class AuthorList(generic.ListView):
    model = Author


class AuthorDetail(generic.DetailView):
    model = Author
    slug_field = 'name'
    slug_url_kwarg = 'name'


class ProjectList(generic.ListView):
    model = Project


class ProjectDetail(generic.DetailView):
    model = Project
    slug_field = 'name'
    slug_url_kwarg = 'name'

class TagList(generic.ListView):
    model = Tag


class TagDetail(generic.DetailView):
    model = Tag
    slug_field = 'name'
    slug_url_kwarg = 'name'
