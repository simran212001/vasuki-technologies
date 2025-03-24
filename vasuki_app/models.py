from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

from django.db import models

class HomeStats(models.Model):
    happy_clients = models.PositiveIntegerField(default=0)
    projects = models.PositiveIntegerField(default=0)
    hours_of_support = models.PositiveIntegerField(default=0)
    hard_workers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Home Page Stats"
    





from django.db import models
from django.utils.text import slugify
from meta.models import ModelMeta

class Blog( models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

