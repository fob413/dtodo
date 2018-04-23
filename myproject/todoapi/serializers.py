from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Todo
        fields = ('id', 'name', 'completed', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
