from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posts
from .forms import PostsForm
from django.contrib import messages

# Create your views here.


@login_required
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


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    if request.user != post.user and not request.user.is_superuser:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('posts')

    if request.method == "POST":
        form = PostsForm(request.POST, instance=post)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.edited_by = request.user
            post_form.save()
            messages.success(request, "Post updated successfully")
            return redirect('posts')
        else:
            messages.error(request,
                           "Update failed. Please ensure the form is valid.")
    else:
        form = PostsForm(instance=post)

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/edit_post.html', context)
