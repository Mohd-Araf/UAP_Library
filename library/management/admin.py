from django.contrib import admin

from .models import Book, borrow_book, BookType

# Register your models here.
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(borrow_book)