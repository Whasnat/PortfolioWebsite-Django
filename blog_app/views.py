from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog_home(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_app/blog_home.html', {'blogs': blogs})

def blog_details(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog_app/blog_details.html', {'blog':blog_detail})