from django.urls import path
from job.rest.views import (JobApplicationCreateView, JobCreateView,
                            JobDeleteView, JobListPublicView, JobUpdateView,
                            RecruiterDashboardView)

urlpatterns = [
    path('jobs/create/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('jobs/apply/', JobApplicationCreateView.as_view(), name='job-apply'),
    path('recruiter/dashboard/', RecruiterDashboardView.as_view(), name='recruiter-dashboard'),
    path("all/", JobListPublicView.as_view(), name="job-public-list"),
]