from rest_framework import permissions

class IsOwnerReadOnly(permissions.BasePermission):
    """
    Object level permissions for owners only to edit
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner = request.user