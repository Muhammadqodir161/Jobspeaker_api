from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from applications.models import Application
from jobs.models import JobPosting
from django.db.models import Count

class JobStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_jobs = JobPosting.objects.count()
        total_applications = Application.objects.count()
        jobs_with_most_applications = JobPosting.objects.annotate(app_count=Count("applications")).order_by("-app_count")[:5]

        return Response({
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "top_jobs": [{"job_title": job.title, "applications": job.app_count} for job in jobs_with_most_applications]
        })
