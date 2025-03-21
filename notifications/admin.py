from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "notification_type", "is_read", "created_at")
    search_fields = ("user__email", "message")
    list_filter = ("notification_type", "is_read", "created_at")
    ordering = ("-created_at",)
