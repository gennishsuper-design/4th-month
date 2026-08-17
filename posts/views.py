from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import CategoryForm, PostForm
from posts.models import Category, Post

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello world!</h1>")


def post_list(request: HttpRequest):
    posts = Post.objects.order_by("-created_at").all()

    return render(request, "posts/posts.html", {"posts": posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})


def create_category(request: HttpRequest) -> HttpResponse:
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("post_create")

    return render(request, "posts/create_category.html", {"form": form})


def create_post(request: HttpRequest) -> HttpResponse:
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("post_list")

    return render(request, "posts/create_post.html", context={"form": form})
