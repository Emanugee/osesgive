from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'phone', 'email']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name','last_name', 'amount', 'phone', 'paid','pay_code','payment_date']

@admin.register(PaymentOption)
class PaymentOptionAdmin(admin.ModelAdmin):
    list_display = ['id','option']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'phone', 'added']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Payment, PaymentAdmin)