from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Product
# Create your views here.

def home_view(request):
    return  render(request,'index.html',{'home':home_view})
def contact_view(request):
    return render(request,'contact.html',{'contact':contact_view})
def blog_view(request):
    return render(request,'blog.html',{'blog':blog_view})
def blogdetails_view(request):
    return render(request,'blog-details.html',{'blog-details':blogdetails_view})
def productdetails_view(request):
    return render(request,'product-details.html',{'product-details':productdetails_view})
def shopcart_view(request):
    return render(request,'shop-cart.html',{'shop-cart':shopcart_view})
def checkout_view(request):
    return render(request,'checkout.html',{'checkout':checkout_view})
def shop_view(request):
    return render(request,'shop.html',{'shop':shop_view})
# def login_view(request):
#     return render(request, 'login.html', {'login':login_view})
def login(request):
    if request.method == 'POST':
        return render(request,'login.html')
# def register_view(request):
#     return render(request, 'register.html', {'register':register_view})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                return HttpResponse('invalid credentials')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
