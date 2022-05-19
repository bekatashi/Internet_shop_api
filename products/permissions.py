from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser is True

