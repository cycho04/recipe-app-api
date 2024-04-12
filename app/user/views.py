"""
Views for the user API
"""

from rest_framework import generics  # type: ignore
from rest_framework.authtoken.views import ObtainAuthToken  # type: ignore
from rest_framework.settings import api_settings  # type: ignore

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer
)


class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
