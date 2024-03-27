from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    rating_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=20, choices=rating_choice, default='4')
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    products =models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=100, choices=order_status, default='Pending')

    def __str__(self):
        return self.products.name




