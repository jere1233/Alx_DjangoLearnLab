from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# Existing read-only list API, now requires authentication
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# ViewSet for full CRUD operations, requires authentication
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
