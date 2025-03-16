from django.db import models
from django.contrib.auth import get_user_model
from jobs.models import JobPosting

User = get_user_model()

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name="applications")
    job_seeker = models.ForeignKey("job_seekers.JobSeeker", on_delete=models.CASCADE)
    job_posting = models.ForeignKey("jobs.JobPosting", on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField()
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("accepted", "Accepted"), ("rejected", "Rejected")],
        default="pending"
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.job.title}"
