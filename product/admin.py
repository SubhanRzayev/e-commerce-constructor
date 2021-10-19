from django.contrib import admin

from product.models import (Product,Size,Color,Category,Image,Price,BrandSlider)

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','discount_price','description','quantity','products_image','is_published']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','icon']


@admin.register(Color)
class Color(admin.ModelAdmin):
    list_display = ['color']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['price']

@admin.register(BrandSlider)
class BrandSliderAdmin(admin.ModelAdmin):
    list_display = ['image']




