from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.contrib import messages

# Create your views here.


def all_posts(request):
    """Show all posts"""

    form = PostsForm()

    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('posts')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')

    posts = Posts.objects.all()

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'posts/posts.html', context)
