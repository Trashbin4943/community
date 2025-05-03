from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import PostForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def create_post(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_list')
    else:
        form=PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_list(request):
    posts = Blog.objects.all()
    return render (request, 'post_list.html', {'posts': posts})

def view_post(request, pk):
    post=get_object_or_404(Blog,pk=pk)
    return render (request, 'view_post.html', {'post': post})

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post= get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post',post})

def signup_view(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('post_list')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})
