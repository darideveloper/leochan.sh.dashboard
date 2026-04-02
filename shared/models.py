from django.db import models

class Image(models.Model):
    name = models.CharField(
        max_length=255, help_text="A descriptive name for the image."
    )
    image = models.ImageField(
        upload_to="shared/images/",
        help_text="The image file to upload.",
    )
    upload_date = models.DateTimeField(
        auto_now_add=True, help_text="The date and time the image was uploaded."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["-upload_date"]


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
