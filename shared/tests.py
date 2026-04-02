from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from .models import ContactMessage

class ContactFormAPITest(TestCase):
    def test_successful_submission(self):
        """
        Ensure contact form can be submitted successfully.
        """
        url = reverse("contact-form")
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message.",
        }
        with patch("shared.views.send_mail") as mocked_send_mail:
            response = self.client.post(url, data, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(ContactMessage.objects.count(), 1)
            self.assertEqual(ContactMessage.objects.get().name, "Test User")
            mocked_send_mail.assert_called_once()

    def test_invalid_email(self):
        """
        Ensure form submission fails with an invalid email.
        """
        url = reverse("contact-form")
        data = {
            "name": "Test User",
            "email": "invalid-email",
            "message": "This is a test message.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_empty_name(self):
        """
        Ensure form submission fails with an empty name.
        """
        url = reverse("contact-form")
        data = {
            "name": "",
            "email": "test@example.com",
            "message": "This is a test message.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_empty_message(self):
        """
        Ensure form submission fails with an empty message.
        """
        url = reverse("contact-form")
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_email_sending(self):
        """
        Ensure email is sent on successful submission.
        """
        url = reverse("contact-form")
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message.",
        }
        with patch("shared.views.send_mail") as mocked_send_mail:
            self.client.post(url, data, format="json")
            self.assertTrue(mocked_send_mail.called)
            self.assertEqual(mocked_send_mail.call_count, 1)
            args, kwargs = mocked_send_mail.call_args
            self.assertEqual(args[0], "New Contact Message from Test User")
            self.assertIn("Name: Test User", args[1])
            self.assertIn("Email: test@example.com", args[1])
            self.assertIn("""Message:
This is a test message.""", args[1])
