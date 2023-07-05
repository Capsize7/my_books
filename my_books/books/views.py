from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from taggit.models import Tag
from .forms import EmailPostForm, CommentForm
from .models import *
from django.db.models import Count


# Create your views here.
def books_list(request, tag_slug=None):
    book_list = Book.read.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])

    paginator = Paginator(book_list, 3)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    return render(request, 'books/list.html', {'books': books, 'tag': tag})


def book_detail(request, book):
    book = get_object_or_404(Book, slug=book,
                             status=Book.Status.READ)
    comments = book.comments.all()
    form = CommentForm()
    book_tags_ids = book.tags.values_list('id', flat=True)
    similar_books = Book.read.filter(tags__in=book_tags_ids) \
        .exclude(id=book.id)
    similar_books = similar_books.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', '-published')[:4]
    return render(request, 'books/detail.html',
                  {'book': book, 'comments': comments, 'form': form, 'similar_books': similar_books})


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
def book_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.book = book
        comment.save()
    return render(request, 'books/comment.html', {'book': book, 'form': form, 'comment': comment})


def book_search(request, ):
    pass
