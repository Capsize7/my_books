from django.urls import path
from .views import BookList, BookDetail, CommentList, CommentDetail

urlpatterns = [
    path("", BookList.as_view(), name="books_list"),
    path("<int:pk>/", BookDetail.as_view(), name="books_detail"),
    path("comment/", CommentList.as_view(), name="comments_list"),
    path("comment/<int:pk>/", CommentDetail.as_view(), name="comment_detail"),

]