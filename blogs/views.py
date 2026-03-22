from django.shortcuts import render, get_object_or_404
from blogs.models import Blog

# Create your views here.
def BlogView(request):
    context = {
        'data': Blog.objects.filter(is_published=True).order_by('-updated_at')[:12]
    }
    return render(request, 'blog.html',context)

def BlogDetails(request,slug):
    blog = get_object_or_404(Blog, slug=slug, is_published=True)
    context = {
        'blog': blog
    }
    return render(request, 'blog-detail.html',context)