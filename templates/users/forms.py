from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    model = User
    fields = ["username", "password"] # type: ignore