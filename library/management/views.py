from django.shortcuts import render, redirect, get_object_or_404
from .forms import BorrowBookForm
from .models import Book, BorrowBook

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
                return redirect('borrow-success', borrow_id=borrow.id)
            else:
                form.add_error('book', 'This book is not available.')
    else:
        form = BorrowBookForm()
    return render(request, 'borrowing_book/borrow_book.html', {'form': form})

def borrow_success_view(request, borrow_id):
    borrow = get_object_or_404(BorrowBook, id=borrow_id)
    return render(request, 'borrowing_book/success.html', {'borrow': borrow})