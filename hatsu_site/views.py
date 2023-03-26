from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView

from .models import *
from .utils import *


class Blog(DataMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return self.join_context(c_def, context)


class Post(DataMixin, DetailView):
    model = Post
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].title)
        return self.join_context(c_def, context)
