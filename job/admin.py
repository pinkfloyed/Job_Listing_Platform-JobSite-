from django.contrib import admin
from job.models import Job, JobApplication
from shared.base_admin import BaseModelAdmin


@admin.register(Job)
class JobAdmin(BaseModelAdmin):
    list_display = ['uid', 'title', 'recruiter', 'deadline', 'status']
    search_fields = ['title', 'recruiter__email']
    list_filter = ['status', 'is_active', 'deadline']
    ordering = ['-created_at']


@admin.register(JobApplication)
class JobApplicationAdmin(BaseModelAdmin):
    list_display = ['uid', 'job', 'candidate']
    ordering = ['job'] 
    list_filter = ['job']
