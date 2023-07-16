from django.core.cache import cache
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from taggit.models import Tag
from .forms import EmailPostForm, CommentForm, SearchForm
from .models import *
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity
from django.views.decorators.cache import cache_page


@cache_page(60)
def books_list(request, tag_slug=None, genre_slug=None, ordering='rating', direction='&uarr;', author=None):
    direction_symbols = {'&darr;': '&uarr;', '&uarr;': '&darr;'}
    direction = direction_symbols[direction]
    template = 'books/list.html'
    main = True
    if direction == '&darr;':
        if not author:
            book_list = Book.read.all().order_by('-' + ordering).distinct().prefetch_related('tags')
        else:
            template = 'books/list_author.html'
            book_list = Book.read.all().filter(author=author).order_by('-' + ordering).distinct().prefetch_related(
                'tags')
            main = False
    else:
        if not author:
            book_list = Book.read.all().order_by(ordering).distinct().prefetch_related('tags')
        else:
            template = 'books/list_author.html'
            book_list = Book.read.all().filter(author=author).order_by(ordering).distinct().prefetch_related('tags')
            main = False
    tag = None
    if tag_slug:
        main = False
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])

    if genre_slug:
        main = False
        if genre_slug == 'hochu-prochest':
            if direction == '&darr;':
                book_list = Book.want_to_read.all().order_by('-' + ordering, 'title').distinct().prefetch_related(
                    'tags')
            else:
                book_list = Book.want_to_read.all().order_by(ordering, 'title').distinct().prefetch_related('tags')
        else:
            genre_id = Genre.objects.get(slug=genre_slug).id
            book_list = book_list.filter(genre_id=genre_id).prefetch_related('tags')

    paginator = Paginator(book_list, 3)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    return render(request, template,
                  {'books': books, 'tag': tag, 'genre_slug': genre_slug, 'main': main, 'ordering': ordering,
                   'direction': direction, 'paginator': paginator, 'author': author})


def book_detail(request, book, ordering='-created', read=True, comment_edit=None, comment_id=None):
    book = get_object_or_404(Book, slug=book)
    comments = book.comments.all().order_by(ordering)
    if not comment_edit:
        form = CommentForm()
    else:
        form = CommentForm(instance=Comment.objects.get(id=comment_id))
    book_tags_ids = book.tags.values_list('id', flat=True)
    similar_books = Book.read.filter(tags__in=book_tags_ids) \
        .exclude(id=book.id)
    similar_books = similar_books.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', '-published')[:4]
    auth = request.user.is_authenticated
    return render(request, 'books/detail.html',
                  {'book': book, 'comments': comments, 'form': form, 'similar_books': similar_books, 'auth': auth,
                   'ordering': ordering, 'comment_edit': comment_edit, 'comment_id': comment_id})


def book_share(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book_url = request.build_absolute_uri(
                book.get_absolute_url())
            subject = f"{cd['name']} посоветовал вам прочитать книгу - " \
                      f"{book.title}"
            message = f"С данной книгой можно ознакомиться на  {book_url}\n\n" \
                      f"{cd['name']} оставил комментарий: {cd['comments']}"
            send_mail(subject, message, 'kislinskii1999@mail.ru',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'books/share.html', {'book': book, "form": form, 'sent': sent})


@require_POST
def book_comment(request, book_slug, comment_id=None):
    book = get_object_or_404(Book, slug=book_slug)
    comment = None
    form = None
    if not comment_id:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.author = request.user
            comment.name = request.user.username
            comment.save()
    else:
        comment = Comment.objects.get(id=comment_id)
        comment.body = request.POST['body']
        comment.save()
    return render(request, 'books/comment.html',
                  {'book': book, 'form': form, 'comment': comment, 'comment_id': comment_id})


def book_comment_delete(request, book_slug, comment_id, delete=True):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    book = Book.read.get(slug=book_slug)
    return render(request, 'books/comment.html', {'book': book, 'delete': delete})


def book_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.read.annotate(
                similarity=TrigramSimilarity(('title'), query),
            ).filter(similarity__gt=0.2).order_by('-similarity')
            if not results:
                results = Book.read.annotate(
                    similarity=TrigramSimilarity(('author'), query),
                ).filter(similarity__gt=0.2).order_by('-similarity')

    return render(request,
                  'books/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
