from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        return request.user.is_superuser


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if str(request).find('comment') == -1:
            return request.user.is_superuser
        else:
            return obj.author == request.user