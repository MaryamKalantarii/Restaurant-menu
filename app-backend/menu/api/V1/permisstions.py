from rest_framework import permissions

class IsAdminAndVerifiedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        return (
            user.is_authenticated and 
            user.is_verified and
            (user.type == 2 or user.type == 3) 
        )