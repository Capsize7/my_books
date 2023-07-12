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
    return Book.read.count()


@register.inclusion_tag('books/best_books.html')
def show_best_books(count=5):
    best_books = Book.read.order_by('-rating')[:count]
    return {'best_books': best_books}


@register.inclusion_tag('books/commented_books.html')
def get_most_commented_books(count=5):
    most_commented_books = Book.read.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    return {'most_commented_books': most_commented_books}


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.inclusion_tag('books/ordering.html')
def get_ordering(curr_order=None, genre_slug=None, direction=None):
    ordering = {'title': "Название", 'author': "Автор", 'rating': 'Рейтинг', 'written': "Год написания"}
    return {'ordering': ordering, 'curr_order': curr_order, 'genre_slug': genre_slug, 'direction': direction}
