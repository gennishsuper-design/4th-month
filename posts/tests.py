from django.test import TestCase
from django.urls import reverse

from posts.models import Category, Post


class CreatePostWithCategoryTests(TestCase):
    def test_create_post_with_new_category(self):
        response = self.client.post(
            reverse("post_create"),
            {
                "title": "Новый пост",
                "description": "Описание поста",
                "new_category": "Python",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Новый пост").exists())
        self.assertTrue(Category.objects.filter(name="Python").exists())
        self.assertEqual(Post.objects.get(title="Новый пост").Category.name, "Python")
