from django.urls import path
from .views import JobPostingListCreateView, JobPostingDetailView

urlpatterns = [
    path("jobs/", JobPostingListCreateView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobPostingDetailView.as_view(), name="job-detail"),
]
