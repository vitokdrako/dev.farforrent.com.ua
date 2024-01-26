from django.db import models
from django.utils.text import slugify

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    auto_generate = models.BooleanField(default=False)
    page_name = models.CharField(max_length=200, default='Default Name')
    content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class GalleryItem(models.Model):
    name = models.CharField(max_length=100)  # Назва елемента галереї
    image = models.ImageField(upload_to='gallery_images/')  # Зображення елемента галереї

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва товару")
    article_number = models.CharField(max_length=50, verbose_name="Артикул")
    color = models.CharField(max_length=20, blank=True, verbose_name="Колір")
    availability = models.CharField(max_length=50, verbose_name="Наявність")
    size = models.CharField(max_length=50, verbose_name="Розмір")
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Вага")
    damages = models.CharField(max_length=100, blank=True, verbose_name="Збитки")
    image = models.ImageField(upload_to='product_images/', verbose_name="Зображення")

    def __str__(self):
        return self.name