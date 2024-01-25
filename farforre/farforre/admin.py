from django.contrib import admin
from django.utils.html import format_html
from .models import Page, Customer, GalleryItem, Product

admin.site.register(Page)
admin.site.register(Customer)
admin.site.register(GalleryItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'name', 'article_number', 'availability', 'size', 'weight')
    search_fields = ('name', 'article_number')

    def preview_image(self, obj):
        return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)

    preview_image.short_description = 'Прев\'ю'
