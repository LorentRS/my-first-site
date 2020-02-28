from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by("published_date")
    return render(request,'pages/index.html',{'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'pages/post_detail.html',{'post' : post})
