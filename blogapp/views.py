from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import JsonResponse
from django.template.loader import render_to_string
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blogapp/posts')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_update(request, pk):
    expense = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=Post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=expense)
    return render(request, 'posts/post_form.html', {'form': form, 'post': Post})

def post_delete(request, pk):
    expense = Post.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': Post})


def front_post_view(request):
    posts = Post.objects.all()[:10]
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request
        post_partial_html = render_to_string('posts/frontpost_partial.html', {'posts': posts})
        return JsonResponse({'new_posts': len(posts), 'html': post_partial_html})
    else:
        # Handle regular request
        return render(request, 'posts/frontpost.html', {'posts': posts})