from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("published_date")
    return render(request,'pages/index.html',{'posts' : posts})

def about(request):
    return render(request, 'pages/about.html')

def post_list(request):
    pass