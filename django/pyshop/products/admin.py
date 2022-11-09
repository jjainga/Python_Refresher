from django.contrib import admin
from .models import Product, Discount_Offers



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('coupon_code','discription', 'discount_amount')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount_Offers, DiscountAdmin)