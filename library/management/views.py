from django.shortcuts import render, redirect
from .forms import BorrowBookForm
from .models import Book

def borrow_book_view(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            book = borrow.book
            if book.total_available > 0:
                book.total_available -= 1
                book.save()
                borrow.save()
                return redirect('borrow-success')
            else:
                form.add_error('book', 'This book is not available.')
    else:
        form = BorrowBookForm()
    return render(request, 'borrowing_book/borrow_book.html', {'form': form})
