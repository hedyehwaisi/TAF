from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^(09|\+989)\d{8}$', message="Phone number must be in the format '09xxxxxxxx' or '+989xxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedIn_addr = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
