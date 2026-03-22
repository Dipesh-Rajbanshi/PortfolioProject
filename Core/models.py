from django.db import models
import os


# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='Profile/profile-picture', null=True, blank=True)
    cover_picture = models.ImageField(upload_to='Profile/cover-picture', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    resume_file = models.FileField(upload_to='Resume/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class SocialLink(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='socials')
    platform_name = models.CharField(max_length=50) 
    url = models.URLField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.platform_name}"
    
class Skill(models.Model):
    skill_name = models.CharField(max_length=100, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    if instance.category:
        return f'Gallery/{instance.category.name}/{filename}'
    return f'Gallery/{filename}'


class Gallery(models.Model):
    image_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.image_name or "Image"
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class ContactInfo(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length=14,null=True,blank=True)
    working_time = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title