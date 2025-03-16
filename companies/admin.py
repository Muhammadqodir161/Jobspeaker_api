from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "industry", "location", "founded_year")
    search_fields = ("name", "industry", "location")
    list_filter = ("industry", "location", "founded_year")
    ordering = ("-founded_year",)

