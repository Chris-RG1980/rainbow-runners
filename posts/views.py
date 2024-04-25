from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Posts, Comment
from .forms import PostsForm, CommentForm
from django.contrib import messages

# Create your views here.


def is_in_group(user, group_name):
    """
    Check if the user is in the given group.
    """
    return user.groups.filter(name=group_name).exists()


@login_required
def all_posts(request):
    """
    A view to show all posts
    """

    form = PostsForm()

    is_coordinator = is_in_group(request.user, 'co-ordinators')
    is_admin = is_in_group(request.user, 'admin')

    if request.method == "POST":
        if is_coordinator or is_admin:
            form = PostsForm(request.POST)
            if form.is_valid() and request.user.is_authenticated:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, 'Post added successfully')
                return redirect('posts')
            else:
                msg = "Update failed. Please ensure the form is valid."
                messages.error(request, msg)
        else:
            messages.error(request, "You are not authorized to create a post.")
            return redirect('posts')

    posts = Posts.objects.all().order_by('-created_date')
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'posts/posts.html', context)


@login_required
def edit_post(request, post_id):
    """
    A view to allow co-ordinators and admin to edit posts
    """

    post = get_object_or_404(Posts, id=post_id)
    is_coordinator = is_in_group(request.user, 'co-ordinators')
    is_admin = is_in_group(request.user, 'admin')

    if request.method == "POST":
        if is_coordinator or is_admin:
            form = PostsForm(request.POST, instance=post)
            if form.is_valid() and request.user.is_authenticated:
                post_form = form.save(commit=False)
                post_form.edited_by = request.user
                post_form.save()
                messages.success(request, "Post updated successfully")
                return redirect('posts')
            else:
                msg = "Update failed. Please ensure the form is valid."
                messages.error(request, msg)
        else:
            msg = "You are not authorized to edit this post."
            messages.error(request, msg)
            return redirect('posts')
    else:
        form = PostsForm(instance=post)

    print("Is Coordinator:", is_coordinator)
    context = {
        'post': post,
        'form': form
    }

    return render(request, 'posts/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """
    A view to allow admin or co-ordinators to delete posts
    """

    post = get_object_or_404(Posts, id=post_id)
    is_coordinator = is_in_group(request.user, 'co-ordinators')
    is_admin = is_in_group(request.user, 'admin')

    if is_coordinator or is_admin:
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect('posts')
    else:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('posts')


@login_required
def post_detail(request, post_id):
    """
    A view to allow users to comment on posts
    """

    post = get_object_or_404(Posts, id=post_id)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect(post.get_absolute_url())
        else:
            messages.error(
                request,
                'Comment failed. Please ensure the form is valid.'
            )
    else:
        comment_form = CommentForm()

    comments = Comment.objects.filter(
        post_id=post_id).order_by('-created_date')

    page = request.GET.get('page')
    paginator = Paginator(comments, 3)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def delete_comment(request, post_id, comment_id):
    """
    A view to allow the post author,
    co-ordinators or admin to delete comments
    """

    comment = get_object_or_404(Comment, id=comment_id)
    is_coordinator = is_in_group(request.user, 'co-ordinators')
    is_admin = is_in_group(request.user, 'admin')

    if request.user == comment.author or is_coordinator or is_admin:
        comment.delete()
        messages.success(request, "Comment deleted successfully")
        return redirect(reverse(
                'post_detail',
                kwargs={'post_id': post_id})
            )
    else:
        msg = "You are not authorized to delete this comment."
        messages.error(request, msg)
        return redirect('posts')
