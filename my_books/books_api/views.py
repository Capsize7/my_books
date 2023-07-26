from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from books.models import Book, Comment
from .serializers import BookSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['genre__slug']
    ordering_fields = ['title', 'published']
    ordering = ['title']
    permission_classes = IsAuthorOrReadOnly,


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthorOrReadOnly,


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)


    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer