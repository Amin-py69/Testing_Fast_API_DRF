from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User


class ChangeUserNamePermission(BasePermission):
    def has_permission(self, request, view):
        if User.objects.filter(username=request.user.username).exists():
            name = request.user.first_name == request.user.username
            return name
