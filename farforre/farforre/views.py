from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Customer, Page

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def rules(request):
    return render(request, 'rules.html')

def favorites(request):
    return render(request, 'favorites.html')

def search(request):
    return render(request, 'search.html')

def cart(request):
    return render(request, 'cart.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def page_detail(request, slug):
    # Отримання сторінки за слагом або відображення 404 помилки, якщо вона не існує
    page = get_object_or_404(Page, slug=slug)

    # Відправлення даних сторінки у шаблон
    return render(request, 'page_detail.html', {'page': page})