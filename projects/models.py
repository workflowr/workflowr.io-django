from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Author(models.Model):
    # Avoid the complication of a registered user for the moment
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('projects:author_detail',
                       args=[self.project_set.filter()[0].platform.name, self.name])

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.SlugField(primary_key=True)

    def get_absolute_url(self):
        return reverse('projects:tag_detail', args=[self.name])

    def __str__(self):
        return self.name


class Publication(models.Model):
    doi = models.CharField('DOI', max_length=200, unique=True)
    pmid = models.CharField('PMID', max_length=200, blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.doi


class Platform(models.Model):
    name = models.SlugField(primary_key=True)
    url = models.URLField('URL')

    def get_absolute_url(self):
        return reverse('projects:platform_detail', args=[self.name])

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.SlugField(max_length=200)
    url = models.URLField('URL')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publications = models.ManyToManyField(Publication, blank=True)

    def __str__(self):
        return self.name
