from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone


class ReadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.READ)


class Genre(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    class Status(models.TextChoices):
        READ = 'RD', 'READ'
        WANT_TO_READ = 'WR', 'WANT_TO_READ'

    title = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='books_images', default='default_books.jpg')
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    written = models.IntegerField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.READ)
    rating = models.IntegerField()
    published = models.DateTimeField(default=timezone.now())
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')

    objects = models.Manager()
    read = ReadManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['title', 'author']
        indexes = [models.Index(fields=['title', 'author'])]

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug, ])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return f'Comment by {self.name} on {self.book}'
