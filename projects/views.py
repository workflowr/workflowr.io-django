from django.shortcuts import render
from django.views import generic

from .models import Tag


def index(request):
    return render(request, 'index.html')


class TagList(generic.ListView):
    model = Tag


class TagDetail(generic.DetailView):
    model = Tag
