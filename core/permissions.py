from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    """Allow access only to users with role Recruiter"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Recruiter'

class IsCandidate(BasePermission):
    """Allow access only to users with role Candidate"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Candidate'
