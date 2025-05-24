from django.contrib import admin
from .models import Category, Product, Order, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'my_order', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('my_order',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount', 'amount', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('my_order',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'product', 'quantity', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('product',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating', 'created_at')
    search_fields = ('name', 'email', 'product__name')
    list_filter = ('rating', 'product')