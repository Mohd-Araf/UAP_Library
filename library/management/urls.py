from django.urls import path
from . import views

urlpatterns = [
    path('library/books/', views.book_list, name='book_list'),
    path('borrow/<int:book_id>/', views.borrow_book_view, name='borrow-book'),
    path('borrow/success/<int:borrow_id>/', views.borrow_success_view, name='borrow-success'),
]