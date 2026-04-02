from django.contrib import admin, messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import action

from utils.media import get_media_url

from .models import Image, ContactMessage

@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ["name", "image_preview", "upload_date"]
    search_fields = ["name"]
    readonly_fields = ["upload_date"]
    actions_row = ["copy_link"]

    class Media:
        js = ["js/copy_clipboard.js"]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px; border-radius: 4px;" />',
                obj.image.url,
            )
        return "No image"

    image_preview.short_description = "Preview"

    @action(description="Copy link")
    def copy_link(self, request: HttpRequest, object_id: int):
        obj = self.get_object(request, object_id)

        # Get url and show message
        image_url = get_media_url(obj.image.url)
        messages.success(request, f"Copied to clipboard: {image_url}")

        # Redirect to the same page with a cookie
        response = redirect(request.META.get("HTTP_REFERER", ".."))
        response.set_cookie("copy_to_clipboard", image_url, max_age=10)

        return response


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ["name", "email", "created_at"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["name", "email", "message", "created_at"]
    date_hierarchy = "created_at"
