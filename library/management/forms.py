from django import forms
from .models import BorrowBook

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowBook
        fields = ['book', 'return_date']
        widgets = {
            'return_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }