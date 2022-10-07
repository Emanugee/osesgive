from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.username


# PURPOSE = [
#     ('Offering','Offering'),
#     ('Tithe','Tithe'),
#     ('Thanksgiving','Thanksgiving'),
#     ('Transport','Transport'),
#     ('Project 22','Project 22'),
#     ('Shiloh Sacrifice','Shiloh Sacrifice'),
#     ('Welfare','Welfare'),
#     ('Prophet Offering','Prophet Offering'),
# ] 
class PaymentOption(models.Model):
    option = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    amount = models.IntegerField()
    email = models.EmailField(max_length=254)
    paid = models.BooleanField(default=False)
    phone = models.CharField(max_length=50)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    phone = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    admin_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

