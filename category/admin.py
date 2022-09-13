from django.contrib import admin

from django.contrib.admin import register

from category.models import Category, Brand, Product, ProductType, ProductAttribute, ProductAttributeValue

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

class ProductImageInline(admin.TabularInline)
    model = ProductImage

@register (Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'product_type', 'title', 'is_active', 'category', 'brand')
    list_display_links = ('title')
    list_filter = ('is_active')
    list_editable = ('is_active')
    search_fields = ['upc', 'title', 'category__name', 'brand__name']
    actions = ['active_all']
    inlines = [ProductAttributeValueInline, ProductImageInline]

    def active_all(self, request, queryset):
        pass

    def
