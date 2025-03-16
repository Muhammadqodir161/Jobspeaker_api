from django.db import models
from users.models import User

class JobSeeker(models.Model):
    EDUCATION_LEVELS = [
        ("bachelor", "Bachelor"),
        ("master", "Master"),
        ("phd", "PhD"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="job_seeker")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    bio = models.TextField()
    skills = models.ManyToManyField("Skill", related_name="job_seekers")
    experience_years = models.IntegerField()
    education_level = models.CharField(max_length=50, choices=EDUCATION_LEVELS)
    resume = models.FileField(upload_to="resumes/")
    profile_picture = models.ImageField(upload_to="profile_pictures/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    CATEGORIES = [
        ("Programming", "Programming"),
        ("Design", "Design"),
        ("Marketing", "Marketing"),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return self.name
