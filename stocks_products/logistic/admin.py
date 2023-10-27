from django.contrib import admin

from .models import Product, Stock, StockProduct


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class Stock(admin.ModelAdmin):
    pass
# Register your models here.


@admin.register(StockProduct)
class StockProduct(admin.ModelAdmin):
    pass
