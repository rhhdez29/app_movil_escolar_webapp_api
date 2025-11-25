from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdministrador(BasePermission):
    """
    Permite acceso solo a usuarios que pertenecen al grupo 'administrador'.
    """
    def has_permission(self, request, view):
        user = request.user

        # Debe estar autenticado
        if not user or not user.is_authenticated:
            return False

        # Revisar si el usuario pertenece al grupo 'administrador'
        return user.groups.filter(name='administrador').exists()