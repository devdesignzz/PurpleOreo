from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update-post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('index')


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            confessions = Post.objects.all()
        else:
            confessions = Post.objects.filter(author_id=request.user)
        
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'dashboard.html', {'Confessions':confessions, 'full_name':full_name})
    else:
        return HttpResponseRedirect('/members/login/')