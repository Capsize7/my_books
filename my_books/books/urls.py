from django.urls import path
from .views import *


app_name = 'books'

urlpatterns = [
    path('', books_list, name='books_list'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<slug:book>/<str:ordering>', book_detail, name='book_detail'),
    path('search/', book_search, name='book_search'),
    path('tag/<slug:tag_slug>/', books_list, name='book_list_by_tag'),
    path('genre/<slug:genre_slug>/', books_list, name='book_list_by_genre'),
    path('ordering/<slug:ordering>/<str:direction>/', books_list, name='books_list_ordering'),
    path('genre/<slug:genre_slug>/ordering/<slug:ordering>/<str:direction>/', books_list, name='book_list_by_genre_ordering'),
    path('<int:book_id>/share/', book_share, name='book_share'),
    path('<int:book_id>/comment/', book_comment, name='book_comment'),

]
