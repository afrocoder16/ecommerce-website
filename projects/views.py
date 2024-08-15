from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Product, UserProfile
from .cart import Cart


# Render your homepage (index.html)
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_listing(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_listing.html', context)

@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    messages.success(request, 'Item added to cart successfully!')
    return redirect('cart_detail')

@login_required
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})

