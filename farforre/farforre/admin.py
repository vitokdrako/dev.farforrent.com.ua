from django.contrib import admin
from django.utils.html import format_html
from .models import Page, Customer, GalleryItem, Product

admin.site.register(Page)
admin.site.register(Customer)
admin.site.register(GalleryItem)

def dublicate_product(modeladmin, request, queryset):
    for product in queryset:
        product.id = None 
        product.save()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'name','color', 'article_number', 'availability', 'size', 'weight')
    list_editable = ('name','color', 'article_number', 'availability', 'size', 'weight')
    list_display_links = ('preview_image',)
    search_fields = ('name', 'article_number','color')
    actions = [dublicate_product]

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)
        return ""

    preview_image.short_description = 'Прев\'ю'
