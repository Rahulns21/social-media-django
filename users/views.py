from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.models import *
from .models import *
from .forms import *

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('User authenticated and logged in')
            else:
                return HttpResponse('Invalid credentials!')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('User logged out')
    return redirect('users:index')

def user_register(request):
    user_form = UserRegistrationForm()
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
        else:
            user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

@login_required
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    context = {'posts': posts}
    return render(request, 'users/index.html', context=context)

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/edit.html', context=context)