from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        """save the post data when creating a new bucketlist."""
        serializer.save()
