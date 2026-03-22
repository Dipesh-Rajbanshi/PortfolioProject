from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from .models import *
from projects.models import Project
from blogs.models import Blog
from django.core.mail import send_mail


# Create your views here.
def Home(request):
# Get projects and blogs
    projects = Project.objects.filter(is_published=True).order_by('-updated_at')[:5]
    blogs = Blog.objects.filter(is_published=True).order_by('-updated_at')[:5]
    combined_feed = []
    for project in projects:
        combined_feed.append({
            'type': 'project',
            'object': project,
            'updated_at': project.updated_at
        })
    for blog in blogs:
        combined_feed.append({
            'type': 'blog',
            'object': blog,
            'updated_at': blog.updated_at
        })
    combined_feed.sort(key=lambda x: x['updated_at'], reverse=True)
    context = {
        'user_data' : UserProfile.objects.first(),
        'social': SocialLink.objects.all().order_by('-id')[:5],
        'skills': Skill.objects.all(),
        'img' : Gallery.objects.all().order_by('-created_at')[:6],
        'feed': combined_feed,
        'contact' : ContactInfo.objects.first(),
        'blog': blogs,
        'project': projects

    }
    return render(request, 'index.html',context)

def GalleryView(request):
    context = {
        'cat' : Category.objects.all(),
        'img' : Gallery.objects.all()
    }
    return render(request,'gallery.html',context)


def Contact(request):
    if request.method == 'POST':
        # Get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        # Compose email
        email_subject = f"Contact Form: {subject if subject else 'No Subject'}"
        email_body = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        
        try:
            # Send email
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,  # From email (your email or noreply@yourdomain.com)
                [settings.RECIPIENT_EMAIL],     # To email (your email)
                fail_silently=False,
            )
            
            # Success message
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
            
        except Exception as e:
            # Error message
            messages.error(request, 'Failed to send message. Please try again.')
            return redirect('contact')
        
    context = {
        'contact': ContactInfo.objects.first(),
        'social': SocialLink.objects.all().order_by('-id')[:5]
    }
    return render(request,'contact.html',context)


# Custom error handlers

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)

def bad_request(request, exception):
    return render(request, '400.html', status=400)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)