from django.db import models
import uuid
# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(
        null=True,upload_to='images', blank=True)
    body = models.TextField(null=True)
    project_link = models.CharField(max_length=200, null=True, blank=True)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
