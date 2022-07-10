from rest_framework import permissions


class IsCreatorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.is_authenticated()
        return True

    def has_object_permission(self, request, view, obj):
        if view.action == "update" or view.action == "destroy":
            return obj.creator == request.user
        return True
