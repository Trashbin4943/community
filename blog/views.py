from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
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