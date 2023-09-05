from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls.base import resolve
from django.urls import reverse
from .views import books_list
from .models import Book, Genre, Comment
from .forms import SearchForm


class BooksURLsTest(TestCase):
    """Testing URLs to check returning status code and requested view"""

    def test_homepage_url_name(self):
        response = self.client.get(reverse('books:books_list'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, books_list)


class SearchTemplateTests(TestCase):
    """Testing a template to check used template and the context of it"""

    def test_homepage_template(self):
        response = self.client.get(reverse('books:book_search'))
        self.assertTemplateUsed(response, 'books/search.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('books:book_search'))
        self.assertContains(response, 'Поиск')


class SearchFormTests(TestCase):
    """Testing search form"""

    def setUp(self):
        self.response = self.client.get(reverse('books:book_search'))

    def test_search_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SearchForm)

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('form')
        self.assertIn('class="form-control mb-1"', form.as_p())

    def test_book_form_validation_for_blank_items(self):
        search_form = SearchForm(
            data={'query': ''}
        )

        self.assertFalse(search_form.is_valid())


class BookGenreCommentUserModelTest(TestCase):
    """Testing Book, Genre, User, Comment model to check creation and retrieving data from models"""

    def setUp(self) -> None:
        self.genre = Genre(
            name='test_genre',
            slug='test_slug'
        )

        self.book = Book(
            title='test_book',
            author='test_author',
            slug='test_book',
            description='test',
            written='2023',
            rating=10,
            genre=self.genre
        )

        self.user = User(
            username='test_user'
        )

        self.comment = Comment(
            book=self.book,
            name='test_name',
            author=self.user,
            email='test@mail.ru',
            body='test'
        )

    def test_create_genre(self):
        self.assertIsInstance(self.genre, Genre)

    def test_create_book(self):
        self.assertIsInstance(self.book, Book)

    def test_create_user(self):
        self.assertIsInstance(self.user, User)

    def test_create_comment(self):
        self.assertIsInstance(self.comment, Comment)

    def test_str_representation(self):
        self.assertEquals(str(self.book), 'test_book - test_author')

    def test_saving_and_retrieving_genre(self):
        self.genre.save()
        saved_genres = Genre.objects.all()
        self.assertEquals(saved_genres.count(), 1)
        self.assertEquals(self.genre.name, 'test_genre')

    def test_saving_and_retrieving_book(self):
        self.genre.save()
        self.book.save()
        saved_books = Book.objects.all()
        self.assertEquals(saved_books.count(), 1)
        self.assertEquals(self.book.genre, self.genre)

    def test_saving_and_retrieving_user(self):
        self.user.save()
        saved_users = User.objects.all()
        self.assertEquals(saved_users.count(), 1)
        self.assertEquals(self.user.username, 'test_user')

    def test_saving_and_retrieving_comment(self):
        self.genre.save()
        self.book.save()
        self.user.save()
        self.comment.save()
        saved_comments = Comment.objects.all()
        self.assertEquals(saved_comments.count(), 1)
        self.assertEquals(self.comment.author, self.user)


class CatalogViewTests(TestCase):
    """Testing views for checking which data will be displayed on this view"""

    def test_book_detail_view(self):
        genre = Genre.objects.create(
            name='test_genre',
            slug='test_slug'
        )

        book_1 = Book.objects.create(
            title='test_book',
            author='test_author',
            slug='test_book',
            description='test',
            written='2023',
            rating=10,
            genre=genre
        )

        response = self.client.get(reverse('books:book_detail', args=[book_1.slug]))

        self.assertIn('test_book', response.content.decode())
        self.assertIn('test', response.content.decode())
