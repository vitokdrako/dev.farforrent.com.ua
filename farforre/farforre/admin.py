from django.contrib import admin
from django.utils.html import format_html
from .models import Page, Customer, GalleryItem, Product
from django.urls import reverse

admin.site.register(Page)
admin.site.register(Customer)
admin.site.register(GalleryItem)

def dublicate_product(modeladmin, request, queryset):
    for product in queryset:
        product.id = None 
        product.save()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'name','prise', 'color', 'article_number', 'availability', 'size', 'weight', 'view_on_site_link')
    list_editable = ('name','prise', 'color', 'article_number', 'availability', 'size', 'weight')
    list_display_links = ('preview_image',)
    search_fields = ('name', 'article_number','color')
    actions = [dublicate_product]
    
    def view_on_site_link(self, obj):
        url = reverse('product_detail', kwargs={'pk': obj.pk})
        return format_html('<a href="{}" target="_blank">Перегляд</a>', url)

    view_on_site_link.short_description = 'Переглянути'

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 65px; height:45px;" />', obj.image.url)
        return ""

    preview_image.short_description = 'Прев\'ю'
