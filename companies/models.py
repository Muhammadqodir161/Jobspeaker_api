from django.db import models
from users.models import User

class Company(models.Model):
    INDUSTRY_CHOICES = [
        ("IT", "IT"),
        ("Finance", "Finance"),
        ("Marketing", "Marketing"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    location = models.CharField(max_length=255)
    founded_year = models.IntegerField()
    logo = models.ImageField(upload_to="company_logos/")
    employees_count = models.IntegerField()

    def __str__(self):
        return self.name
