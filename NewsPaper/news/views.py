from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, ArticlForm
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


class SearchPosts(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = PostFilter()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCrate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = "post_edit.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = "NEWS"
        return super().form_valid(form)


class ArticleCrate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('news.add_post')
    form_class = ArticlForm
    model = Post
    template_name = "post_edit.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = "ARTI"
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = "post_edit.html"


class PostDelete(PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('news.delete_post')
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("posts")