from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=300)
    full_details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Blogs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Always generate slug from title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)