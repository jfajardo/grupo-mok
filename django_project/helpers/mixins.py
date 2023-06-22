from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class AuthMixin(object):
    """
    Proporciona autenticación básica en las vistas.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class PublicMixin(object):
    """
    Permite el acceso público a las vistas.
    """
    permission_classes = [permissions.AllowAny]
