from django.contrib import admin
from .models import BookType, Book, BorrowBook
from django.contrib import admin
from .models import Book, BookType, BorrowBook
@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

from django.contrib import admin
from .models import Book, BookType, BorrowBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'booktype', 'author', 'total_available')

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrow_date', 'return_date', 'returned', 'fine_amount')
