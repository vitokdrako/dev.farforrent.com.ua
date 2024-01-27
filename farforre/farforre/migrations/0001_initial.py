# Generated by Django 4.2.7 on 2024-01-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('auto_generate', models.BooleanField(default=False)),
                ('page_name', models.CharField(default='Default Name', max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва товару')),
                ('article_number', models.CharField(max_length=50, verbose_name='Артикул')),
                ('availability', models.CharField(max_length=50, verbose_name='Наявність')),
                ('size', models.CharField(max_length=50, verbose_name='Розмір')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Вага')),
                ('damages', models.CharField(blank=True, max_length=100, verbose_name='Збитки')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Зображення')),
            ],
        ),
    ]