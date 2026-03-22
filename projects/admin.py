from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','short_description','image','is_published','created_at','updated_at')
    filter_horizontal = ['technology_used']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
