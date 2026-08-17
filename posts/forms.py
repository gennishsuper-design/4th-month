from django import forms

from posts.models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название категории",
                    "maxlength": "200",
                }
            )
        }
        labels = {
            "name": "Название категории",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image", "category")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg rounded-3",
                    "placeholder": "Введите заголовок поста...",
                    "maxlength": "200",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control rounded-3",
                    "rows": 6,
                    "placeholder": "Расскажите о чём ваш пост...",
                }
            ),
            "category": forms.Select(
                attrs={"class": "form-select rounded-3"}
            ),
        }
        labels = {
            "title": "Заголовок",
            "description": "Описание",
            "image": "Изображение",
            "category": "Категория",
        }

    def clean_title(self) -> str:
        title = self.cleaned_data["title"]

        if title == "banned word":
            raise forms.ValidationError("this word is banned")

        return title
