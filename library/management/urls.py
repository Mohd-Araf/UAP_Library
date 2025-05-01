from django.urls import path
from .views import borrow_book_view
from django.shortcuts import render
urlpatterns = [
    path('borrow/', borrow_book_view, name='borrow-book'),
    path('success/', lambda request: render(request, 'borrowing_book/success.html'), name='borrow-success'),
]
