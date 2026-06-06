from django.db import models

class Service(models.Model):
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    full_desc = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    features = models.JSONField(default=list, help_text="List of features")
    why_choose_us = models.JSONField(default=list, blank=True, help_text="List of reasons to choose us")
    conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
