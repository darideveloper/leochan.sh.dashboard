# Tasks: Implement Contact Form

## Phase 1: Model Implementation
- [x] **Create ContactMessage Model**
  - Add `ContactMessage` to `shared/models.py`.
  - fields: `name`, `email`, `message`, `created_at`.
  ```python
  class ContactMessage(models.Model):
      name = models.CharField(max_length=255)
      email = models.EmailField()
      message = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return f"Message from {self.name} ({self.email})"

      class Meta:
          verbose_name = "Contact Message"
          verbose_name_plural = "Contact Messages"
          ordering = ["-created_at"]
  ```

- [x] **Register Model in Admin**
  - Register `ContactMessage` in `shared/admin.py` using `unfold.admin.ModelAdmin`.
  ```python
  from unfold.admin import ModelAdmin
  from .models import ContactMessage

  @admin.register(ContactMessage)
  class ContactMessageAdmin(ModelAdmin):
      list_display = ["name", "email", "created_at"]
      search_fields = ["name", "email", "message"]
      readonly_fields = ["name", "email", "message", "created_at"]
      date_hierarchy = "created_at"
  ```

- [x] **Create and Apply Migrations**
  - Run `python manage.py makemigrations shared`.
  - Run `python manage.py migrate shared`.

## Phase 2: API Implementation
- [x] **Create Serializer**
  - Create `shared/serializers.py` (if it doesn't exist) and add `ContactMessageSerializer`.
  ```python
  from rest_framework import serializers
  from .models import ContactMessage

  class ContactMessageSerializer(serializers.ModelSerializer):
      class Meta:
          model = ContactMessage
          fields = ["name", "email", "message", "created_at"]
          read_only_fields = ["created_at"]
  ```

- [x] **Create View**
  - Update `shared/views.py` with `ContactFormView`.
  - Use `CreateAPIView` with `AllowAny` permission.
  - Implement `perform_create` to send email notifications.
  ```python
  from django.core.mail import send_mail
  from django.conf import settings
  from rest_framework import generics, permissions
  from .models import ContactMessage
  from .serializers import ContactMessageSerializer

  class ContactFormView(generics.CreateAPIView):
      queryset = ContactMessage.objects.all()
      serializer_class = ContactMessageSerializer
      permission_classes = [permissions.AllowAny]

      def perform_create(self, serializer):
          instance = serializer.save()
          
          # Send email notification
          subject = f"New Contact Message from {instance.name}"
          message = f"Name: {instance.name}\nEmail: {instance.email}\n\nMessage:\n{instance.message}"
          from_email = settings.EMAIL_FROM
          recipient_list = settings.EMAILS_NOTIFICATIONS
          
          if recipient_list and recipient_list != [""]:
              send_mail(subject, message, from_email, recipient_list, fail_silently=True)
  ```

- [x] **Register URLs**
  - Create `shared/urls.py` (if it doesn't exist).
  - Include it in `project/urls.py`.
  ```python
  # shared/urls.py
  from django.urls import path
  from .views import ContactFormView

  urlpatterns = [
      path("contact/", ContactFormView.as_view(), name="contact-form"),
  ]
  ```

## Phase 3: Validation
- [x] **Test Endpoint**
  - Use `curl` or Postman to submit a valid form.
  - Check database record creation.
  - Check email delivery (if using a local SMTP server or `console` backend).
- [x] **Verify Admin UI**
  - Log in to `/admin/` and verify the "Contact Messages" section appears with the correct theme.
