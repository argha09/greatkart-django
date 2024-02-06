from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    search_fields = ['category_name']
    list_per_page = 5 # No of records per page 

admin.site.register(Category, CategoryAdmin)
