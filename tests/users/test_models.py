from django.test import TestCase
from apps.users.models import CustomUser


class CustomUserManagerTests(TestCase):
    
    def test_create_user(self):
        user = CustomUser.objects.create_user(email="user@gmail.com", password="notarealpassword", is_active=True)
        self.assertEqual(user.email, "user@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(email="superuser@gmail.com", password="notarealpassword", is_active=True, is_staff=True, is_superuser=True)
        self.assertEqual(user.email, "superuser@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class CsutomeUserModelTests(TestCase):

    def test_user_slug_is_unique(self):
        user1 = CustomUser.objects.create_user(email="user1@gmail.com", password="notarealpassword", slug="weird-user1")
        user2 = CustomUser.objects.create_user(email="user2@gmail.com", password="notarealpassword", slug="weird-user2")
        self.assertNotEqual(user1.slug, user2.slug)
        
    def test_user_slug_is_generated_if_blank(self):
        user = CustomUser.objects.create_user(email="user@gmail.com", password="notarealpassword")
        self.assertNotEqual(user.slug, "")

    def test_user_slug_is_not_overwritten(self):
        user = CustomUser.objects.create_user(email="user@gmail.com", password="notarealpassword", slug="weird-slug")
        self.assertEqual(user.slug, "weird-slug")