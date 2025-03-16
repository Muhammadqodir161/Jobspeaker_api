from rest_framework import serializers
from .models import JobPosting, SavedJob

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = "__all__"

class SavedJobSerializer(serializers.ModelSerializer):
    job_posting_title = serializers.CharField(source="job_posting.title", read_only=True)

    class Meta:
        model = SavedJob
        fields = ['id', 'job_seeker', 'job_posting', 'job_posting_title', 'saved_at']
        read_only_fields = ['saved_at']