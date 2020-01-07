from django.db import models

from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publication(models.Model):
    doi = models.CharField('DOI', max_length=200)
    pmid = models.CharField('PMID', max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.doi

class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField('URL', max_length=200)
    author = models.ManyToManyField(Author)
    tag = models.ManyToManyField(Tag)
    publication = models.ManyToManyField(Publication)

    def __str__(self):
        return self.name
