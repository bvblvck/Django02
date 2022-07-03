from django.shortcuts import render, reverse_lazy

# Create your views here.

from django.views.generic.edit import ListView
from .models import Post

class PostListView(ListView):
      model = Post

from django.views.generic.edit import CreateView
from .models import Post

class PostCreateView(CreateView):
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")

from django.views.generic.edit import DetailView
from .models import Post

class PostListView(DetailView):
      model = Post

from django.views.generic.edit import UpdateView
from .models import Post

class PostCreateView(UpdateView):
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")

from django.views.generic.edit import DeleteView
from .models import Post

class PostCreateView(DeleteView):
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")

