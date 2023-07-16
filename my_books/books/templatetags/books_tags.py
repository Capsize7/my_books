from django.core.cache import cache
from django.db.models import Count
from django.utils.safestring import mark_safe
from django import template
import markdown
from ..models import Book, Genre

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_books():
    books_count = cache.get('books_count')
    if not books_count:
        books_count = Book.read.count()
        cache.set('books_count', books_count, 60 * 10)
    return books_count


@register.inclusion_tag('books/best_books.html')
def show_best_books(count=5):
    best_books = cache.get('best_books')
    if not best_books:
        best_books = Book.read.order_by('-rating')[:count]
        cache.set('best_books', best_books, 60 * 10)
    return {'best_books': best_books}


@register.inclusion_tag('books/commented_books.html')
def get_most_commented_books(count=5):
    most_commented_books = cache.get('most_commented_books')
    if not most_commented_books:
        most_commented_books = Book.read.annotate(
            total_comments=Count('comments')
        ).order_by('-total_comments')[:count]
        cache.set('most_commented_books', most_commented_books, 60*10)
    return {'most_commented_books': most_commented_books}


@register.simple_tag()
def get_genres():
    genres = cache.get('genres')
    if not genres:
        genres = Genre.objects.all()
        cache.set('genres', genres, 60*10)
    return genres


@register.inclusion_tag('books/ordering.html')
def get_ordering(curr_order=None, genre_slug=None, direction=None, author=None):
    ordering = {'title': "Название", 'author': "Автор", 'rating': 'Рейтинг', 'written': "Год написания"}
    return {'ordering': ordering, 'curr_order': curr_order, 'genre_slug': genre_slug, 'direction': direction,
            'author': author}
