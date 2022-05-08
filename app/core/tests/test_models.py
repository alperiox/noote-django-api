from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

import os
import tempfile


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@test.com"
        password = "TestPassword123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_and_photo_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@test.com"
        password = "TestPassword123"

        photo = tempfile.NamedTemporaryFile(suffix=".jpg").read()

        user = get_user_model().objects.create_user(
            email=email, password=password, photo=photo
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        """Test creating a new user with email that contains uppercase case characters"""
        email = "test634@TeSt.com"
        password = "TestPassword123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_create_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="test1235Tsert")

    def test_create_new_super_user(self):
        """Text creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
