from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    message = "У вас нет доступа к этой выборке"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerOrStuffPermission(BasePermission):
    message = "У вас нет доступа к этому объявлению"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in ["admin", "moderator"]:
            return True
        return False
