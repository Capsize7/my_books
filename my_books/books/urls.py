from django.urls import path
from .views import *


app_name = 'books'

urlpatterns = [
    path('', books_list, name='books_list'),
    path('search/', book_search, name='book_search'),
    path('author/<str:author>', books_list, name='book_list_by_author'),
    path('<slug:book>/', book_detail, name='book_detail'),
    path('<slug:book>/<str:ordering>', book_detail, name='book_detail'),
    path('<slug:book>/<str:ordering>/<str:comment_edit>/<int:comment_id>', book_detail, name='book_detail_comment_edit'),
    path('tag/<slug:tag_slug>/', books_list, name='book_list_by_tag'),
    path('genre/<slug:genre_slug>/', books_list, name='book_list_by_genre'),
    path('ordering/<slug:ordering>/<str:direction>/', books_list, name='books_list_ordering'),
    path('genre/<slug:genre_slug>/ordering/<slug:ordering>/<str:direction>/', books_list, name='book_list_by_genre_ordering'),
    path('<int:book_id>/share/', book_share, name='book_share'),
    path('<slug:book_slug>/comment/', book_comment, name='book_comment'),
    path('<slug:book_slug>/comment/<int:comment_id>', book_comment, name='book_comment_edit'),

]
