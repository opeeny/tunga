from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions to only allow owners of an object to edit
jjj
    """
    def has_object_permission(self, request, view, obj):
        #The read permissions are allowed to any requet
        #Always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        #Write permissions are only allowed to the owner of the who creates visitors
        return obj.owner == request.user
        