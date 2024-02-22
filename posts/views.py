from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('users:index')
    else:
        form = PostCreateForm(data=request.GET)
    context = {'form': form}
    return render(request, 'posts/create.html', context=context)

def feed(request):
    posts = Post.objects.all()
    logged_user = request.user
    context = {'posts': posts, 'logged_user': logged_user}
    return render(request, 'posts/feed.html', context=context)

def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('posts:feed')