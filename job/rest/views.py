from core.permissions import IsCandidate, IsRecruiter
from django.utils import timezone
from job.models import Job, JobApplication
from job.rest.serializers.application import JobApplicationSerializer
from job.rest.serializers.job import JobSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)
        
class JobApplicationCreateView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()
    permission_classes = [IsCandidate]

    def perform_create(self, serializer):
        user = self.request.user
        job = serializer.validated_data['job']

        if job.deadline < timezone.now().date():
            raise ValidationError("Cannot apply to this job after the deadline.")

        if JobApplication.objects.filter(candidate=user, job=job).exists():
            raise ValidationError("You have already applied to this job.")

        serializer.save(candidate=user)

class JobUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

class JobDeleteView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    def get_queryset(self):
        return Job.objects.filter(recruiter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

class RecruiterDashboardView(APIView):
    permission_classes = [IsRecruiter]

    def get(self, request):
        recruiter = request.user
        jobs = Job.objects.filter(recruiter=recruiter)
        applications = JobApplication.objects.filter(job__in=jobs)

        total_jobs = jobs.count()
        total_closed = jobs.filter(is_active=False).count()
        total_applications = applications.count()
        total_hired = applications.filter(status="Hired").count()
        total_rejected = applications.filter(status="Rejected").count()

        return Response({
            "total_published_jobs": total_jobs,
            "total_closed_jobs": total_closed,
            "total_candidate_applications": total_applications,
            "total_candidates_hired": total_hired,
            "total_candidates_rejected": total_rejected,
        })

class JobListPublicView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True, status="open")
    serializer_class = JobSerializer
    permission_classes = [AllowAny]