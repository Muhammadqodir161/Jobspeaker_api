from django.contrib import admin
from .models import JobSeeker, Skill

@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "location", "experience_years")
    search_fields = ("first_name", "last_name", "user__email", "location")
    list_filter = ("experience_years", "education_level")
    ordering = ("-experience_years",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)
