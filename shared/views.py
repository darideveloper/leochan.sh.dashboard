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
