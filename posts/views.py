from django.shortcuts import render
from .models import Posts


# Create your views here.


def all_posts(request):
    """Show all posts"""

    posts = Posts.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'posts/posts.html', context)
