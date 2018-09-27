from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publication(models.Model):
    doi = models.CharField(max_length=200)
    pmid = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.doi

class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    author = models.ManyToManyField(User)
    tag = models.ManyToManyField(Tag)
    publication = models.ManyToManyField(Publication)

    def __str__(self):
        return self.name
