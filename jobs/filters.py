import django_filters
from django_filters import rest_framework as filters
from companies.models import Company
from job_seekers.models import JobSeeker
from applications.models import Application
from .models import SavedJob, JobPosting

class SavedJobFilter(filters.FilterSet):
    job_posting = filters.CharFilter(field_name="job_posting__title", lookup_expr="icontains")
    job_seeker = filters.CharFilter(field_name="job_seeker__user__email", lookup_expr="icontains")
    saved_after = filters.DateFilter(field_name="saved_at", lookup_expr="gte")
    saved_before = filters.DateFilter(field_name="saved_at", lookup_expr="lte")

    class Meta:
        model = SavedJob
        fields = ['job_posting', 'job_seeker', 'saved_after', 'saved_before']

class JobPostingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    company = django_filters.CharFilter(field_name="company__name", lookup_expr="icontains")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")
    job_type = django_filters.ChoiceFilter(choices=JobPosting.JOB_TYPES)
    experience_level = django_filters.ChoiceFilter(choices=JobPosting.EXPERIENCE_LEVELS)
    salary_min = django_filters.NumberFilter(field_name="salary_min", lookup_expr="gte")
    salary_max = django_filters.NumberFilter(field_name="salary_max", lookup_expr="lte")

    class Meta:
        model = JobPosting
        fields = ['title', 'company', 'location', 'job_type', 'experience_level', 'salary_min', 'salary_max']

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    industry = django_filters.CharFilter(field_name="industry", lookup_expr="icontains")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")

    class Meta:
        model = Company
        fields = ['name', 'industry', 'location']

class JobSeekerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")
    skills = django_filters.CharFilter(field_name="skills__name", lookup_expr="icontains")

    class Meta:
        model = JobSeeker
        fields = ['first_name', 'last_name', 'location', 'skills']
        
class ApplicationFilter(filters.FilterSet):
    job = filters.CharFilter(field_name="job__title", lookup_expr="icontains")
    user = filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    status = filters.CharFilter(field_name="status", lookup_expr="iexact")

    class Meta:
        model = Application
        fields = ["job", "user", "status"]