from django.shortcuts import render
from django.views import generic

from .models import Author, Platform, Project, Publication, Tag


def index(request):
    return render(request, 'index.html')


class AuthorList(generic.ListView):
    model = Author


class AuthorDetail(generic.DetailView):
    model = Author
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list_for_author'] = Project.objects.filter(
            author=context['author'])
        return context


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


class PublicationList(generic.ListView):
    model = Publication


class PlatformDetail(generic.DetailView):
    model = Platform
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list_for_platform'] = Project.objects.filter(
            platform=context['platform'])
        return context
