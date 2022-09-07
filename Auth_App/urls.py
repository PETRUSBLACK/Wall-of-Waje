from django.urls import path

from .views import AuthorList, AuthorDetail, BooksList, BooksDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='list'),
    path('authors/pk/', AuthorDetail.as_view(), name='detail'),
    path('books/', BooksList.as_view(), name='list'),
    path('authors/pk/', BooksDetail.as_view(), name='detail'),
]