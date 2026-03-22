from django.contrib import admin
from .models import *

# Register your models here.

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ['platform_name','icon','url']  

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','profession','bio','created_at')
    inlines = [SocialLinkInline]

    def has_add_permission(self, request):
        return not UserProfile.objects.exists() 
  

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'skill_name', 'created_at', 'updated_at')
     # Add help text in the form
    fieldsets = (
        (None, {
            'fields': ('skill_name',),
            'description': '<div style="padding: 10px; background: #417690; margin-bottom: 15px;">'
                '<strong>💡 Tip:</strong> Enter Skill that  you\'ve learned and you know  till date.</div>'
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')   

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_name','image', 'category','created_at','updated_at')
    list_display_links = ('image_name','category')         

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title','message','phone_number','created_at','updated_at')

    def has_add_permission(self,request):
        return not ContactInfo.objects.exists()

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)