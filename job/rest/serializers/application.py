from django.utils import timezone
from job.models import Job, JobApplication
from rest_framework import serializers


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'candidate', 'job', 'cover_letter']
        read_only_fields = ['id', 'candidate']

    def validate(self, data):
        user = self.context['request'].user
        job = data.get('job')

        if job.deadline < timezone.now().date():
            raise serializers.ValidationError("You cannot apply to a job after the deadline.")

        if JobApplication.objects.filter(candidate=user, job=job).exists():
            raise serializers.ValidationError("You have already applied to this job.")

        return data

    def create(self, validated_data):
        validated_data['candidate'] = self.context['request'].user
        return super().create(validated_data)
