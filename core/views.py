from core.permissions import IsRecruiter
from job.models import Job
from job.rest.serializers import JobSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]
