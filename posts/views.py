from django.shortcuts import render, redirect # type: ignore
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from posts.models import Category, Post
# Create your views here.

def hello_world(request: HttpRequest):
    return HttpResponse('<h1>Hello world!</h1>')


def my_name(request: HttpRequest):
    return HttpResponse('<h1>Bekzhan</h1>')


def post_list(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "posts/posts.html", {"posts": posts})

def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = Post.objects.get(id=id)

    return render(request, "posts/post_detail.html", {"post": post})

def create_post(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all().order_by("name")

    if request.method.lower() == "post":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        new_category_name = request.POST.get("new_category")

        category = None
        if category_id:
            category = Category.objects.filter(id=category_id).first()
        elif new_category_name and new_category_name.strip():
            category, _ = Category.objects.get_or_create(name=new_category_name.strip())

        Post.objects.create(title=title, description=description, image=image, Category=category)
        return redirect("post_list")

    return render(request, "posts/create_post.html", {"categories": categories})
