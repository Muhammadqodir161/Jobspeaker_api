from django.db import models
from companies.models import Company
from job_seekers.models import Skill
from django.contrib.auth import get_user_model

class JobPosting(models.Model):
    JOB_TYPES = [
        ("full_time", "To‘liq ish kuni"),
        ("part_time", "Yarim kun"),
        ("contract", "Shartnoma asosida"),
        ("internship", "Amaliyot"),
    ]
    
    EXPERIENCE_LEVELS = [
        ("entry", "Boshlang‘ich"),
        ("mid", "O‘rta"),
        ("senior", "Senior"),
        ("executive", "Raxbariyat"),
    ]
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="job_postings")
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS)
    education_required = models.CharField(max_length=255)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    skills_required = models.ManyToManyField(Skill, related_name="job_postings")
    is_active = models.BooleanField(default=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

User = get_user_model()

class SavedJob(models.Model):
    job_seeker = models.ForeignKey("job_seekers.JobSeeker", on_delete=models.CASCADE, related_name="saved_jobs")
    job_posting = models.ForeignKey("jobs.JobPosting", on_delete=models.CASCADE, related_name="saved_by_users")
    saved_at = models.DateTimeField(auto_now_add=True)
    saved_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('job_seeker', 'job_posting')
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.job_seeker.user.email} saved {self.job_posting.title}"