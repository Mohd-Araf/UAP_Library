from django.db import models

# Create your models here.
class BookType(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100,unique=True, blank=True, null=True)
    booktype = models.ForeignKey(BookType, on_delete=models.CASCADE)
    author = models.CharField(max_length=100,blank=True, null=True)
    total_available = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='product_pdfs/', blank=True, null=True)
    def __str__(self):
        return self.name


class borrow_book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    def __str__(self):
        return self.book.name
