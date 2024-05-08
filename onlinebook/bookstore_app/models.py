from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=30)
    featured = models.BooleanField(default=False)
    book_author = models.CharField(null=True, default='N/A', max_length=15)
    image = models.ImageField(upload_to='all_books/img')
    book_file = models.FileField(upload_to='all_books')
    book_price = models.IntegerField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_price(self):
        total = 0
        for item in self.cart_items.all():
            total += item.quantity * item.book.book_price
        return total




class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.book.book_price

