from rest_framework import permissions


class IsMemberOfGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            if view.action in ('list', 'retrieve'):
                return user.groups.filter(name='Consultor').exists()
            elif view.action in ('create', 'update', 'partial_update', 'destroy'):
                return user.groups.filter(name='Administrador').exists()
        return False
