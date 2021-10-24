from blog.tests import TestDataStr, TestDataInt, create_category, create_test_user
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from strenum import StrEnum


class TestPutData(StrEnum):
    TITLE = "Updated Title"
    EXCERPT = "updated-excerpt"
    CONTENT = "Updated Content"


class TestPostDetail(APITestCase):
    pass


class TestPostList(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.list_create_url = reverse("blog_api:post-list")
        cls.detail_create_url = reverse("blog_api:post-detail", kwargs={"pk": 1})

    def test_posts_view(self):
        response = self.client.get(self.list_create_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        create_category()
        test_user = create_test_user()
        logged = self.client.login(username=test_user.user_name, password=TestDataStr.USER_PASSWORD_1)
        self.assertTrue(logged)
        post_data = {
            "title": TestDataStr.POST_TITLE,
            "content": TestDataStr.POST_CONTENT,
            "slug": TestDataStr.POST_SLUG,
            "author": TestDataInt.POST_AUTHOR,
            "category": TestDataInt.POST_CATEGORY_ID
        }
        response = self.client.post(self.list_create_url, post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.detail_create_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        self.test_post_create()
        put_data = {
            "title": TestPutData.TITLE,
            "excerpt": TestPutData.EXCERPT,
            "content": TestPutData.CONTENT,
            "category": TestDataInt.POST_CATEGORY_ID,
            "author": TestDataInt.POST_AUTHOR
        }
        response = self.client.put(self.detail_create_url, put_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        test_user_2 = create_test_user(TestDataStr.USER_NAME_2, TestDataStr.USER_PASSWORD_2)
        self.client.login(username=test_user_2.username, password=TestDataStr.USER_PASSWORD_2)
        response = self.client.put(self.detail_create_url, put_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
