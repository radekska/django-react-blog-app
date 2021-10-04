from enum import IntEnum
from typing import Tuple

from blog.models import Category, Post
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from strenum import StrEnum


class TestDataStr(StrEnum):
    EMAIL = "a@a.com"
    USER_NAME = "abc"
    FIRST_NAME = "A"
    PASSWORD = "strong"
    DJANGO_CATEGORY = "django"

    USER_NAME_1 = "test_user_1"
    USER_PASSWORD_1 = "qwerty123"

    USER_NAME_2 = "test_user_2"
    USER_PASSWORD_2 = "qwerty1234"

    POST_TITLE = "Test Title"
    POST_EXCERPT = "Test Excerpt"
    POST_CONTENT = "Test Content"
    POST_SLUG = "test-post-slug"
    POST_STATUS = "published"


def create_category(category: TestDataStr = TestDataStr.DJANGO_CATEGORY) -> Category:
    return Category.objects.create(name=category)


def create_test_user(username: TestDataStr = TestDataStr.USER_NAME_1,
                     password: TestDataStr = TestDataStr.USER_PASSWORD_1) -> Tuple[Category, User]:
    return get_user_model().objects.create_user(user_name=username, password=password, email=TestDataStr.EMAIL,
                                                first_name=TestDataStr.FIRST_NAME)


class TestDataInt(IntEnum):
    POST_CATEGORY_ID = 1
    POST_AUTHOR = 1


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_user()
        create_category()
        Post.objects.create(category_id=TestDataInt.POST_CATEGORY_ID, title=TestDataStr.POST_TITLE,
                            excerpt=TestDataStr.POST_EXCERPT, content=TestDataStr.POST_CONTENT,
                            slug=TestDataStr.POST_SLUG, author_id=TestDataInt.POST_AUTHOR)

    def test_blog_content(self):
        post = Post.post_objects.get(id=1)
        category = Category.objects.get(id=1)

        self.assertEqual(str(post.author), TestDataStr.USER_NAME_1.value)
        self.assertEqual(str(post.title), TestDataStr.POST_TITLE.value)
        self.assertEqual(str(post.content), TestDataStr.POST_CONTENT.value)
        self.assertEqual(str(post.status), TestDataStr.POST_STATUS.value)
        self.assertEqual(str(post), TestDataStr.POST_TITLE.value)
        self.assertEqual(str(category), TestDataStr.DJANGO_CATEGORY.value)


class TestCategoryModel(TestCase):
    def test_category_text_representation(self):
        category = create_category()
        self.assertEqual(TestDataStr.DJANGO_CATEGORY, str(category))