from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import BookList, BookDetail, CommentList, CommentDetail

urlpatterns = [
    path("books/", BookList.as_view(), name="books_list"),
    path("books/<int:pk>/", BookDetail.as_view(), name="books_detail"),
    path("comment/", CommentList.as_view(), name="comments_list"),
    path("comment/<int:pk>/", CommentDetail.as_view(), name="comment_detail"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")

]
