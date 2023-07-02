from django.urls import path
from .views import *


app_name = 'books'

urlpatterns = [
    path('', books_list, name='books_list'),
    path('tag/<slug:tag_slug>/', books_list, name='books_list_by_tag'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<int:book_id>/share/', book_share, name='book_share'),
    path('<int:book_id>/comment/', book_comment, name='book_comment'),
    path('search/', book_search, name='book_search'),
]