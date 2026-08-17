from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from posts.forms import CategoryForm, PostForm
from posts.models import Category, Post


class HelloWorldView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse("<h1>Hello world!</h1>")


class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.order_by("-created_at").all()


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "id"


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("post_list")


class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = "posts/create_category.html"
    success_url = reverse_lazy("post_create")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    context_object_name = "post"
    pk_url_kwarg = "id"

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        # allow staff or the original author if model has `author` field
        if user.is_staff:
            return True
        return getattr(post, "author", None) == user
