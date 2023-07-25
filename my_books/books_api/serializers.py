from rest_framework import serializers
from books.models import Book, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "written",
            'rating',
            'genre'
        )
        model = Book

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'book',
            'author',
            'created'
        )

        model = Comment
