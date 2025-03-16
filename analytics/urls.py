from django.urls import path
from .views import JobStatsView

urlpatterns = [
    path("analytics/jobs/", JobStatsView.as_view(), name="job-stats"),
]
