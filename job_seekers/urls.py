from django.urls import path
from .views import JobSeekerListCreateView, JobSeekerDetailView

urlpatterns = [
    path("job_seekers/", JobSeekerListCreateView.as_view(), name="jobseeker-list"),
    path("job_seekers/<int:pk>/", JobSeekerDetailView.as_view(), name="jobseeker-detail"),
]
