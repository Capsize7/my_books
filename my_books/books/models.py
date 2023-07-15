from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone


class ReadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.READ)

class WantToReadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.WANT_TO_READ)


class Genre(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Слаг')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    class Status(models.TextChoices):
        READ = 'RD', 'READ'
        WANT_TO_READ = 'WR', 'WANT_TO_READ'

    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    author = models.CharField(max_length=250, verbose_name='Автор')
    photo = models.ImageField(upload_to='books_images', default='books_images/default_book.png', verbose_name='Обложка')
    slug = models.SlugField(max_length=250, verbose_name='Cлаг')
    description = models.TextField(verbose_name='Описание')
    written = models.IntegerField(verbose_name="Год издания")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.READ, verbose_name='Cтатус')
    rating = models.IntegerField(verbose_name='Рейтинг')
    published = models.DateTimeField(default=timezone.now(), verbose_name="Дата внесения в базу")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres', verbose_name='Жанр')

    objects = models.Manager()
    read = ReadManager()
    want_to_read = WantToReadManager()
    tags = TaggableManager(verbose_name='Теги')

    class Meta:
        ordering = ['-rating']
        indexes = [models.Index(fields=['title', 'author'])]
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name='Книга')
    name = models.CharField(max_length=80, verbose_name='Имя')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors', verbose_name='Автор')
    email = models.EmailField(verbose_name='Почта')
    body = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.name} на книгу - {self.book}'
