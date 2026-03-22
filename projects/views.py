from django.shortcuts import render, get_object_or_404
from .models import Project
from Core.models import *

# Create your views here.
def ProjectView(request):
    context = {
        'data': Project.objects.filter(is_published=True).order_by('-updated_at')[:20]
    }
    return render(request, 'project.html',context)

def ProjectDetails(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    context = {
        'data': project,
        'social': SocialLink.objects.all(),
        'user': UserProfile.objects.first()
    }
    return render(request, 'project-detail.html', context)