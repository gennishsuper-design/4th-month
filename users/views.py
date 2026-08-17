from django.contrib.auth import authenticate, login
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import UserForm, LoginForm


class RegisterView(CreateView):
    form_class = UserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            form.add_error(None, "Неверные учетные данные")
            return self.form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)
