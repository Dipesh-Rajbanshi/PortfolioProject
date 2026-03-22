from django.db import models
from Core.models import Skill
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=300)
    technology_used = models.ManyToManyField(Skill, blank=True)
    full_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    github_repo = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Always generate slug from title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
