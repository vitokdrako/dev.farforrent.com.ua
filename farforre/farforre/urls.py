"""
URL configuration for farforre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from . import views
from .views import customer_list
from .views import page_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # ... ваші інші URL-шляхи ...
]

urlpatterns += i18n_patterns(
    
    path('register/', views.register, name='register'),
    path("admin/", admin.site.urls),
    path('', views.index, name='home'),  # Використовуйте 'home' як основне ім'я
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('rules/', views.rules, name='rules'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('customers/', customer_list, name='customers'),
    path('page/<slug:slug>/', page_detail, name='page_detail'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

