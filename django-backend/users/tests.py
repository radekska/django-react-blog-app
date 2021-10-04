from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import NewUser


class TestUserData:
    EMAIL = "a@a.com"
    USER_NAME = "abc"
    FIRST_NAME = "A"
    PASSWORD = "strong"


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "email": TestUserData.EMAIL,
            "user_name": TestUserData.USER_NAME,
            "first_name": TestUserData.FIRST_NAME,
            "password": TestUserData.PASSWORD
        }
        cls.db = get_user_model()

    def _test_basic_user_data(self, user: NewUser):
        self.assertEqual(TestUserData.EMAIL, user.email)
        self.assertEqual(TestUserData.USER_NAME, user.user_name)
        self.assertEqual(TestUserData.FIRST_NAME, user.first_name)

    def test_superuser_creation(self):
        super_user = self.db.objects.create_superuser(**self.user_data)
        self._test_basic_user_data(super_user)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_active)

    def test_user_creation(self):
        user = self.db.objects.create_user(**self.user_data)
        self._test_basic_user_data(user)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_active)

    def test_email_not_provided(self):
        self.user_data["email"] = ""
        self.assertRaises(ValueError, lambda: self.db.objects.create_user(**self.user_data))

    def test_user_text_representation(self):
        user = self.db.objects.create(**self.user_data)
        self.assertEqual(TestUserData.USER_NAME, str(user))
