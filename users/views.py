from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from users.forms import UserForm
from django.contrib.auth import login 
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect, render


def register(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method.lower() == "post": # type: ignore
        form = UserForm(request.POST)
        if form.is_valid():
            form.instance.save()
            form.instance.password = form.instance.set_password(form.cleaned_data["password"])
            login(request, form.instance)
            return redirect("post_list")
        

    return render(request, "users/register.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    form = UserForm()

    if request.method.lower() == "post":
        form = UserForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, username=form.cleaned_data["username"])

            if user.check_password(form.cleaned_data["password"]):
                login(request, user)    #type: ignore
                return redirect("post_list")

    return render(request, "users/login.html", context={"form": form})
