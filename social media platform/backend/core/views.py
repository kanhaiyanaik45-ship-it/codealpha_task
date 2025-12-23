from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PostForm, CommentForm
from .models import Profile, Post, Comment, Like


def index(request):
    posts = Post.objects.select_related('author__user').order_by('-created_at')[:50]
    return render(request, 'feed.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    posts = Post.objects.filter(author=profile).order_by('-created_at')
    is_following = False
    if request.user.is_authenticated:
        try:
            is_following = profile.followers.filter(pk=request.user.profile.pk).exists()
        except Exception:
            is_following = False
    return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'is_following': is_following})


@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    me = request.user.profile
    if me in target_profile.followers.all():
        target_profile.followers.remove(me)
    else:
        target_profile.followers.add(me)
    return redirect('profile', username=username)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user.profile
            c.post = post
            c.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(post=post, user=request.user.profile).exists()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form, 'liked': liked})


@login_required
def like_toggle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = request.user.profile
    like, created = Like.objects.get_or_create(post=post, user=profile)
    if not created:
        like.delete()
    return redirect('post_detail', pk=pk)
