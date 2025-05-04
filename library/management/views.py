from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BorrowBook
from .forms import BorrowBookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'borrowing_book/book_list.html', {'books': books})


def borrow_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.book = book
            if book.total_available > 0:
                book.total_available -= 1
                book.save()
                borrow.save()
                return redirect('borrow-success', borrow_id=borrow.id)
            else:
                form.add_error('book', 'This book is not available.')
    else:
        form = BorrowBookForm(initial={'book': book})
    return render(request, 'borrowing_book/borrow_book.html', {'form': form, 'book': book})


from django.shortcuts import render, get_object_or_404
from .models import BorrowBook

def borrow_success_view(request, borrow_id):
    borrow = get_object_or_404(BorrowBook, id=borrow_id)
    return render(request, 'borrowing_book/success.html', {'borrow': borrow})