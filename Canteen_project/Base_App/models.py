from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)
    
    def __str__(self): 
           return self.Category_name
    
class Items(models.Model):
        Item_name = models.CharField(max_length=15)
        #Category_name = models.CharField(max_length=15)
        description = models.TextField(blank=False)
        price = models.IntegerField()
        Category = models.ForeignKey(ItemList, related_name= 'Name', on_delete=models.CASCADE)
        Image = models.ImageField(upload_to='items/', default='default.jpg')
        def __str__(self): 
             return self.Item_name
   

class AboutUs(models.Model):
            Description = models.TextField(blank=False)

class Feedback(models.Model):
            User_name = models.CharField(max_length=15)
            description = models.TextField(blank=False)
            Rating = models.IntegerField()

            def __str__(self): 
             return self.User_name

class BookTable(models.Model):
        Name = models.CharField(max_length=15)
        Phone_number = models.IntegerField()
        Email = models.EmailField()
        Total_person = models.IntegerField()
        Booking_date = models.DateField()
        def __str__(self): 
           return self.Name
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   # added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product.Item_name} x {self.quantity}"

    def get_total(self):
        return self.quantity * self.product.price
    
from django.db import models

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)  # Linking to User model (you can replace with your user model)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Payment amount
    payment_method = models.CharField(max_length=50, default='Online')  # or whatever default you want
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)  # If you're using Razorpay
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)  # If you're using Razorpay
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} - {self.payment_status}"
