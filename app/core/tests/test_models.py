"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test cases """
    def test_create_user_with_email_successfully(self):
        """ Test creating a user with email is successful """
        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email is normalized for users. """
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
            ['test5@example.com', 'test5@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email,
                password='sample123'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """ Test creating a new user w/o email raises ValueError """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", 'test123')

    def test_create_superuser(self):
        """ test creating superuser """
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
