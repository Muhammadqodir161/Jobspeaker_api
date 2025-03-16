from django.contrib import admin
from .models import JobPosting, SavedJob

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "job_type", "salary_min", "salary_max", "posted_date")
    search_fields = ("title", "company__name", "location")
    list_filter = ("job_type", "experience_level", "education_required", "posted_date", "deadline")
    ordering = ("-posted_date",)

@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ("job_seeker", "job_posting", "saved_date")
    search_fields = ("job_seeker__user__email", "job_posting__title")
    ordering = ("-saved_date",)
