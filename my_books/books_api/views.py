from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            user = self.request.user
            return Comment.objects.filter(author=user)
        return Comment.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def amount_comments(self, request):
        amount = Comment.objects.all().count()
        return Response({'amount_comments': amount})
