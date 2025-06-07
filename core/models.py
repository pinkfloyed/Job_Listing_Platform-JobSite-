from core.choices import GenderChoices
from core.managers import UserManager
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from shared.base_model import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    RECRUITER = 'Recruiter'
    CANDIDATE = 'Candidate'
    ROLE_CHOICES = [
        (RECRUITER, 'Recruiter'),
        (CANDIDATE, 'Candidate'),
    ]
    username = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.CharField(max_length=128, blank=True)
    new_password = models.CharField(max_length=128, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='candidate')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"uid:{self.uid} {self.email}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
            self.username = self.email if not self.username else self.username

        if self.new_password:
            self.password = make_password(self.new_password)
            self.new_password = ""

        super().save(*args, **kwargs)


class UserProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(upload_to="profile_pictures/", blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=GenderChoices.choices, default=GenderChoices.NOT_SET
    )

    def __str__(self):
        return f"Profile of {self.user.email}"

class JobApplication(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey('job.Job', on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate', 'job')

    def __str__(self):
        return f"{self.candidate.email} - {self.job.title}"
