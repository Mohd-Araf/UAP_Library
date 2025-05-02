from django.urls import path
from . import views

urlpatterns = [
    path('borrow/', views.borrow_book_view, name='borrow-book'),
    path('borrow/success/<int:borrow_id>/', views.borrow_success_view, name='borrow-success'),
]