from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Image

@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ["name", "image_preview", "upload_date"]
    search_fields = ["name"]
    readonly_fields = ["upload_date"]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px; border-radius: 4px;" />',
                obj.image.url,
            )
        return "No image"
    
    image_preview.short_description = "Preview"
