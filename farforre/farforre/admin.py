from django.contrib import admin
from .models import Page, Customer, GalleryItem

# Зареєструйте ваші моделі тут
admin.site.register(Page)
admin.site.register(Customer)
admin.site.register(GalleryItem)

# Ваші інші налаштування...
