"""
Views for the Recipe API
"""

from rest_framework import viewsets  # type: ignore
from rest_framework.authentication import TokenAuthentication  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """ view for manage recipe APIs """
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve recipes for authenticated users """
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """ Return the serializer class for the request """
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class
