from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job_seeker", "job_posting", "status", "applied_date")
    search_fields = ("job_seeker__user__email", "job_posting__title")
    list_filter = ("status", "applied_date")
    ordering = ("-applied_date",)
    readonly_fields = ("applied_date", "updated_date")
