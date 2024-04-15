"""
Serializers for Recipe API
"""

from rest_framework import serializers  # type: ignore
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for recipes """

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
