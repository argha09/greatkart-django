from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock','category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    search_fields = ['product_name']
    list_per_page = 7 # No of records per page 

admin.site.register(Product, ProductAdmin)
